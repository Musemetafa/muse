"""Factory Test 2 — code-computed motion, deterministic render.

Reads script2.json (3 scenes x 2.0 s, 30 fps, 720x1280). Each scene has a
code-computed motion, evaluated per frame from the frame index only:
  slide  - title slides in from the left (ease-out cubic, first 0.5 s),
           a dot travels left -> right across the frame.
  grow   - a filled circle grows from the centre; a bar sweeps top -> bottom.
  bounce - a ball bounces (two parabolas); a progress bar fills left -> right.

Frames are generated with Pillow/numpy and piped as raw RGB to ffmpeg
(libx264, same settings as Test 1). No randomness, no wall-clock input:
same input must give byte-identical output.
"""
import json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))  # persistent workspace dir, not /tmp (/tmp was wiped mid-run)
OUT = os.path.join(BASE, "output.mp4")
with open(os.path.join(BASE, "script2.json")) as f:
    spec = json.load(f)

W = spec["width"]; H = spec["height"]; FPS = spec["fps"]

def load_font(size, bold=False):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

title_font = load_font(64, True)
body_font = load_font(36, False)
ACCENT = (255, 190, 60)

def gradient_bg(scene):
    r0, g0, b0 = scene["bg"]
    r1, g1, b1 = min(255, r0 + 60), min(255, g0 + 60), min(255, b0 + 60)
    t = np.linspace(0, 1, H, dtype=np.float64)[:, None, None]
    c0 = np.array([r0, g0, b0], dtype=np.float64)
    c1 = np.array([r1, g1, b1], dtype=np.float64)
    arr = (c0 + (c1 - c0) * t).astype(np.uint8)
    arr = np.repeat(arr, W, axis=1)
    return Image.fromarray(arr, "RGB")

def text_w(draw, s, font):
    bb = draw.textbbox((0, 0), s, font=font)
    return bb[2] - bb[0]

def draw_static(draw, scene, i):
    title = scene["title"]
    tw = text_w(draw, title, title_font)
    body = scene["body"]
    bw = text_w(draw, body, body_font)
    return tw, bw

def frame_for(scene_idx, scene, fi, nframes):
    """fi: frame index inside the scene, 0..nframes-1. t in [0,1)."""
    t = fi / nframes
    img = BASE_IMG[scene_idx].copy()
    draw = ImageDraw.Draw(img)
    title = scene["title"]
    body = scene["body"]
    tw = text_w(draw, title, title_font)
    bw = text_w(draw, body, body_font)
    cx = (W - tw) // 2
    motion = scene["motion"]
    if motion == "slide":
        # ease-out cubic over first half of the scene
        p = min(1.0, t / 0.5)
        e = 1 - (1 - p) ** 3
        x = int(-tw + (cx + tw) * e)
        draw.text((x, 420), title, font=title_font, fill=(255, 255, 255))
        # travelling dot
        dx = int(60 + (W - 120) * t)
        draw.ellipse([dx - 28, 1020 - 28, dx + 28, 1020 + 28], fill=ACCENT)
        draw.rectangle([60, 1080, 60 + int((W - 120) * t), 1092], fill=ACCENT)
    elif motion == "grow":
        draw.text((cx, 420), title, font=title_font, fill=(255, 255, 255))
        r = int(30 + 300 * t)
        draw.ellipse([W // 2 - r, 640 - r, W // 2 + r, 640 + r], fill=ACCENT)
        by = int(300 + 700 * t)
        draw.rectangle([80, by, W - 80, by + 14], fill=(255, 255, 255))
    elif motion == "bounce":
        draw.text((cx, 420), title, font=title_font, fill=(255, 255, 255))
        # two bounces per scene: |sin| parabola, floor at y=1000
        y = int(1000 - 420 * abs(math.sin(math.pi * 2 * t)))
        draw.ellipse([W // 2 - 40, y - 40, W // 2 + 40, y + 40], fill=ACCENT)
        draw.rectangle([60, 1080, 60 + int((W - 120) * t), 1092], fill=ACCENT)
    else:
        raise ValueError(f"unknown motion {motion!r}")
    draw.text(((W - bw) // 2, 560), body, font=body_font, fill=(230, 230, 230))
    draw.rectangle([(0, H - 90), (W, H)], fill=(0, 0, 0))
    label = f"scene {scene_idx+1} / {len(spec['scenes'])}  -  {scene['duration']}s  -  {motion}"
    lw = text_w(draw, label, body_font)
    draw.text(((W - lw) // 2, H - 70), label, font=body_font, fill=(255, 255, 255))
    return img

BASE_IMG = [gradient_bg(s) for s in spec["scenes"]]
total = sum(s["duration"] for s in spec["scenes"])
total_frames = int(round(total * FPS))

cmd = ["ffmpeg", "-y",
       "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "pipe:0",
       "-f", "lavfi", "-i", f"sine=frequency=440:duration={total}",
       "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
       "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", OUT]
proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
frame_no = 0
for i, scene in enumerate(spec["scenes"]):
    nframes = int(round(scene["duration"] * FPS))
    for fi in range(nframes):
        img = frame_for(i, scene, fi, nframes)
        proc.stdin.write(img.tobytes())
        frame_no += 1
_, err = proc.communicate()  # communicate() closes stdin itself
print(f"frames_written={frame_no} expected={total_frames} returncode={proc.returncode}")
if proc.returncode != 0:
    print(err.decode(errors="replace"), file=sys.stderr)
    sys.exit(1)
print("wrote", OUT)
