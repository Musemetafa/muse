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

## Rule 3 — Retention: the hook and the pacing (Module 2)

Evidence: `research/retention-hooks-2026-11-22.md`. Level: LEARNING — no
retention data from our own videos exists yet, so these rules are built
from TikTok's own guidance and published retention data, and they are
revised in writing when our Studio curves arrive.

- **Promise by second 3.** The video's promise — what it is, what the
  viewer gets — is spoken and on screen by second 3. Design to 2,
  deadline 3. No greeting, no introduction, no logo-first frame.
- **Frame 0 is live.** Something moves or changes in the first frame.
  A static title card is not an opening.
- **The question stays visible ≥3 seconds,** and the first change
  (an elimination, a tick, a movement) lands before second 3.
- **No dead seconds.** Every second of think time shows change —
  countdown, progress, elimination, motion. A pause with nothing
  changing is a lull and is cut.
- **The promise test.** Every hook must deliver the exact thing it
  promised. A hook that fails is rewritten, not published.
- **Nothing unrelated immediately after a reveal.** The beat after a
  reveal is the next question's hook — not an unrelated fact, a CTA,
  branding, or a score recap. A one-sentence 'why' that belongs to the
  answer just given is part of the reveal, not a violation. The reveal
  itself gets a clean 1–2 second beat (answer + why, spoken and on
  screen) before the next hook, and the next hook must be a real gap
  ('Question 4' is not a hook). CONFIRMED as a rule by Module 3
  (Keller et al. 2024, [ACADEMIC]); behavioural effect of a CTA after
  a reveal still UNPROVEN — H-M3-2 tests it.
- **Hook patterns live in `factory/HOOKS.md`.** One pattern per video.
  The hook zone (y ~200–470) carries the promise text; the subtitle
  band carries it in captions at the same time, so the hook survives
  muted viewing.
- **A reveal's spoken text must caption in ≤4 lines.** The answer text
  sits at y 540 and the caption block is bottom-anchored at 830 with a
  42 px line height, so a 5-line caption climbs into a two-line answer
  (found on trivia round 2 Q4: a 6-line caption overwrote the answer
  text — the safe-zone checker does not catch text-on-text overlap,
  only text outside the safe box). Keep the why to one short sentence;
  ~75 characters captions in 3 lines and is comfortable. If a reveal
  needs a longer fact, the fact belongs in the script's `explain` field
  and the report, not in the spoken reveal.

## Rule 4 — Question design: the gap, the reveal, the dead zone (Module 3)

Evidence: `research/curiosity-science-2026-11-22.md`. Level: LEARNING —
lab findings, no feed transfer proven; the rules are adopted on academic
evidence and are revised in writing when our own data, or a replication,
says otherwise. The v2 prototypes are unchanged (they are the control);
these rules govern round 2 onward.

- **The "almost know" rule.** Every question passes the foothold test
  (it contains something the viewer already knows) and the guess test
  (a viewer can form a guess in the think time, even a wrong one).
  Difficulty rises across a round: easy opener, medium middle, hardest
  last. A question with no foothold is dropped, not simplified into a
  giveaway.
- **At least one common-mistake question per round.** The obvious answer
  is wrong. Strongest memory device and most commentable question type.
- **The reveal has three jobs.** State the answer unambiguously; show
  why the likely guess was wrong in one short sentence; give the one
  fact that makes the true answer feel inevitable. Then a clean 1–2
  second beat on the answer before the next hook.
- **Nothing unrelated immediately after a reveal.** (Rule 3's confirmed
  form; M3 §8.) No unrelated fact, CTA, branding, or score recap in the
  post-reveal beat. Scores appear at the end of the round only.
- **Fact-checking is memory-critical.** A wrong answer is hyper-encoded
  by exactly the viewers who engaged hardest. Every answer is verified
  before rendering; "obvious" answers get the same verification as
  obscure ones.
- **The attempt is the product.** The video is built so answering in
  the head is the natural behaviour: question visible, countdown gives
  time, voice asks the viewer to commit before the timer ends.
