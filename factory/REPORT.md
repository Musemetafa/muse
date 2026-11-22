# Factory capabilities: safe-zone layout + icon/animation library — REPORT

Date: 2026-11-22. This is the proof that Mohamed's correction became factory
law, not a patch to two videos: the TikTok safe zone and the icon/animation
system are now permanent parts of how the factory builds every video. The two
v2 prototypes are the first proof, not the goal.

## What was built

| File | What it is |
|---|---|
| `factory/layout.py` | Safe-zone constants, named zones, automated checker (`check_boxes`, `check_frame`, `inside_safe`, `subtitle_top`) |
| `factory/test_layout.py` | Checker test: v1 defect cases FAIL, v2 positions PASS |
| `factory/icons.py` | 9 original code-drawn icons + 5 micro-animation primitives (all pure functions of `t`) |
| `factory/icons-catalog.jpg` | Contact sheet of every icon + animation frames — viewed, icons read clearly at small size |
| `factory/DESIGN_RULES.md` | The two rules as factory law, with numbers and reasons |
| `factory/render2.py` | v2 renderer: imports layout + icons; runs the safe-zone checker on **every** frame's recorded text boxes; a violation fails the render (exit 2) |
| `factory/smoke2.py` | Smoke test: renders sample frames across all beat kinds, runs the checker, saves a contact sheet |

`factory/render.py` (v1) is untouched. `render2.py` has the same CLI as v1
(script, timings, words, out) and reuses the existing narration WAVs — no
re-synthesis (voice is still provisional af_heart).

## Safe-zone numbers and source

Source: TikTok's own published In-Feed ads template (1080×1920): keep
text/faces 240 px from the top, 660 px from the bottom, 120 px from each
side, plus a 300 px right column from y=840 down. Scaled to our 720×1280
canvas (×2/3): **top 160, bottom 440, sides 80, right column 200 px from
y=560 down. Safe box: x 80–640, y 160–840.**

The looser organic-post measurements (top ~133, bottom ~223, right ~93 on
720×1280) are recorded in a comment in `layout.py`, with the reason the
factory designs to the stricter ads template: it guarantees visibility in
every placement, not just organic feed.

Named zones: HOOK_ZONE (y ~200–470), SUBTITLE_BAND (y ~667–840, captions
bottom-anchored at 830, never below 840), BODY_ZONE (question/answer text,
centred in the safe box), CTA_ZONE (middle of the frame, never the bottom
quarter), RIGHT_COLUMN_CLEAR (below y=560, keep x ≤ 520).

## Checker test — v1 FAIL / v2 PASS

`factory/test_layout.py` runs the checker on the real v1 defects and on the
corrected positions:

- **FAIL (correctly):** v1 caption line (40,1070,680,1112) — deep in the
  covered zone; v1 progress bar (0,1246,720,1256); v1 header label
  (40,36,220,64); v1 question text 620 wide centred; one pixel into the
  action column (x1=521 below y=560).
- **PASS (correctly):** all seven v2 positions.
- A tall text block crossing y=560 at full width correctly FAILS on the
  right-column rule. A box exactly on a boundary passes.

The test run caught my own error first: the safe box rectangle itself fails
the right-column rule — correct behaviour for a text box, since the box is a
region, not text. The test was fixed, not the checker.

## Icon + micro-animation library

Original Pillow vector icons only — no copied artwork, no downloads, no emoji:
**question, check, cross, lightbulb, clock, brain, star, hourglass, arrow.**
Each is a function drawing into an RGBA image at any size, with colour and
line-weight parameters. Primitives, all pure functions of `t` (same input →
same output): `pop_scale` (0.8→1.0 ease-out, 0.4 s), `tick_progress` (0→1
over 0.3 s), `slide_offset`, `pulse_scale` (±0.04, 1 s period),
`fade_alpha`. Verified deterministic (same inputs → same bytes) and
primitives behave as specified (pop 0.8→1.0, tick 0.5 at 0.15 s, pulse 1.04
at 0.25 s, slide −110→0).

