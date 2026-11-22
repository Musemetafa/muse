"""Original icon + micro-animation library — a permanent factory capability.

Every icon is drawn in code with Pillow vector shapes (circles, rounded
rectangles, polygons, lines). No copied artwork, no downloaded icons, no
emoji rendered as icons. Icons are therefore original to the factory and
free of any licence or likeness question.

Each icon function returns an RGBA PIL Image of the requested size, the
icon centred with a small padding so strokes never clip. Colour and line
weight are parameters, so the same icon serves every format.

Micro-animation primitives are pure functions of frame time t
(deterministic: same t gives the same picture, as the renderer
requires). They compose: e.g. an answer banner pops in while its
checkmark draws itself.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

ACCENT = (255, 190, 60)
GREEN = (46, 160, 90)
WHITE = (255, 255, 255)

_FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def _font(size):
    if os.path.exists(_FONT):
        return ImageFont.truetype(_FONT, size)
    return ImageFont.load_default()


def ease_out(p):
    p = min(1.0, max(0.0, p))
    return 1 - (1 - p) ** 3


# ---------------------------------------------------------------- icons

def _canvas(size):
    return Image.new("RGBA", (size, size), (0, 0, 0, 0))


def _weight(size, weight):
    return weight if weight else max(3, size // 14)


def icon_question(size, color=ACCENT, weight=None):
    """Question mark inside a circle."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    r = size * 0.36
    d.ellipse([size / 2 - r, size / 2 - r, size / 2 + r, size / 2 + r],
              outline=color, width=w)
    f = _font(int(size * 0.52))
    bb = d.textbbox((0, 0), "?", font=f)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((size / 2 - tw / 2 - bb[0], size / 2 - th / 2 - bb[1] - size * 0.02),
           "?", font=f, fill=color)
    return img


def _check_points(size):
    """Checkmark polyline points (normalised -> pixels)."""
    return [(size * 0.26, size * 0.54), (size * 0.44, size * 0.72),
            (size * 0.76, size * 0.30)]


def _draw_check_partial(d, size, progress, color, weight):
    """Draw a checkmark stroke up to `progress` (0..1) of its length."""
    pts = _check_points(size)
    (ax, ay), (bx, by), (cx, cy) = pts
    l1 = math.hypot(bx - ax, by - ay)
    l2 = math.hypot(cx - bx, cy - by)
    total = (l1 + l2) * max(0.0, min(1.0, progress))
    if total <= 0:
        return
    if total <= l1:
        f = total / l1
        d.line([(ax, ay), (ax + (bx - ax) * f, ay + (by - ay) * f)],
               fill=color, width=weight, joint="curve")
    else:
        d.line([(ax, ay), (bx, by)], fill=color, width=weight,
               joint="curve")
        f = (total - l1) / l2
        d.line([(bx, by), (bx + (cx - bx) * f, by + (cy - by) * f)],
               fill=color, width=weight, joint="curve")


def icon_check(size, color=GREEN, weight=None):
    """Checkmark inside a circle (fully drawn)."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    r = size * 0.36
    d.ellipse([size / 2 - r, size / 2 - r, size / 2 + r, size / 2 + r],
              outline=color, width=w)
    _draw_check_partial(d, size, 1.0, color, w)
    return img


def icon_check_partial(size, progress, color=GREEN, weight=None):
    """Checkmark circle with the tick drawn to `progress` (0..1)."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    r = size * 0.36
    d.ellipse([size / 2 - r, size / 2 - r, size / 2 + r, size / 2 + r],
              outline=color, width=w)
    _draw_check_partial(d, size, progress, color, w)
    return img


def icon_cross(size, color=(220, 80, 80), weight=None):
    """Cross (X) inside a circle."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    r = size * 0.36
    d.ellipse([size / 2 - r, size / 2 - r, size / 2 + r, size / 2 + r],
              outline=color, width=w)
    a, b = size * 0.36, size * 0.64
    d.line([(a, a), (b, b)], fill=color, width=w, joint="curve")
    d.line([(b, a), (a, b)], fill=color, width=w, joint="curve")
    return img


def icon_lightbulb(size, color=ACCENT, weight=None):
    """Lightbulb: circle + base + three rays."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    cx, cy, r = size / 2, size * 0.40, size * 0.24
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=w)
    # base: two short lines under the bulb
    d.line([(cx - r * 0.55, cy + r * 0.95), (cx + r * 0.55, cy + r * 0.95)],
           fill=color, width=w)
    d.line([(cx - r * 0.45, cy + r * 1.15), (cx + r * 0.45, cy + r * 1.15)],
           fill=color, width=w)
    # rays above the bulb
    for ang in (-45, 0, 45):
        a = math.radians(ang - 90)
        x0 = cx + math.cos(a) * (r + size * 0.04)
        y0 = cy + math.sin(a) * (r + size * 0.04)
        x1 = cx + math.cos(a) * (r + size * 0.13)
        y1 = cy + math.sin(a) * (r + size * 0.13)
        d.line([(x0, y0), (x1, y1)], fill=color, width=w)
    return img


