# Factory Design Rules

These are factory law: they apply to every video the factory builds,
in every format, from now on. They are not fixes to one video.

They exist because Mohamed corrected the framing on 2026-11-22: fixing
the two prototype videos was NOT the goal. The safe zone and the
icons/animation are deeper — they are part of how the factory builds
every video. A video that breaks a rule fails verification, exactly
like a video with black or frozen frames.

## Rule 1 — Safe zone: no text where TikTok puts its interface

TikTok draws its own interface on top of every video: tabs and search
at the top, the username / caption / sound at the bottom, and the
like / comment / share buttons in a column on the right. Text placed
under that interface is invisible to the viewer.

The numbers come from TikTok's own published In-Feed ads template
(1080x1920), scaled to our 720x1280 canvas:

| Edge | Keep clear (720x1280) |
|---|---|
| Top | 160 px |
| Bottom | 440 px |
| Left / right | 80 px |
| Right column (below y=560) | keep text x <= 520 |

Safe box: **x 80–640, y 160–840.** Below y=560 the action buttons
sit on the right, so text there must end at x<=520. That is why the
factory centres body content on x=300 with a max width of 440 px
(x 80–520) instead of centring on the frame middle.

Named zones (see `factory/layout.py`):

- **Hook zone** — upper middle, y ~200–470. Titles and hooks.
- **Body zone** — question / clue / answer text, centred on x=300.
- **Subtitle band** — captions live here, y ~700–830, bottom-anchored
  at y=830. Captions never go below 840.
- **CTA zone** — middle of the frame, never the bottom quarter.

The factory designs to the stricter ads template even though organic
posts cover less (measured: top ~133, bottom ~223, right ~93 on
720x1280), because the ads template guarantees visibility in every
placement. The organic numbers are recorded in `layout.py` for
reference only.

**Enforcement:** `layout.check_boxes()` checks every text box on
sampled frames. A video with any text outside the safe box FAILS
verification. The checker test (`factory/test_layout.py`) proves it
catches the real v1 defect: v1 captions at y=1070 and the v1 progress
bar at y=1246 both fail; the corrected v2 positions pass.

## Rule 2 — Motion with purpose

Every motion element must serve structure, reward, or identity:

- **Structure** — signal the format's phases: question icon on
  question cards, timer icon on the countdown, checkmark tick on the
  answer reveal, pop-in on the answer banner. The viewer always knows
  where they are in the round.
- **Reward** — reward attention: the reveal pop, the tick drawing
  itself, the countdown pulse. Small payoffs for staying.
- **Identity** — build recognition: the same icons, the same accent
  colour, the same progress track in the header, in every video.

Decoration without function is noise. If a motion element does none of
the three, it does not go in.

**Icons are original.** Every icon is drawn in code with Pillow vector
shapes (`factory/icons.py`) — circles, polygons, lines, arcs. No copied
artwork, no downloaded icon sets, no emoji rendered as icons. That
keeps the factory free of any licence or likeness question, and it
means any icon can be redrawn at any size, in any colour, with any
line weight.

**Micro-animation primitives are pure functions of time** (`icons.py`):
pop-in (scale 0.8→1.0, ease-out), tick-draw (checkmark stroke over
0.3 s), slide-in, pulse (gentle scale loop), fade. Same time input
gives the same picture, so determinism is preserved — a re-render is
byte-identical.

## What the current stack cannot do (recorded honestly)

- Rich character animation, lip-sync, and physics-based motion are
  out of reach for the Pillow frame-by-frame renderer. The motion
  vocabulary is: slides, pops, pulses, ticks, travelling dots and
  progress bars, plus the ambient stripe field.
- OpenFilm (HTML/CSS/JS rendering) can do richer animation than
  Pillow, and is the proven render layer for it. If a future format
  needs motion Pillow cannot express, the format moves to OpenFilm
  rather than stretching Pillow.
- The brain icon is the most abstract in the library: it reads as a
  stylised thinking blob at small size, not a literal brain. It is
  usable as a phase marker; it is not a literal illustration.
