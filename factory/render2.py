"""Prototype video renderer v2: safe-zone layout + icons + micro-animation.

Reads a script JSON + timings JSON + words JSON (same inputs as v1).
Every frame is computed from the frame index only (deterministic — no
randomness, no wall-clock). Frames are piped as raw RGB to ffmpeg with
the EXISTING mixed narration WAV as audio (no re-synthesis).

Layout (factory/layout.py, TikTok In-Feed ads template on 720x1280):
safe box x 80-640, y 160-840; below y=560 text ends at x<=520, so body
content is centred on x=300, max 440 wide. Captions live in the
subtitle band (bottom-anchored at y=830) and show only the current
sentence. Captions are suppressed during ask beats (the question/clue
is already on screen as large text) and think beats (no speech).
The static explain text is gone: the spoken explanation is shown
word-by-word in the caption band instead.

Icons (factory/icons.py, original code-drawn shapes): phase icon in
the header slot, checkmark tick-draw + pop-in answer banner, pulsing
countdown number, slide/pop title.

Verification: the safe-zone checker runs on EVERY frame's recorded
text boxes. Any box outside the safe box fails the render (exit 1),
exactly like a black or frozen frame. Results go to
<out>-safezone.json next to the video.
"""
import json
import math
import os
import re
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout
import icons

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

# --- per-frame text-box recording (for the safe-zone checker) ---
BOXES = []


def rec(x0, y0, x1, y1, label):
    BOXES.append((x0, y0, x1, y1, label))


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


F_TITLE = load_font(64, True)
F_Q = load_font(50, True)
F_BODY = load_font(36, False)
F_SMALL = load_font(28, False)
F_CAP = load_font(30, False)
F_ANS = load_font(48, True)
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

STRIPE_AMP = 6
STRIPE_PERIOD = 64
STRIPE_SPEED = 150  # px/s
_stripe_table = (STRIPE_AMP * np.sin(
    2 * np.pi * np.arange(W + STRIPE_PERIOD) / STRIPE_PERIOD)).astype(np.int16)


def frame_base(fi):
    off = int(round(STRIPE_SPEED * fi / FPS)) % STRIPE_PERIOD
    stripe = _stripe_table[off:off + W]
    arr = BASE_ARR + stripe[None, :, None]
    np.clip(arr, 0, 255, out=arr)
    return Image.fromarray(arr.astype(np.uint8), "RGB")


def text_w(draw, s, font):
    bb = draw.textbbox((0, 0), s, font=font)
    return bb[2] - bb[0]


def wrap(draw, text, font, max_w):
    """Greedy word wrap. Returns a list of word lists.

    Width is the LARGER of the two ways a line can be drawn, because
    the renderer has both: draw_lines_centered_r draws the joined
    string (natural space glyph, ~8 px at 30 pt but ~12 px at 44 pt),
    while draw_text_block/draw_caption draw words with a fixed 10 px
    gap. Measuring only one way overflows the other: the joined-only
    measure let a 30 pt caption draw 446 wide in a 440 column (56
    outro frames failed), and the gap-only measure let a 44 pt
    question line draw 459 wide (Q5 "In what year did"). Taking the
    max of both is conservative for either draw path and can never
    overflow the column.
    """
    lines, line = [], []
    for w in text.split():
        trial = line + [w]
        joined_w = text_w(draw, " ".join(trial), font)
        gap_w = sum(text_w(draw, x, font) + 10 for x in trial) - 10
        if line and max(joined_w, gap_w) > max_w:
            lines.append(line)
            line = [w]
        else:
            line = trial
    if line:
        lines.append(line)
    return lines


def draw_text_r(draw, s, font, x, y, fill, label):
    """Draw text at (x, y) and record its true ink box."""
    bb = draw.textbbox((0, 0), s, font=font)
    draw.text((x, y), s, font=font, fill=fill)
    rec(x + bb[0], y + bb[1], x + bb[2], y + bb[3], label)
    return bb[2] - bb[0]