Catalog `factory/icons-catalog.jpg` (720×1420) viewed: the first version had
clipped titles, a cut-off animation strip, and a brain that read as two
rings. Fixed (brain redesigned as a bumpy harmonic outline with squiggle +
stem; catalog height 1420; titles shortened) and re-viewed — all 9 icons
read clearly at small size; animation strip complete (pop-in 3 sizes,
tick-draw empty→half→full check, pulse 3 clocks, slide-in 3 arrows).
Honest note: the brain is the most abstract icon — a stylised thinking blob,
usable as a phase marker, not a literal brain.

## v2 layout changes vs v1

Header label (80,180), counter right edge 640, progress track y=238–248
x 80–640 with fill + travelling dot (replaces the bottom progress bar);
phase icon (80,270) size 48 (question/lightbulb/clock/star/arrow per beat);
chip centred x=300 y=280; trivia question cx=300 max_w 440 y=360; riddle
clues from y=340, leading 48, gap 20 (with `fit_stack` — see below); think
recap from y=330, "THINK!" at y=680, countdown digit 130 pt centred
(300,780) with pulse; answer checkmark tick-draw centred (300,350) size 80,
banner pop-in x 80–520 y=400–510, "ANSWER" label y=440, answer text 48 pt
from y=540; **no static explain text** (the spoken explanation is shown
word-by-word in the caption band); captions show the **current sentence
only**, wrapped at 440, cx=300, bottom-anchored at 830, and are **suppressed
during ask beats** (question/clues already on screen as large text) **and
think beats** (no speech); intro/outro subtitle y=310, title pop-in top
y=430. Stripes kept (same params as v1).

## v2 verification results

Both videos PASS every check. Render A and render B are byte-identical
(determinism proven, not assumed).

| | Trivia quiz round v2 | Riddle round v2 |
|---|---|---|
| File | `prototype-1/v2/trivia-quiz-round-v2.mp4` | `prototype-1/v2/riddle-round-v2.mp4` |
| Format | 720×1280, 30 fps | 720×1280, 30 fps |
| Duration | 90.41 s | 92.29 s |
| Frames | 2712 (ffprobe) / 2713 written | 2768 / 2769 written |
| Size | 3,517,955 bytes | 4,273,047 bytes |
| SHA256 A = B | `ceba15848acad576ababd490ac2026175b87b4814794de97536b2030ad9073c6` | `77b34a9c74b906f79b51814071c8944169ac15acc30685e26d7b89a59034c299` |
| Render time | 62.3 s (A) / 64.3 s (B) | 73.5 s (A) / 82.2 s (B) |
| Safe-zone checker | **PASS — 2713 frames checked, 0 failed** | **PASS — 2769 frames checked, 0 failed** |
| blackdetect | 0 | 0 |
| freezedetect | 0 | 0 |
| silencedetect | 0 | 0 |
| Contact sheet | `prototype-1/v2/contact-sheet-trivia-quiz-round-v2.jpg` — viewed | `prototype-1/v2/contact-sheet-riddle-round-v2.jpg` — viewed |

Contact sheets confirm: captions sit in the subtitle band (ink measured at
full resolution: caption band x-centre 298–299 vs expected 300, y 793–815,
bottom-anchored at 830), icons read clearly (question mark on ask, clock on
think, checkmark tick on answer, star on intro, arrow on outro), answer
banners pop in, countdown digits pulse.

The safe-zone JSON for each video is beside it
(`<video>-safezone.json`: `passed: true`, `frames_failed: 0`). Run B files
are kept in `prototype-1/v2/runB/` as the determinism evidence; run A
SHA256s are in `prototype-1/v2/runA.sha256`.

Note: ffprobe counts 2712 frames where the renderer wrote 2713 (same for
the riddle: 2768 vs 2769). This matches v1 exactly (2712 / 90.41 s) — the
renderer's frame count rounds the total duration up to a whole frame; it is
not a v2 regression.

