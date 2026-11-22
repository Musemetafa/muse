import json, os, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

BASE = "/tmp/factory-test-1"
with open(os.path.join(BASE, "script.json")) as f:
    spec = json.load(f)

W = spec["width"]; H = spec["height"]

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

def make_scene(i, scene):
    # vertical gradient background
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    r0,g0,b0 = scene["bg"]
    r1,g1,b1 = min(255,r0+60), min(255,g0+60), min(255,b0+60)
    for y in range(H):
        t = y / H
        draw.line([(0,y),(W,y)], fill=(int(r0+(r1-r0)*t), int(g0+(g1-g0)*t), int(b0+(b1-b0)*t)))
    # title centered
    title = scene["title"]
    tb = draw.textbbox((0,0), title, font=title_font)
    tw = tb[2]-tb[0]
    draw.text(((W-tw)//2, 420), title, font=title_font, fill=(255,255,255))
    # body wrapped centered
    lines = textwrap.wrap(scene["body"], width=22)
    y = 560
    for line in lines:
        bb = draw.textbbox((0,0), line, font=body_font)
        lw = bb[2]-bb[0]
        draw.text(((W-lw)//2, y), line, font=body_font, fill=(230,230,230))
        y += 55
    # scene number bar at bottom
    draw.rectangle([(0, H-90), (W, H)], fill=(0,0,0))
    label = f"scene {i+1} / {len(spec['scenes'])}  -  {scene['duration']}s"
    lb = draw.textbbox((0,0), label, font=body_font)
    lw = lb[2]-lb[0]
    draw.text(((W-lw)//2, H-70), label, font=body_font, fill=(255,255,255))
    path = os.path.join(BASE, f"scene_{i}.png")
    img.save(path)
    return path

paths = []
for i, scene in enumerate(spec["scenes"]):
    paths.append(make_scene(i, scene))

total = sum(s["duration"] for s in spec["scenes"])
# Fix for concat-with-stills failure: make a real video segment per scene
# with -loop 1 -t duration, then concat the segments (video files, not images).
seg_paths = []
for i, p in enumerate(paths):
    seg = os.path.join(BASE, f"seg_{i}.mp4")
    c1 = ["ffmpeg","-y","-loop","1","-t",str(spec["scenes"][i]["duration"]),"-i",p,
          "-vf","scale=720:1280,format=yuv420p,fps=30",
          "-c:v","libx264","-preset","veryfast","-crf","23","-r","30","-an", seg]
    r1 = subprocess.run(c1, capture_output=True, text=True)
    if r1.returncode != 0:
        print(r1.stderr, file=sys.stderr)
        sys.exit(1)
    seg_paths.append(seg)

with open(os.path.join(BASE, "segments.txt"), "w") as f:
    for s in seg_paths:
        f.write(f"file '{s}'\n")

out = os.path.join(BASE, "output.mp4")
cmd = ["ffmpeg","-y","-f","concat","-safe","0","-i",os.path.join(BASE,"segments.txt"),
       "-f","lavfi","-i",f"sine=frequency=440:duration={total}",
       "-vf","scale=720:1280,format=yuv420p,fps=30",
       "-c:v","libx264","-preset","veryfast","-crf","23",
       "-c:a","aac","-b:a","128k","-shortest","-movflags","+faststart", out]
print(" ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)
print(res.stdout)
print(res.stderr, file=sys.stderr)
print("returncode", res.returncode)
print("total_duration", total)
if res.returncode != 0:
    sys.exit(1)
print("wrote", out)