def icon_clock(size, color=ACCENT, weight=None):
    """Clock: circle + two hands (12 o'clock and 4 o'clock)."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    cx, cy, r = size / 2, size / 2, size * 0.36
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=w)
    d.line([(cx, cy), (cx, cy - r * 0.75)], fill=color, width=w)
    d.line([(cx, cy), (cx + r * 0.55, cy + r * 0.45)], fill=color, width=w)
    d.ellipse([cx - w, cy - w, cx + w, cy + w], fill=color)
    return img


def icon_brain(size, color=ACCENT, weight=None):
    """Stylised brain: a bumpy closed outline (radius modulated by
    sine harmonics, so it reads as an organic lobe, not a circle)
    with a centre squiggle and a small stem."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    cx, cy, R = size * 0.50, size * 0.44, size * 0.30
    pts = []
    for i in range(48):
        th = 2 * math.pi * i / 48
        r = R * (1 + 0.09 * math.sin(3 * th + 0.7)
                 + 0.05 * math.sin(5 * th + 2.0))
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th) * 0.92))
    d.line(pts + [pts[0]], fill=color, width=w, joint="curve")
    d.line([(size * 0.43, size * 0.34), (size * 0.51, size * 0.42),
            (size * 0.43, size * 0.50), (size * 0.51, size * 0.58)],
           fill=color, width=max(2, w - 1), joint="curve")
    d.line([(size * 0.45, size * 0.72), (size * 0.50, size * 0.82),
            (size * 0.55, size * 0.72)], fill=color, width=max(2, w - 1),
           joint="curve")
    return img




def icon_star(size, color=ACCENT, weight=None):
    """Five-point star (filled)."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    cx, cy = size / 2, size / 2
    ro, ri = size * 0.44, size * 0.44 * 0.382
    pts = []
    for i in range(10):
        r = ro if i % 2 == 0 else ri
        a = math.radians(-90 + i * 36)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=color)
    return img


def icon_hourglass(size, color=ACCENT, weight=None):
    """Hourglass: two triangles meeting at the centre + sand."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    w = _weight(size, weight)
    cx = size / 2
    d.polygon([(size * 0.24, size * 0.18), (size * 0.76, size * 0.18),
               (cx, size * 0.50)], outline=color, width=w)
    d.polygon([(size * 0.24, size * 0.82), (size * 0.76, size * 0.82),
               (cx, size * 0.50)], outline=color, width=w)
    d.line([(cx, size * 0.50), (cx, size * 0.62)], fill=color, width=w)
    for (fx, fy, fr) in [(0.50, 0.68, 0.035), (0.44, 0.74, 0.028),
                         (0.56, 0.74, 0.028)]:
        d.ellipse([(fx - fr) * size, (fy - fr) * size,
                   (fx + fr) * size, (fy + fr) * size], fill=color)
    return img


def icon_arrow(size, color=ACCENT, weight=None):
    """Bold right arrow (filled)."""
    img = _canvas(size)
    d = ImageDraw.Draw(img)
    s = size
    d.polygon([(0.14 * s, 0.43 * s), (0.58 * s, 0.43 * s),
               (0.58 * s, 0.26 * s), (0.88 * s, 0.50 * s),
               (0.58 * s, 0.74 * s), (0.58 * s, 0.57 * s),
               (0.14 * s, 0.57 * s)], fill=color)
    return img


ICONS = {
    "question": icon_question,
    "check": icon_check,
    "cross": icon_cross,
    "lightbulb": icon_lightbulb,
    "clock": icon_clock,
    "brain": icon_brain,
    "star": icon_star,
    "hourglass": icon_hourglass,
    "arrow": icon_arrow,
}


# ------------------------------------------------- micro-animation primitives
# All are pure functions of t (seconds since the element started).

def pop_scale(t, dur=0.4):
    """Scale 0.8 -> 1.0 with ease-out over `dur` seconds."""
    return 0.8 + 0.2 * ease_out(t / dur)


