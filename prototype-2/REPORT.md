# Prototype 2 — Second-round videos (Day 2 production)

**Date:** 2026-11-22 (built ~20:00–20:15 UTC)
**Status: PASS for both videos** (see verification below).
**Not published anywhere.** Production only, per the brief — no TikTok
contact, no account access, nothing pushed to GitHub by this task.

## Deliverables

| File | What it is |
|---|---|
| `trivia-round-2.mp4` | Trivia/quiz round 2, 105.97 s |
| `riddle-round-2.mp4` | Riddle round 2, 109.49 s |
| `trivia-script.json`, `riddle-script.json` | Machine-readable scripts (incl. `facts` / `riddles` + sources) |
| `trivia-quiz-round-2-narration.wav`, `riddle-round-2-narration.wav` | Mixed narration tracks (24 kHz mono) |
| `trivia-quiz-round-2-timings.json`, `riddle-round-2-timings.json` | Beat/part start/end times (incl. `hold_after`) |
| `trivia-quiz-round-2-words.json`, `riddle-round-2-words.json` | faster-whisper word timestamps + WER |
| `segments/<id>/beatXX_partY.wav` | Individual narration parts (evidence) |
| `trivia-contact-sheet.jpg`, `riddle-contact-sheet.jpg` | Contact sheets (viewed) |
| `synth.py`, `caption.py`, `render.py`, `layout.py`, `icons.py` | Build pipeline (v2 pipeline reused, two adaptations — see below) |
| `runA.sha256`, `runB/` | Determinism evidence (run B byte-identical) |
| `trivia-round-2-safezone.json`, `riddle-round-2-safezone.json` | Safe-zone checker results (0 failed frames) |

## Voice

Both videos use **af_heart** (Kokoro-82M, American female), same as
round 1. Voice decision stands per the ownership rule: af_heart is
judged by audience data, not re-asked.

## The scripts (full text)

### Trivia round 2 (5 questions, 5 s think time each)

Hook pattern: **HOOKS.md #5, The Common Mistake** — the intro promises
one question catches almost everyone, and Q4 delivers it.

- **Intro:** "Five questions. One of them catches almost everyone —
  most people answer it wrong. See how many you can get right, and
  drop your score in the comments when you are done."
- **Q1 (easy opener):** "Question one, and this one is a warm-up.
  Which animal is the largest land animal in the world?" → think 5 s →
  "The African elephant. A big male can weigh up to seven tons."
- **Q2:** "Question two. One planet in our solar system does not spin
  like the others. Which planet spins on its side?" → think 5 s →
  "Uranus. It is tilted ninety-eight degrees, so it rolls around the
  Sun on its side."
- **Q3:** "Question three. Africa's highest peak — do you know its
  name? What is the tallest mountain in Africa?" → think 5 s →
  "Mount Kilimanjaro, in Tanzania. It stands nearly six thousand
  meters tall."
- **Q4 (common-mistake slot):** "Question four — and this one catches
  almost everyone. What is the largest desert in the world?" → think
  5 s → "The Antarctic desert. Not the Sahara — a desert means dry,
  not hot."
- **Q5 (hardest last):** "Question five, the last one — and the
  hardest. How many hearts does an octopus have?" → think 5 s →
  "Three. Two pump blood to the gills, and one pumps it around the
  body."
- **Outro:** "That is your score out of five. Did the desert question
  catch you? Tell me in the comments — and follow for round three."

### Riddle round 2 (3 riddles, "3 clues, 10 seconds" each)

Hook pattern: **HOOKS.md #8, The Personal Dare** — "pause the video
and try each one before I reveal the answer."

All three riddles are original wording written for this video. The
answers (bookmark, traffic light, pencil) are everyday objects; no
copyrighted text is used.

- **Intro:** "Three riddles. Pause the video and try each one before I
  reveal the answer — you get ten seconds each. Get all three, and
  your brain is officially warmed up."
- **Riddle 1 — answer: a bookmark.** Clue 1: "I hold your place in a
  story, but I never read a single word." Clue 2: "I slip between the
  pages and wait for you to come back." Clue 3: "Lose me, and you lose
  your place." → think 10 s → "A bookmark. It holds your place, but
  it never reads a word."