## Failures and fixes

The checker earned its keep: three real layout defects were caught by it
during this work, each fixed at the root rather than patched per video.

1. **Title too wide (smoke test, before any full render).** At 76 pt the
   title "CHALLENGE" is ~496 px wide; centred at x=300 it ran to x=52–548,
   failing left and right-column. Fixed: title font 76 → 64 pt (title box
   now 91–509). The smoke test caught this before a single full render.
2. **Title image height clipped the second line.** The old height formula
   (`sum(heights)+(n-1)*(leading-font_size)`) understated the image height
   and cut the bottom of "CHALLENGE". Fixed: total height is now
   `(n-1)*80 + last-line height`. Verified by ink measurement (title ink
   bottom 557, unclipped) and a full-res viewed frame.
3. **Word-wrap measured a different width than the draw path (two rounds).**
   - Round 1: `wrap()` measured the joined string, but `draw_caption`
     draws words with fixed 10 px gaps. DejaVu's space glyph is ~8 px at
     30 pt, so "That is your score out of five." measured 434 joined but
     drew 446 wide — 6 px past the 440 column. The checker failed 56
     outro frames. First fix: measure with 10 px gaps only.
   - Round 2: the gap-only measure broke 44 pt question lines, because at
     44 pt the space glyph is ~12 px — wider than the 10 px gap. Q5 "In
     what year did" measured 437 (gap) but drew 459 (joined). The checker
     failed 135 frames. Final fix: `wrap()` keeps a line only if
     **max(joined width, gap width) ≤ max_w**. Conservative for either
     draw path, and it can never overflow the column. Trivia then passed
     0/2713.
   - The two draw paths (`draw_lines_centered_r` draws the joined string;
     `draw_text_block`/`draw_caption` draw words with 10 px gaps) are the
     reason a single measure could not work. The max-of-both rule is now
     documented in `wrap()`'s docstring.
4. **Riddle clue stack overflowed the safe bottom.** The three clues wrap
   to up to 10 lines; at leading 48 / gap 20 the stack reached y=846, 6 px
   past the safe-box bottom (131 frames failed). Fixed with `fit_stack()`:
   the renderer wraps all visible clues first, then shrinks the leading
   (then the gap) until the whole stack fits y 340 → 830. This is a
   general capability for any future stacked-text format, not a riddle
   tweak. Riddle then passed 0/2769.
5. **My own edit error.** While adding `fit_stack` I swallowed the
   `def draw_lines_centered_r` line, leaving its body orphaned. Caught by
   reading the file back, restored, syntax-checked. No render ran on the
   broken file.

Also noted: the safe-zone JSON lists at most the first 20 violating frames
(`violations[:20]`); the `frames_failed` count is complete. That cap is a
reporting limit only — the PASS/FAIL verdict covers every frame.

## What is still missing

- **Richer animation.** The Pillow renderer cannot do character animation,
  lip-sync, or physics. What it can do — phase icons, pop-in, tick-draw,
  slide, pulse, fade, travelling progress — is now a library, but it is a
  deliberately small vocabulary. OpenFilm is the proven render layer if a
  future format needs richer motion (see the deep-inspection report).
- **Voice is still provisional af_heart.** The v2 renders reuse the v1
  narration WAVs. If Mohamed picks am_adam, re-synthesise and re-render
  (~2 min synthesis + ~70 s render per video).
- **No audience data yet.** The v2 videos are a layout/icons proof, not a
  format verdict. The fair-comparison method in `prototype-1/REPORT.md`
  still governs: a format wins only on comments/view **and** completion
  together, minimum 7 days and 1,000 views each.
- **The checker checks recorded boxes, not pixels.** It trusts the
  renderer to record every text box it draws. A pixel-level check (OCR or
  ink detection on the rendered frames) would catch a box the renderer
  forgot to record. The ink measurements in this report were a manual
  spot-check of that gap; automating it is future work.
