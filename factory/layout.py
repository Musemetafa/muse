"""TikTok safe-zone layout system — a permanent factory capability.

Every video the factory builds lays its text out inside the safe box and
verifies it with the automated checker in this module. A video whose text
leaves the safe box FAILS verification, exactly like a black or frozen
frame. This is factory law (see factory/DESIGN_RULES.md), not a per-video
fix: it was built because the v1 prototypes put their karaoke captions
at y=1070 of 1280, where TikTok's own interface covers them.

Numbers — source: TikTok's own published In-Feed ads template
(1080x1920). The factory designs to the STRICTER ads template, not to
the looser organic-post measurements, because the ads template
guarantees the text is visible in every placement (organic feed,
promoted, Spark Ads). The organic measurements are recorded below for
reference only.

    1080x1920 template:  top 240 px, bottom 660 px, sides 120 px,
                          right action column 300 px wide from y=840 down.
    720x1280 (scale 2/3): top 160 px, bottom 440 px, sides 80 px,
                          right action column 200 px wide from y=560 down.
    Safe box on 720x1280: x 80-640, y 160-840.

Organic-post measurements (measured in the app, TikTok publishes none):
on 1080x1920 roughly top 200, bottom 334, right 140; on 720x1280
roughly top 133, bottom 223, right 93. Designing to the ads template
covers these with margin.

Layout consequence of the right column: below y=560 the action buttons
sit on the right, so text there must end at x<=520. The factory
therefore centres all body content on x=300 with a max width of 440 px
(x 80-520) instead of centring on the frame middle. Text above y=560
may use the full safe width (x 80-640). The header (label, counter,
progress track) lives above y=560 and uses the full safe width.
"""

W, H = 720, 1280

# --- Safe box (TikTok In-Feed ads template, scaled to 720x1280) ---
TOP_MARGIN = 160
BOTTOM_MARGIN = 440
SIDE_MARGIN = 80
SAFE_BOX = (SIDE_MARGIN, TOP_MARGIN, W - SIDE_MARGIN, H - BOTTOM_MARGIN)
# SAFE_BOX == (80, 160, 640, 840)

# Right action column: below this y, keep text x <= this value.
RIGHT_COLUMN_Y = 560
RIGHT_COLUMN_X = 520  # 720 - 200 px column

# Organic-post measurements (reference only — the factory does NOT
# design to these; see module docstring).
ORGANIC = {"top": 133, "bottom": 223, "right": 93, "left": 57}

# --- Named zones (all inside the safe box) ---
# Header: label + counter + progress track. Above y=560, full safe width.
HEADER_ZONE = (80, 170, 640, 260)
# Hook: title cards, upper middle.
HOOK_ZONE = (80, 200, 520, 470)
# Body: question / clue / answer text. Centred on x=300, max 440 wide.
BODY_ZONE = (80, 280, 520, 700)
CONTENT_CX = 300
CONTENT_MAX_W = 440
# Subtitle band: captions live here, bottom-anchored at y=830, never below.
SUBTITLE_BAND = (80, 700, 520, 830)
CAPTION_BOTTOM = 830
CAPTION_CX = 300
CAPTION_MAX_W = 440
CAPTION_LINE_H = 42
# CTA: final card / call to action — middle of the frame, never the
# bottom quarter.
CTA_ZONE = (80, 380, 520, 700)


def _edge_violations(x0, y0, x1, y1):
    """Which safe-box edges a box crosses. Empty list means inside."""
    v = []
    if x0 < SAFE_BOX[0]:
        v.append("left")
    if x1 > SAFE_BOX[2]:
        v.append("right")
    if y0 < SAFE_BOX[1]:
        v.append("top")
    if y1 > SAFE_BOX[3]:
        v.append("bottom")
    # Right action column: any part of the box below y=560 must end
    # at x <= 520.
    if y1 > RIGHT_COLUMN_Y and x1 > RIGHT_COLUMN_X:
        v.append("right-column")
    return v


def check_boxes(boxes):
    """Check text bounding boxes against the safe box.

    boxes: iterable of (x0, y0, x1, y1) or (x0, y0, x1, y1, label).
    Returns (passed: bool, violations: list[dict]) where each violation
    is {"label": str, "box": (x0, y0, x1, y1), "edges": [...]}.
    A box exactly on a boundary passes (edges are inclusive).
    """
    violations = []
    for b in boxes:
        if len(b) == 5:
            x0, y0, x1, y1, label = b
        else:
            x0, y0, x1, y1 = b
            label = f"box({x0},{y0},{x1},{y1})"
        edges = _edge_violations(x0, y0, x1, y1)
        if edges:
            violations.append({"label": label, "box": (x0, y0, x1, y1),
                               "edges": edges})
    return (len(violations) == 0), violations


def check_frame(boxes, frame_no=None):
    """Check one frame's text boxes. Returns a small report dict."""
    passed, violations = check_boxes(boxes)
    return {"frame": frame_no, "n_boxes": len(boxes),
            "passed": passed, "violations": violations}


def inside_safe(x0, y0, x1, y1):
    """True if a box lies entirely inside the safe box."""
    return not _edge_violations(x0, y0, x1, y1)


def subtitle_top(n_lines, line_h=CAPTION_LINE_H):
    """Top y of a caption block with n_lines lines, bottom-anchored at
    CAPTION_BOTTOM (830)."""
    return CAPTION_BOTTOM - n_lines * line_h