- **Riddle 2 — answer: a traffic light.** Clue 1: "I have three eyes,
  but I never blink." Clue 2: "I tell you when to stop and when to
  go, but I never say a word." Clue 3: "Red means wait, green means
  go — I change my mind all day." → think 10 s → "A traffic light.
  Three eyes, no words — just red, yellow, and green."
- **Riddle 3 — answer: a pencil.** Clue 1: "The more you use me, the
  shorter I get." Clue 2: "I leave my mark everywhere I go, but I
  never speak." Clue 3: "When I get it wrong, you rub it out and I
  try again." → think 10 s → "A pencil. It gets shorter with every
  word it writes."
- **Outro:** "How many did you solve? Tell me your score in the
  comments, and send this to a friend who thinks they are clever."

## Fact-checking (trivia answers — every fact verified before rendering)

| Question | Answer | Source |
|---|---|---|
| Which animal is the largest land animal in the world? | The African elephant — "African elephants are the largest land animals on Earth"; a big male weighs up to seven tons | National Geographic, "African elephant, facts and photos" — https://www.nationalgeographic.com/animals/mammals/facts/african-elephant |
| Which planet spins on its side? | Uranus — "rotates nearly on its side, with a 98 deg axial tilt" | NASA Goddard, "Solar System Tour — Uranus" — http://science.gsfc.nasa.gov/690/solar-system-tour/Uranus.html |
| What is the tallest mountain in Africa? | Mount Kilimanjaro, Tanzania — 5,895 m (19,341 ft); Tanzania National Parks Authority and UNESCO both list 5,895 m | Wikipedia, "Mount Kilimanjaro" (citing TANAPA and UNESCO) — https://en.wikipedia.org/wiki/Mount_Kilimanjaro |
| What is the largest desert in the world? | The Antarctic desert, ~14.2M km² — a desert is defined by low precipitation, not heat; the Sahara (9.2M km²) is the largest *hot* desert | Guinness World Records, "Largest desert" — https://www.guinnessworldrecords.com/world-records/largest-desert-cold |
| How many hearts does an octopus have? | Three — two pump blood through the gills, one circulates it around the body | Smithsonian Magazine, "Ten Wild Facts About Octopuses" — https://www.smithsonianmag.com/science-nature/ten-wild-facts-about-octopuses-they-have-three-hearts-big-brains-and-blue-blood-7625828/ |

No question repeats round 1 (Mars / Pacific / hexagon / gold /
Apollo 11).

## What M3 changed vs round 1

Source: `research/curiosity-science-2026-11-22.md` §9 + §8, and
`factory/DESIGN_RULES.md` Rule 3 (as refined by M3). Applied to both
videos:

1. **Post-reveal hold.** Every answer beat carries `hold_after: 1.5`
   in the script JSON. After the spoken reveal ends, the answer stays
   on screen for a clean 1.5 s beat with only the ambient bed playing —
   no new speech, no CTA, no fact, no score recap in the dead zone
   (Keller et al. 2024). The next beat is the next question's hook.
   Implemented in `synth.py` (the hold extends the answer beat's end
   in the timings; the bed covers it, so the audio is never silent);
   `render.py` needed no change — the beat simply lasts longer, and
   captions clear 0.6 s after the speech ends, leaving the answer
   alone on screen. Verified on full-res frames (see below).
2. **Gap sizing — foothold + guess test on every question.**

   | Question | Foothold (something the viewer already knows) | Guess test (a guess can form in the think time) | Difficulty |
   |---|---|---|---|
   | Q1 elephant | Elephants are famously huge | Everyone can guess "elephant" | Easy (opener) |
   | Q2 Uranus | Planets, spinning | Can pick a planet; likely wrong guesses Neptune / Venus | Medium |
   | Q3 Kilimanjaro | Africa, mountains | Kilimanjaro or Mount Kenya (5,199 m, 2nd highest) | Medium |
   | Q4 desert | The Sahara | Almost everyone guesses Sahara — wrong (hypercorrection) | Common-mistake slot |
   | Q5 octopus hearts | Octopus, hearts | Most guess one — wrong | Hardest (closer) |
   | R1 bookmark | Books, reading | "Bookmark" / "page" / "dog-ear" | Easy (opener) |
   | R2 traffic light | Roads, driving | "Traffic light" / "camera" / "robot" | Medium |
   | R3 pencil | Desk, school | "Pencil" / "candle" (candle trap: gets shorter too, but clue 3 — rub it out — rules it out) | Hardest (closer) |

   Difficulty rises through each round: easy opener, hardest last.
   Nothing was dropped by the tests — no question lacked a foothold
   or a formable guess.