def tick_progress(t, dur=0.3):
    """Checkmark draw progress 0 -> 1 over `dur` seconds."""
    return min(1.0, max(0.0, t / dur))


def slide_offset(t, distance, dur=0.4):
    """Horizontal offset: starts at -distance, eases to 0."""
    return -distance * (1 - ease_out(t / dur))


def pulse_scale(t, amp=0.04, period=1.0):
    """Gentle scale loop 1-amp .. 1+amp (e.g. countdown numbers)."""
    return 1.0 + amp * math.sin(2 * math.pi * t / period)


def fade_alpha(t, dur=0.25):
    """Opacity 0 -> 255 over `dur` seconds."""
    return int(255 * min(1.0, max(0.0, t / dur)))


def paste_icon(base, icon, cx, cy, scale=1.0, alpha=255):
    """Paste an RGBA icon centred at (cx, cy), scaled and faded.

    `base` is an RGB image (a video frame). Pure function of its inputs
    apart from the paste itself.
    """
    w, h = icon.size
    nw, nh = max(1, int(round(w * scale))), max(1, int(round(h * scale)))
    ic = icon.resize((nw, nh), Image.LANCZOS) if scale != 1.0 else icon
    if alpha < 255:
        ic = ic.copy()
        a = ic.split()[3].point(lambda v: v * alpha // 255)
        ic.putalpha(a)
    base.paste(ic, (int(cx - nw / 2), int(cy - nh / 2)), ic)


# ---------------------------------------------------------------- catalog

def build_catalog(path):
    """Render a contact sheet of every icon + animation frames."""
    import numpy as np
    W, H = 720, 1420
    top = np.linspace(0, 1, H, dtype=np.float64)[:, None, None]
    c0 = np.array([28, 36, 72], dtype=np.float64)
    c1 = np.array([64, 52, 118], dtype=np.float64)
    arr = (c0 + (c1 - c0) * top).astype(np.uint8)
    arr = np.repeat(arr, W, axis=1)
    img = Image.fromarray(arr, "RGB")
    d = ImageDraw.Draw(img)
    f_title = _font(40)
    f_lab = _font(24)
    f_small = _font(20)
    d.text((36, 24), "FACTORY ICONS", font=f_title, fill=WHITE)
    d.text((36, 80), "Drawn in code — original Pillow vector shapes.",
           font=f_small, fill=(200, 200, 215))
    d.text((36, 108), "No copied artwork, no downloads, no emoji.",
           font=f_small, fill=(200, 200, 215))

    # 3x3 icon grid
    cell = 190
    y0 = 150
    for i, name in enumerate(ICONS):
        cx = 120 + (i % 3) * 240
        cy = y0 + (i // 3) * cell + 70
        icon = ICONS[name](140)
        paste_icon(img, icon, cx, cy)
        d.text((cx - 70, cy + 84), name, font=f_lab, fill=WHITE)

    # animation strip: 4 rows x 3 frames
    y0 = y0 + 3 * cell + 40
    d.text((36, y0), "MICRO-ANIMATION", font=f_title, fill=WHITE)
    rows = [
        ("pop-in  t=0 / 0.2 / 0.4 s",
         [("check", lambda t: pop_scale(t))]),
        ("tick-draw  p=0 / 0.5 / 1.0",
         [("check", None)]),
        ("pulse  t=0 / 0.25 / 0.5 s",
         [("clock", lambda t: pulse_scale(t))]),
        ("slide-in  t=0 / 0.2 / 0.4 s",
         [("arrow", None)]),
    ]
    ts = [0.0, 0.2, 0.4]
    for ri, (label, _) in enumerate(rows):
        ry = y0 + 70 + ri * 130
        d.text((36, ry - 8), label, font=f_lab, fill=(225, 225, 235))
        for ci, t in enumerate(ts):
            cx = 300 + ci * 150
            cy = ry + 62
            if ri == 0:  # pop-in
                paste_icon(img, icon_check(110), cx, cy,
                           scale=pop_scale(t))
            elif ri == 1:  # tick-draw
                p = [0.0, 0.5, 1.0][ci]
                paste_icon(img, icon_check_partial(110, p), cx, cy)
            elif ri == 2:  # pulse
                paste_icon(img, icon_clock(110), cx, cy,
                           scale=pulse_scale(t))
            else:  # slide-in
                off = slide_offset(t, 110)
                paste_icon(img, icon_arrow(110), cx + off, cy)
    img.save(path, quality=90)
    return path


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "icons-catalog.jpg"
    print("wrote", build_catalog(out))
