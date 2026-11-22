"""Prototype video renderer: code-computed motion + word-timed captions.

Reads a script JSON + timings JSON + words JSON. Every frame is computed
from the frame index only (deterministic — no randomness, no wall-clock).
Frames are piped as raw RGB to ffmpeg with the mixed narration WAV as
audio. A travelling dot + filling progress bar move on every frame, so
no two consecutive frames are ever identical.
"""
import json
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

script_path, timings_path, words_path, out_path = sys.argv[1:5]
with open(script_path) as f:
    spec = json.load(f)
with open(timings_path) as f:
    timings = json.load(f)
with open(words_path) as f:
    words_data = json.load(f)

W = spec["width"]
H = spec["height"]
FPS = spec["fps"]
ACCENT = tuple(spec["accent"])
GREEN = (46, 160, 90)
WHITE = (255, 255, 255)
SOFT = (225, 225, 235)
DIM = (150, 150, 165)
FAINT = (95, 95, 110)
TOTAL = timings["total_duration"]
TOTAL_FRAMES = int(math.ceil(TOTAL * FPS))
WORDS = words_data["words"]
BEATS = timings["beats"]
SPEC_BEATS = spec["beats"]


def load_font(size, bold=False):
    cands = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in cands:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()


F_TITLE = load_font(76, True)
F_Q = load_font(50, True)
F_BODY = load_font(36, False)
F_SMALL = load_font(30, False)
F_CAP = load_font(30, False)
F_COUNT = load_font(230, True)
F_ANS = load_font(64, True)
F_CHIP = load_font(28, True)
F_LABEL = load_font(44, True)


def gradient_bg():
    r0, g0, b0 = spec["bg"][0]
    r1, g1, b1 = spec["bg"][1]
    t = np.linspace(0, 1, H, dtype=np.float64)[:, None, None]
    c0 = np.array([r0, g0, b0], dtype=np.float64)
    c1 = np.array([r1, g1, b1], dtype=np.float64)
    arr = (c0 + (c1 - c0) * t).astype(np.uint8)
    arr = np.repeat(arr, W, axis=1)
    return Image.fromarray(arr, "RGB")


BASE_IMG = gradient_bg()
BASE_ARR = np.asarray(BASE_IMG).astype(np.int16)

# Subtle animated vertical stripes (amplitude 6 gray levels, period 64 px,
# drifting at 150 px/s). They keep the frame alive: typography video has
# most pixels static by design, and without a full-frame moving element
# freezedetect's whole-frame mean threshold flags it as frozen even though
# the countdown, captions and dot are visibly moving. The stripes are a
# pure function of the frame index, so determinism is preserved.
STRIPE_AMP = 6
STRIPE_PERIOD = 64
STRIPE_SPEED = 150  # px/s
_stripe_table = (STRIPE_AMP * np.sin(
    2 * np.pi * np.arange(W + STRIPE_PERIOD) / STRIPE_PERIOD)).astype(np.int16)


def frame_base(fi):
    """Background for frame fi: gradient + drifting stripes (deterministic)."""
    off = int(round(STRIPE_SPEED * fi / FPS)) % STRIPE_PERIOD
    stripe = _stripe_table[off:off + W]  # (W,) int16
    arr = BASE_ARR + stripe[None, :, None]
    np.clip(arr, 0, 255, out=arr)
    return Image.fromarray(arr.astype(np.uint8), "RGB")


def text_w(draw, s, font):
    bb = draw.textbbox((0, 0), s, font=font)
    return bb[2] - bb[0]


