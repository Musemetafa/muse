"""Test for factory/layout.py — the checker must catch the real v1 defect.

v1 layout (measured from prototype-1/render.py):
  - karaoke captions at y = H - 210 = 1070, wrapped at 640 px wide and
    centred -> box roughly (40, 1070, 680, 1112)
  - progress bar at the very bottom edge -> (0, 1246, 720, 1256)
  - header label at (40, 36) -> top of frame
All three must FAIL. The corrected v2 positions must PASS.
Run: python3 factory/test_layout.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import layout

FAIL_CASES = [
    # (box, label, edges that must appear)
    ((40, 1070, 680, 1112, "v1 caption line 1"),
     {"bottom", "right", "right-column"}),
    ((0, 1246, 720, 1256, "v1 progress bar"),
     {"bottom", "left", "right", "right-column"}),
    ((40, 36, 220, 64, "v1 header label"),
     {"top", "left"}),
    ((40, 300, 680, 372, "v1 question text, 620 wide centred"),
     {"right", "left"}),
    # boundary probe: one pixel past the right column, below y=560
    ((100, 700, 521, 742, "one pixel into the action column"),
     {"right-column"}),
]

PASS_CASES = [
    (80, 180, 260, 208, "v2 header label"),
    (90, 746, 510, 788, "v2 caption line (bottom-anchored at 830)"),
    (80, 746, 520, 788, "v2 caption line, full band width"),
    (140, 540, 460, 604, "v2 answer text, centred on x=300"),
    (80, 790, 520, 806, "v2 think bar, x1 exactly 520"),
    (80, 160, 640, 560, "full-width text ending exactly at y=560"),
    (80, 400, 520, 510, "v2 answer banner"),
]

# A tall text block that crosses y=560 at full safe width puts its lower
# part behind the action buttons — it must FAIL even though its top is
# inside the safe box. (This is why the safe box rectangle itself is not
# a valid text box: the box (80,160,640,840) fails on right-column.)
TALL_FAIL = (80, 300, 640, 700, "tall text crossing into the column")


def main():
    ok = True
    for box, must in FAIL_CASES:
        passed, violations = layout.check_boxes([box])
        edges = set(violations[0]["edges"]) if violations else set()
        if passed or not must <= edges:
            print(f"FAIL: {box[4]} should fail with {sorted(must)}, "
                  f"got passed={passed} edges={sorted(edges)}")
            ok = False
        else:
            print(f"ok:   {box[4]} correctly FAILS ({sorted(edges)})")
    passed, violations = layout.check_boxes(PASS_CASES)
    if not passed:
        print(f"FAIL: v2 positions should all pass, got {violations}")
        ok = False
    else:
        print(f"ok:   all {len(PASS_CASES)} v2 positions PASS")
    passed, violations = layout.check_boxes([TALL_FAIL])
    if passed or "right-column" not in [e for v in violations
                                         for e in v["edges"]]:
        print(f"FAIL: tall crossing text should fail on right-column, "
              f"got passed={passed} {violations}")
        ok = False
    else:
        print("ok:   tall text crossing into the column correctly FAILS")
    # zone sanity
    assert layout.SAFE_BOX == (80, 160, 640, 840), layout.SAFE_BOX
    assert layout.subtitle_top(2) == 830 - 2 * 42
    assert layout.inside_safe(80, 160, 640, 560)
    assert not layout.inside_safe(80, 160, 640, 840)  # right-column rule
    assert not layout.inside_safe(40, 1070, 680, 1112)
    print("ok:   zone constants sane")
    print("CHECKER TEST:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