3. **Next-question hooks are real gaps.** Each ask opens with a
   gap-creating lead, not a bare number: Q2 "One planet does not spin
   like the others", Q3 "Africa's highest peak — do you know its
   name?", Q4 "this one catches almost everyone", Q5 "the last one —
   and the hardest"; riddle 2 "this one looks easy until the third
   clue", riddle 3 "the last one — the trickiest of the three".
4. **Score recap and CTA only at the end.** The outro carries the
   score recap ("That is your score out of five") as the payoff the
   hook promised, then the comment/follow ask — after the final
   payoff, where no gap is open. No score recap appears after any
   reveal.

## How each video is built (v2 pipeline reused, two adaptations)

- **Narration:** Kokoro-82M via kokoro-onnx, voice af_heart, speed
  1.0, lang en-us, venv `~/workspace/venv-inspection/` (nothing
  reinstalled). Same mixing as round 1 (0.25 s part gaps, 0.35 s beat
  gaps, tick + bed under think time, ding at each reveal, quiet
  110+165 Hz bed across the whole track).
- **Pipeline adaptations (only two):**
  - `synth.py`: `hold_after` on answer beats (see §M3-1 above).
  - `render.py` (copy of v2 `render2.py`): the riddle check is now
    `spec["id"].startswith("riddle")` instead of `== "riddle-round"`,
    because the new ids are `trivia-quiz-round-2` / `riddle-round-2`.
    Everything else — safe-zone checker on every frame, icons, motion,
    stripes, caption band — is the v2 code unchanged (`layout.py` and
    `icons.py` copied verbatim).
- **Captions:** faster-whisper tiny.en (int8 CPU, av==12.3.0 pinned),
  word-level timestamps, karaoke-style captions in the subtitle band.
- **Encode:** libx264 veryfast, crf 23, yuv420p, AAC 128k, +faststart.

## Measured results

### Trivia round 2 — PASS (final build; first build superseded — see §Failures)

- ffprobe: 720×1280, 30 fps, duration 105.967000 s, 3179 frames
  (renderer wrote 3180), H.264 + AAC, 4,144,004 bytes.
- SHA256: `1c75f2b8d6abf8c066a4fbd4be4f32f70b321cbe0dc31efc61de403eb4d2d4f9`
  — rerun byte-identical (`cmp` confirms).
- Narration: 105.97 s total, 210 words, synthesis 71.0 s
  (per-part RTF 0.78–1.11). Mix peak 0.555, RMS 0.0519. Kokoro peak
  RSS 714 MB.
- Captions: faster-whisper tiny.en, load 2.0 s, transcribe 4.8 s,
  language en p=1.00, **WER 0.019** (4 edits / 206 ref words),
  205 words timestamped, peak RSS 289 MB.
- Render time: 76.6 s (run A).
- Safe-zone checker: **PASS — 3180 frames checked, 0 failed.**
- blackdetect: 0 black segments. freezedetect: 0 frozen segments.
  silencedetect: 0 silence segments.
- Contact sheet viewed: real picture — title, legible questions,
  THINK! countdowns, green ANSWER banners, captions with the current
  word highlighted, progress bar, travelling dot. Full-res frames
  viewed for the Q4 reveal (answer + caption cleanly separated) and
  the Q4 hold (clean answer, no caption).

### Riddle round 2 — PASS

- ffprobe: 720×1280, 30 fps, duration 109.490000 s, 3284 frames
  (renderer wrote 3285), H.264 + AAC, 5,033,757 bytes.
- SHA256: `ad9b3fccdcc4fd1ca78512641e19e56573db53a4e4f9b46c9aa9e12aabd33f31`
  — rerun byte-identical (`cmp` confirms).
- Narration: 109.49 s total, 242 words, synthesis 69.5 s
  (per-part RTF 0.86–1.11). Mix peak 0.711, RMS 0.0513. Kokoro peak
  RSS 718 MB.