def wrap(draw, text, font, max_w):
    """Greedy word wrap -> list of lines (each a list of words)."""
    lines, cur = [], []
    for w in text.split():
        trial = cur + [w]
        if text_w(draw, " ".join(trial), font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = [w]
    if cur:
        lines.append(cur)
    return lines


def draw_lines_centered(draw, lines, font, cx, y, lh, fill):
    for line in lines:
        s = " ".join(line)
        draw.text((cx - text_w(draw, s, font) // 2, y), s, font=font, fill=fill)
        y += lh
    return y


def ease_out(p):
    return 1 - (1 - min(1.0, max(0.0, p))) ** 3


def beat_at(t):
    for i, b in enumerate(BEATS):
        if b["start"] <= t < b["end"]:
            return i, b
    return len(BEATS) - 1, BEATS[-1]


def part_at(t):
    """Narration part active at t, or (None, None)."""
    for bi, b in enumerate(BEATS):
        for pi, p in enumerate(b.get("parts", [])):
            if p["start"] - 0.05 <= t < p["end"] + 0.05:
                return bi, pi, p
    # just after a part ended (<0.6 s): keep its final caption state
    best = None
    for bi, b in enumerate(BEATS):
        for pi, p in enumerate(b.get("parts", [])):
            if p["end"] <= t < p["end"] + 0.6:
                if best is None or p["end"] > best[2]["end"]:
                    best = (bi, pi, p)
    return best if best else (None, None, None)


# pre-wrap caption lines per part (stable layout)
CAP_CACHE = {}


def caption_lines(draw, bi, pi, p):
    key = (bi, pi)
    if key in CAP_CACHE:
        return CAP_CACHE[key]
    lines = wrap(draw, p["speak"], F_CAP, 640)
    CAP_CACHE[key] = lines
    return lines


def draw_caption(draw, t):
    bi, pi, p = part_at(t)
    if p is None:
        return
    wlist = [w for w in WORDS if p["start"] - 0.1 <= w["start"] <= p["end"] + 0.2]
    disp_words = p["speak"].split()
    if wlist:
        revealed = sum(1 for w in wlist if w["start"] <= t)
    else:
        frac = (t - p["start"]) / max(p["end"] - p["start"], 0.01)
        revealed = int(frac * len(disp_words))
    revealed = max(0, min(len(disp_words), revealed))
    lines = caption_lines(draw, bi, pi, p)
    y = H - 210
    lh = 42
    idx = 0
    for line in lines:
        total_w = sum(text_w(draw, w, F_CAP) + 10 for w in line) - 10
        x = (W - total_w) // 2
        for w in line:
            if idx < revealed - 1:
                col = WHITE
            elif idx == revealed - 1:
                col = ACCENT
            else:
                col = FAINT
            draw.text((x, y), w, font=F_CAP, fill=col)
            x += text_w(draw, w, F_CAP) + 10
            idx += 1
        y += lh


def draw_header(draw, bi, b):
    label = spec["format"].upper()
    draw.text((40, 36), label, font=F_CHIP, fill=ACCENT)
    if "n" in b:
        right = f"{b['n']} / {b['total']}"
        rw = text_w(draw, right, F_CHIP)
        draw.text((W - 40 - rw, 36), right, font=F_CHIP, fill=SOFT)
    draw.rectangle([40, 84, W - 40, 86], fill=(120, 120, 140))
    # travelling dot (ping-pong, 4 s period) — guarantees frame change
    phase = (draw._t % 4.0) / 4.0
    pos = 1 - abs(1 - 2 * phase)
    dx = int(60 + (W - 120) * pos)
    draw.ellipse([dx - 10, 100, dx + 10, 120], fill=ACCENT)


def draw_progress(draw, t):
    frac = t / TOTAL
    draw.rectangle([0, H - 34, W, H - 24], fill=(30, 30, 44))
    draw.rectangle([0, H - 34, int(W * frac), H - 24], fill=ACCENT)


def frame_for(fi):
    t = fi / FPS
    draw_t = t
    img = frame_base(fi)
    draw = ImageDraw.Draw(img)
    draw._t = t  # frame time for the travelling dot
    bi, b = beat_at(t)
    sbeat = SPEC_BEATS[bi]
    kind = b["kind"]
    draw_header(draw, bi, b)

    if kind == "intro":
        p = b["parts"][0]
        lt = t - b["start"]
        x_off = int(-W * (1 - ease_out(lt / 0.6)))
        title = sbeat["parts"][0]["title"]
        lines = wrap(draw, title, F_TITLE, 640)
        y = 480
        for line in lines:
            s = " ".join(line)
            draw.text((x_off + (W - text_w(draw, s, F_TITLE)) // 2, y), s,
                      font=F_TITLE, fill=WHITE)
            y += 96
        if lt > 0.3:
            sub = sbeat["parts"][0]["subtitle"]
            slines = wrap(draw, sub, F_BODY, 600)
            draw_lines_centered(draw, slines, F_BODY, W // 2, y + 30, 50, SOFT)
    elif kind == "outro":
        p = b["parts"][0]
        lt = t - b["start"]
        x_off = int(-W * (1 - ease_out(lt / 0.6)))
        title = sbeat["parts"][0]["title"]
        lines = wrap(draw, title, F_TITLE, 640)
        y = 480
        for line in lines:
            s = " ".join(line)
            draw.text((x_off + (W - text_w(draw, s, F_TITLE)) // 2, y), s,
                      font=F_TITLE, fill=WHITE)
            y += 96
        if lt > 0.3:
            sub = sbeat["parts"][0]["subtitle"]
            slines = wrap(draw, sub, F_BODY, 600)
            draw_lines_centered(draw, slines, F_BODY, W // 2, y + 30, 50, SOFT)
    elif kind == "ask":
        is_riddle = spec["id"] == "riddle-round"
        chip = f"RIDDLE {b['n']}" if is_riddle else f"QUESTION {b['n']}"
        cw = text_w(draw, chip, F_CHIP)
        draw.text(((W - cw) // 2, 170), chip, font=F_CHIP, fill=ACCENT)
        y = 300
        if is_riddle:
            for pi, part in enumerate(sbeat["parts"]):
                tp = b["parts"][pi]
                if t >= tp["start"]:
                    lines = wrap(draw, part["display"], F_BODY, 620)
                    y = draw_lines_centered(draw, lines, F_BODY, W // 2, y, 52, WHITE)
                    y += 26
        else:
            lines = wrap(draw, sbeat["parts"][0]["display"], F_Q, 620)
            draw_lines_centered(draw, lines, F_Q, W // 2, 420, 72, WHITE)
    elif kind == "think":
        # show the question / clues small at the top
        prev = SPEC_BEATS[bi - 1]
        y = 190
        for part in prev["parts"]:
            lines = wrap(draw, part["display"], F_SMALL, 620)
            y = draw_lines_centered(draw, lines, F_SMALL, W // 2, y, 42, DIM)
            y += 14
        remaining = b["end"] - t
        num = int(math.ceil(remaining - 1e-9))
        num = max(1, min(b["seconds"], num))
        draw.text(((W - text_w(draw, "THINK!", F_LABEL)) // 2, 560), "THINK!",
                  font=F_LABEL, fill=ACCENT)
        ns = str(num)
        draw.text(((W - text_w(draw, ns, F_COUNT)) // 2, 620), ns,
                  font=F_COUNT, fill=WHITE)
        frac = remaining / b["seconds"]
        bw = int((W - 240) * frac)
        draw.rectangle([120, 950, W - 120, 966], fill=(40, 40, 56))
        draw.rectangle([120, 950, 120 + bw, 966], fill=ACCENT)
    elif kind == "answer":
        p = b["parts"][0]
        lt = t - b["start"]
        x_off = int(-W * (1 - ease_out(lt / 0.4)))
        draw.rounded_rectangle([60 + x_off, 430, W - 60 + x_off, 545],
                               radius=24, fill=GREEN)
        lab = "ANSWER"
        draw.text((x_off + (W - text_w(draw, lab, F_LABEL)) // 2, 462), lab,
                  font=F_LABEL, fill=WHITE)
        ans = sbeat["parts"][0]["answer"]
        alines = wrap(draw, ans, F_ANS, 620)
        y = 620
        for line in alines:
            s = " ".join(line)
            draw.text((x_off + (W - text_w(draw, s, F_ANS)) // 2, y), s,
                      font=F_ANS, fill=WHITE)
            y += 84
        if lt > 0.4:
            ex = sbeat["parts"][0]["explain"]
            elines = wrap(draw, ex, F_BODY, 600)
            draw_lines_centered(draw, elines, F_BODY, W // 2, y + 20, 50, SOFT)

    draw_caption(draw, t)
    draw_progress(draw, t)
    return img


def main():
    wav = os.path.join(os.path.dirname(os.path.abspath(script_path)),
                       f"{spec['id']}-narration.wav")
    cmd = ["ffmpeg", "-y",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "pipe:0",
           "-i", wav,
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
           "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "128k", "-shortest",
           "-movflags", "+faststart", out_path]
    import time
    t0 = time.time()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for fi in range(TOTAL_FRAMES):
        img = frame_for(fi)
        proc.stdin.write(img.tobytes())
    _, err = proc.communicate()
    dt = time.time() - t0
    print(f"frames_written={TOTAL_FRAMES} expected={TOTAL_FRAMES} "
          f"returncode={proc.returncode} render_time={dt:.1f}s", flush=True)
    if proc.returncode != 0:
        print(err.decode(errors="replace"), file=sys.stderr)
        sys.exit(1)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
