"""Smoke test for render2.py: render a handful of frames across all
beat kinds and save a contact sheet, so the v2 layout can be eyeballed
before committing to full renders. Also runs the safe-zone checker on
those frames and prints any violation.

Usage: python3 factory/smoke2.py <script.json> <timings.json>
       <words.json> <out-sheet.jpg>
"""
import os
import sys

SHEET = sys.argv[4]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = ["render2.py", sys.argv[1], sys.argv[2], sys.argv[3], "x.mp4"]
import render2
import layout
from PIL import Image

# sample times: intro, ask, think, answer, ask, think, answer, outro
times = [1.0, 10.0, 15.0, 21.0, 40.0, 44.0, 49.0, 85.0]
frames = []
all_bad = []
for t in times:
    fi = int(t * render2.FPS)
    img = render2.frame_for(fi)
    passed, bad = layout.check_boxes(render2.BOXES)
    print(f"t={t:5.1f}s frame={fi:4d} boxes={len(render2.BOXES):2d} "
          f"checker={'PASS' if passed else 'FAIL ' + str(bad)}")
    if not passed:
        all_bad.append((t, bad))
    frames.append(img)

cols, rows = 4, 2
tw, th = 360, 640
sheet = Image.new("RGB", (cols * tw, rows * th), (10, 10, 20))
for i, fr in enumerate(frames):
    sheet.paste(fr.resize((tw, th)), ((i % cols) * tw, (i // cols) * th))
out = SHEET
sheet.save(out, quality=88)
print("sheet:", out, "checker violations:", len(all_bad))
sys.exit(1 if all_bad else 0)