def fit_stack(n_lines, n_groups, y_top, y_bottom, lh=48, gap=20,
              line_h=44, min_lh=40, min_gap=8):
    """Shrink a vertical stack's leading/gap until it fits.

    A stack of n_lines lines in n_groups groups, first line at y_top,
    spans (n_lines-1)*lh + (n_groups-1)*gap + line_h. If that exceeds
    y_bottom - y_top, reduce the leading (then the gap) until it fits.
    This is what keeps the riddle clue stack inside the safe box: the
    three clues wrap to up to 10 lines, which at the default 48/20
    reaches y=846, 6 px past the safe-box bottom. Returns (lh, gap).
    """
    while (n_lines - 1) * lh + max(0, n_groups - 1) * gap + line_h \
            > y_bottom - y_top and (lh > min_lh or gap > min_gap):
        if lh > min_lh:
            lh -= 2
        elif gap > min_gap:
            gap -= 2
    return lh, gap


def draw_lines_centered_r(draw, lines, font, cx, y, lh, fill, label):
    """Draw wrapped lines centred on cx; record each line's box."""
    for line in lines:
        s = " ".join(line)
        w = text_w(draw, s, font)
        draw_text_r(draw, s, font, cx - w // 2, y, fill, label)
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
    for bi, b in enumerate(BEATS):
        for pi, p in enumerate(b.get("parts", [])):
            if p["start"] - 0.05 <= t < p["end"] + 0.05:
                return bi, pi, p
    best = None
    for bi, b in enumerate(BEATS):
        for pi, p in enumerate(b.get("parts", [])):
            if p["end"] <= t < p["end"] + 0.6:
                if best is None or p["end"] > best[2]["end"]:
                    best = (bi, pi, p)
    return best if best else (None, None, None)


# --- pre-rendered assets (built once, reused every frame) ---
PHASE_ICONS = {
    "question": icons.icon_question(48),
    "lightbulb": icons.icon_lightbulb(48),
    "clock": icons.icon_clock(48),
    "star": icons.icon_star(48),
    "arrow": icons.icon_arrow(48),
}
CHECK_PARTIALS = [icons.icon_check_partial(80, p / 10.0)
                  for p in range(11)]


def _digit_image(digit):
    f = load_font(130, True)
    tmp = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    bb = d.textbbox((0, 0), str(digit), font=f)
    img = Image.new("RGBA", (bb[2] - bb[0] + 8, bb[3] - bb[1] + 8),
                    (0, 0, 0, 0))
    d2 = ImageDraw.Draw(img)
    d2.text((4 - bb[0], 4 - bb[1]), str(digit), font=f, fill=WHITE)
    return img


DIGITS = {n: _digit_image(n) for n in range(0, 11)}


def _title_image(text):
    """Render a title (possibly 2 lines) to a trimmed RGBA image."""
    tmp = Image.new("RGBA", (W, 400), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    lines = wrap(d, text, F_TITLE, layout.CONTENT_MAX_W)
    # measure
    heights = []
    for line in lines:
        s = " ".join(line)
        bb = d.textbbox((0, 0), s, font=F_TITLE)
        heights.append(bb[3] - bb[1])
    # Ink extents: line i's ink runs from y=i*80 to y=i*80+h_i, so the
    # image must be (n-1)*80 + last-line height tall. (An earlier
    # version used sum(heights)+(n-1)*(leading-font_size) and clipped
    # the second line's descenders.)
    total_h = (len(lines) - 1) * 80 + heights[-1]
    img = Image.new("RGBA", (W, total_h + 8), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(img)
    y = 0
    for line, h in zip(lines, heights):
        s = " ".join(line)
        bb = d2.textbbox((0, 0), s, font=F_TITLE)
        d2.text(((W - (bb[2] - bb[0])) // 2 - bb[0], y - bb[1]), s,
                font=F_TITLE, fill=WHITE)
        y += 80
    bbox = img.getbbox()
    return img.crop(bbox) if bbox else img


TITLE_IMGS = {}
for _b in SPEC_BEATS:
    for _p in _b.get("parts", []):
        if "title" in _p and _p["title"] not in TITLE_IMGS:
            TITLE_IMGS[_p["title"]] = _title_image(_p["title"])


# --- captions: current sentence only, bottom-anchored in the band ---
def _sentences(text):
    """Split speak text into sentences; return [(words, start_idx)]."""
    parts = re.split(r"(?<=[.?!])\s+", text.strip())
    out, idx = [], 0
    for s in parts:
        ws = s.split()
        if ws:
            out.append((ws, idx))
            idx += len(ws)
    return out


CAP_CACHE = {}


def caption_sentence(draw, bi, pi, p):
    key = (bi, pi)
    if key in CAP_CACHE:
        return CAP_CACHE[key]
    sents = _sentences(p["speak"])
    wrapped = []
    for ws, start in sents:
        lines = wrap(draw, " ".join(ws), F_CAP, layout.CAPTION_MAX_W)
        wrapped.append((lines, start))
    CAP_CACHE[key] = wrapped
    return wrapped


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
    wrapped = caption_sentence(draw, bi, pi, p)
    # current sentence: the one containing the last revealed word
    cur = 0
    for si, (lines, start) in enumerate(wrapped):
        nwords = sum(len(l) for l in lines)
        if start + nwords > max(0, revealed - 1):
            cur = si
            break
        cur = si
    lines, start = wrapped[cur]
    n_lines = len(lines)
    y = layout.subtitle_top(n_lines)
    lh = layout.CAPTION_LINE_H
    idx = start
    x0min, y0min, x1max, y1max = 10 ** 9, 10 ** 9, -1, -1
    for line in lines:
        total_w = sum(text_w(draw, w, F_CAP) + 10 for w in line) - 10
        x = (2 * layout.CAPTION_CX - total_w) // 2
        for w in line:
            if idx < revealed - 1:
                col = WHITE
            elif idx == revealed - 1:
                col = ACCENT
            else:
                col = FAINT
            bb = draw.textbbox((0, 0), w, font=F_CAP)
            draw.text((x, y), w, font=F_CAP, fill=col)
            x0min = min(x0min, x + bb[0])
            y0min = min(y0min, y + bb[1])
            x1max = max(x1max, x + bb[2])
            y1max = max(y1max, y + bb[3])
            x += text_w(draw, w, F_CAP) + 10
            idx += 1
        y += lh
    if x1max > 0:
        rec(x0min, y0min, x1max, y1max, "caption")


def draw_header(draw, bi, b, t):
    label = spec["format"].upper()
    draw_text_r(draw, label, F_CHIP, layout.SAFE_BOX[0], 180, ACCENT,
                "header label")
    if "n" in b:
        right = f"{b['n']} / {b['total']}"
        rw = text_w(draw, right, F_CHIP)
        draw_text_r(draw, right, F_CHIP, layout.SAFE_BOX[2] - rw, 180,
                    SOFT, "header counter")
    # progress track (graphic): x 80-640, y 238-248; fill + dot
    draw.rectangle([80, 238, 640, 248], fill=(40, 40, 56))
    frac = t / TOTAL
    draw.rectangle([80, 238, 80 + int(560 * frac), 248], fill=ACCENT)
    dx = 80 + int(560 * frac)
    draw.ellipse([dx - 8, 235, dx + 8, 251], fill=ACCENT)


def frame_for(fi):
    global BOXES
    BOXES = []
    t = fi / FPS
    img = frame_base(fi)
    draw = ImageDraw.Draw(img)
    bi, b = beat_at(t)
    sbeat = SPEC_BEATS[bi]
    kind = b["kind"]
    draw_header(draw, bi, b, t)

    if kind == "intro":
        p = b["parts"][0]
        lt = t - b["start"]
        icons.paste_icon(img, PHASE_ICONS["star"], 104, 294)
        if lt > 0.3:
            sub = sbeat["parts"][0]["subtitle"]
            slines = wrap(draw, sub, F_BODY, layout.CONTENT_MAX_W)
            draw_lines_centered_r(draw, slines, F_BODY, layout.CONTENT_CX,
                                  310, 50, SOFT, "subtitle")
        title = sbeat["parts"][0]["title"]
        timg = TITLE_IMGS[title]
        sc = icons.pop_scale(lt, 0.5)
        al = icons.fade_alpha(lt, 0.3)
        icons.paste_icon(img, timg, layout.CONTENT_CX, 430 + timg.height // 2,
                         scale=sc, alpha=al)
        rec(int(layout.CONTENT_CX - timg.width * sc / 2), 430,
            int(layout.CONTENT_CX + timg.width * sc / 2),
            int(430 + timg.height * sc), "title")
    elif kind == "outro":
        p = b["parts"][0]
        lt = t - b["start"]
        icons.paste_icon(img, PHASE_ICONS["arrow"], 104, 294)
        if lt > 0.3:
            sub = sbeat["parts"][0]["subtitle"]
            slines = wrap(draw, sub, F_BODY, layout.CONTENT_MAX_W)
            draw_lines_centered_r(draw, slines, F_BODY, layout.CONTENT_CX,
                                  310, 50, SOFT, "subtitle")
        title = sbeat["parts"][0]["title"]
        timg = TITLE_IMGS[title]
        sc = icons.pop_scale(lt, 0.5)
        al = icons.fade_alpha(lt, 0.3)
        icons.paste_icon(img, timg, layout.CONTENT_CX, 430 + timg.height // 2,
                         scale=sc, alpha=al)
        rec(int(layout.CONTENT_CX - timg.width * sc / 2), 430,
            int(layout.CONTENT_CX + timg.width * sc / 2),
            int(430 + timg.height * sc), "title")
    elif kind == "ask":
        is_riddle = spec["id"] == "riddle-round"
        icon = PHASE_ICONS["lightbulb"] if is_riddle else PHASE_ICONS["question"]
        icons.paste_icon(img, icon, 104, 294)
        chip = f"RIDDLE {b['n']}" if is_riddle else f"QUESTION {b['n']}"
        cw = text_w(draw, chip, F_CHIP)
        draw_text_r(draw, chip, F_CHIP, layout.CONTENT_CX - cw // 2, 280,
                    ACCENT, "chip")
        if is_riddle:
            # Wrap every visible clue first, then fit the whole stack
            # into the safe box (y 340 -> 830) by shrinking leading/gap.
            visible = []
            for pi, part in enumerate(sbeat["parts"]):
                tp = b["parts"][pi]
                if t >= tp["start"]:
                    visible.append(wrap(draw, part["display"], F_BODY,
                                        layout.CONTENT_MAX_W))
            n_lines = sum(len(ln) for ln in visible)
            lh, gap = fit_stack(n_lines, len(visible), 340, 830)
            y = 340
            for lines in visible:
                y = draw_lines_centered_r(draw, lines, F_BODY,
                                          layout.CONTENT_CX, y, lh,
                                          WHITE, "clue")
                y += gap
        else:
            lines = wrap(draw, sbeat["parts"][0]["display"], F_Q,
                         layout.CONTENT_MAX_W)
            draw_lines_centered_r(draw, lines, F_Q, layout.CONTENT_CX,
                                  360, 72, WHITE, "question")
    elif kind == "think":
        icons.paste_icon(img, PHASE_ICONS["clock"], 104, 294)
        prev = SPEC_BEATS[bi - 1]
        y = 330
        for part in prev["parts"]:
            lines = wrap(draw, part["display"], F_SMALL,
                         layout.CONTENT_MAX_W)
            y = draw_lines_centered_r(draw, lines, F_SMALL,
                                      layout.CONTENT_CX, y, 34, DIM,
                                      "recap")
            y += 10
        draw_text_r(draw, "THINK!", F_LABEL,
                    layout.CONTENT_CX - text_w(draw, "THINK!", F_LABEL) // 2,
                    680, ACCENT, "think label")
        remaining = b["end"] - t
        num = int(math.ceil(remaining - 1e-9))
        num = max(1, min(b["seconds"], num))
        dimg = DIGITS[num]
        sc = icons.pulse_scale(t - b["start"], amp=0.04, period=1.0)
        icons.paste_icon(img, dimg, layout.CONTENT_CX, 780, scale=sc)
        rec(int(layout.CONTENT_CX - dimg.width * sc / 2),
            int(780 - dimg.height * sc / 2),
            int(layout.CONTENT_CX + dimg.width * sc / 2),
            int(780 + dimg.height * sc / 2), "countdown")
    elif kind == "answer":
        p = b["parts"][0]
        lt = t - b["start"]
        # checkmark tick-draw above the banner
        prog = icons.tick_progress(lt, 0.3)
        step = int(round(prog * 10))
        icons.paste_icon(img, CHECK_PARTIALS[step], layout.CONTENT_CX, 350)
        # answer banner, pop-in about its centre (300, 455)
        sc = icons.pop_scale(lt, 0.4)
        hw, hh = int(220 * sc), int(55 * sc)
        draw.rounded_rectangle([layout.CONTENT_CX - hw, 455 - hh,
                                layout.CONTENT_CX + hw, 455 + hh],
                               radius=max(4, int(24 * sc)), fill=GREEN)
        if lt > 0.05:
            lab = "ANSWER"
            draw_text_r(draw, lab, F_LABEL,
                        layout.CONTENT_CX - text_w(draw, lab, F_LABEL) // 2,
                        440, WHITE, "answer label")
        ans = sbeat["parts"][0]["answer"]
        alines = wrap(draw, ans, F_ANS, layout.CONTENT_MAX_W)
        draw_lines_centered_r(draw, alines, F_ANS, layout.CONTENT_CX,
                              540, 64, WHITE, "answer")
        # NOTE: no static explain text — the spoken explanation is shown
        # word-by-word in the caption band (see draw_caption).

    # Captions: only where the speech is NOT already on screen as large
    # text. Ask beats show the question/clues; think beats have no speech.
    if kind in ("intro", "answer", "outro"):
        draw_caption(draw, t)
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
    t0 = time.time()
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    violations = []
    for fi in range(TOTAL_FRAMES):
        img = frame_for(fi)
        passed, bad = layout.check_boxes(BOXES)
        if not passed:
            violations.append({"frame": fi, "t": round(fi / FPS, 3),
                               "violations": bad})
        proc.stdin.write(img.tobytes())
    _, err = proc.communicate()
    dt = time.time() - t0
    check = {"video": os.path.basename(out_path),
             "frames_checked": TOTAL_FRAMES,
             "frames_failed": len(violations),
             "passed": len(violations) == 0,
             "violations": violations[:20]}
    check_path = out_path.replace(".mp4", "-safezone.json")
    with open(check_path, "w") as f:
        json.dump(check, f, indent=2)
    print(f"frames_written={TOTAL_FRAMES} expected={TOTAL_FRAMES} "
          f"returncode={proc.returncode} render_time={dt:.1f}s", flush=True)
    print(f"safezone: checked {TOTAL_FRAMES} frames, "
          f"{len(violations)} failed -> "
          f"{'PASS' if not violations else 'FAIL'}", flush=True)
    if proc.returncode != 0:
        print(err.decode(errors="replace"), file=sys.stderr)
        sys.exit(1)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)
    if violations:
        print("SAFEZONE FAIL — see", check_path, flush=True)
        sys.exit(2)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