- Captions: faster-whisper tiny.en, load 1.9 s, transcribe 6.8 s,
  language en p=1.00, **WER 0.017** (4 edits / 237 ref words),
  237 words timestamped, peak RSS 293 MB.
- Render time: 91.4 s (run A).
- Safe-zone checker: **PASS — 3285 frames checked, 0 failed.**
- blackdetect: 0 black segments. freezedetect: 0 frozen segments.
  silencedetect: 0 silence segments.
- Contact sheet viewed: clues accumulating one by one, THINK!
  countdown (10 s), green ANSWER banners, captions present.
  Full-res frames viewed for the riddle-2 reveal (answer + 2-line
  caption, no overlap) and the riddle-2 hold (clean answer).

## Failures and fixes

1. **Q4 caption overwrote the answer text (trivia, first build).**
   The first trivia render passed every automated check — safe-zone
   0/3341, black/freeze/silence 0 — but a full-res frame of the Q4
   reveal showed the 6-line caption ("Not the Sahara — the Sahara is
   the largest hot desert, but Antarctica is bigger, about fourteen
   million square kilometers of ice.") climbing over the two-line
   answer "THE ANTARCTIC / DESERT". Both texts were illegible where
   they overlapped.
   Root cause: the caption block is bottom-anchored at y=830 with a
   42 px line height, so a 6-line caption starts at y=578 — inside
   the answer text (y 540–652). The safe-zone checker cannot catch
   this: both boxes are inside the safe box; it checks containment,
   not text-on-text overlap. (Same class of gap as the v2 report's
   honest note: the checker trusts recorded boxes, not pixels.)
   Fix (content, at the root for this format): the Q4 reveal was
   shortened to "The Antarctic desert. Not the Sahara — a desert
   means dry, not hot." (71 chars, 3 caption lines, top y=704, 52 px
   clear of the answer). The size fact (14.2M vs 9.2M km²) moved to
   the script's `explain` field and this report; the definition
   ("a desert means dry, not hot") still does the M3 job of making
   the answer feel inevitable. The trivia video was re-synthesised,
   re-captioned and re-rendered from scratch; the first build
   (SHA `b3764b80…`, 111.36 s) is superseded and its MP4 replaced.
   The fix was verified on full-res frames, not just the contact
   sheet. **New factory rule recorded in `factory/DESIGN_RULES.md`
   Rule 3: a reveal's spoken text must caption in ≤4 lines
   (~75 characters captions in 3 lines and is comfortable).**
2. **Whisper notes (ASR confusions, not proven errors).** Trivia:
   "ninety-eight" heard as "98" (normalisation); "Uranus",
   "Kilimanjaro", "Antarctic" all transcribed correctly. Riddle:
   "Ten seconds, go" heard as "10 seconds go". The on-screen text
   always shows the correct answer, so a viewer is never misled.
3. **Round 2 is longer than round 1** (trivia 105.97 s vs 90.41 s;
   riddle 109.49 s vs 92.29 s). Causes: the 1.5 s hold after each
   reveal (+7.5 s trivia / +4.5 s riddle) and longer hook leads in
   the ask parts. This is a deliberate M3 cost, not a defect — but
   completion must be read against it: if round 2 completion falls
   vs round 1, the first suspect is length, and the next test
   isolates it.

## What this does NOT prove

- That the M3 changes (holds, gap sizing, common-mistake slot) help
  with a real audience. They are built from lab evidence and applied
  as designed; only Studio retention curves and comment behaviour
  can confirm them. H-M3-1 (common-mistake vs straightforward) and
  H-M3-3 (the "why" line) are the hypotheses these videos feed.
- That the voice sounds natural or American to a US audience
  (af_heart is judged by audience data, per the ownership rule).
- That either format will perform. No success numbers, no winner —
  that needs the comparison in `prototype-1/REPORT.md` and
  `factory/EXPERIMENTS.md` (7 days, 1,000 views, comments/view AND
  completion together).

## Next step

These are Day 2 production files, ready for the publishing schedule
(3/day from 2026-11-23). Nothing was published by this task. The
third video of Day 2 needs a new round (new questions/riddles) — the
pipeline in this directory is the reusable instrument for it.
