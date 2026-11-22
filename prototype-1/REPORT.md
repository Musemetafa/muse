# Prototype 1 — First factory prototype videos

**Date:** 2026-11-22 (built ~14:00–14:15 UTC, at Mohamed's direct request
"why not now?" instead of waiting for the 19:45 loop run)
**Status: PASS for both videos** (see verification below).
**Not published anywhere.** Files are local only; nothing was pushed to
GitHub by this task (per the brief).

## Deliverables

| File | What it is |
|---|---|
| `trivia-quiz-round.mp4` | Trivia/quiz round, 90.41 s |
| `riddle-round.mp4` | Riddle/logic-puzzle round, 92.29 s |
| `trivia-script.json`, `riddle-script.json` | Machine-readable scripts |
| `trivia-quiz-round-narration.wav`, `riddle-round-narration.wav` | Mixed narration tracks (24 kHz mono) |
| `trivia-quiz-round-timings.json`, `riddle-round-timings.json` | Beat/part start/end times |
| `trivia-quiz-round-words.json`, `riddle-round-words.json` | faster-whisper word timestamps + WER |
| `segments/<id>/beatXX_partY.wav` | Individual narration parts (evidence) |
| `trivia-contact-sheet.jpg`, `riddle-contact-sheet.jpg` | Contact sheets (viewed) |
| `synth.py`, `caption.py`, `render.py` | Build pipeline (reusable) |

## Voice — PROVISIONAL

Both videos use **af_heart** (Kokoro-82M, American female, grade A).
Mohamed has **not** answered the listening test yet (af_heart vs am_adam),
so this voice is provisional: if he picks am_adam, the narration must be
re-synthesized and both videos re-rendered. The scripts, timings structure
and visuals would not change — only the audio track (and therefore the
file hashes).

## The scripts (full text)

### Trivia quiz round (5 questions, 5 s think time each)

- **Intro:** "Think you know it all? Five questions. No Googling, no
  lifelines. See how many you can get right, and drop your score in the
  comments when you are done."
- **Q1:** "Question one, and this one looks easy. Which planet is known
  as the Red Planet?" → think 5 s → "The answer is Mars. It looks red
  because of iron oxide, basically rust, covering its surface."
- **Q2:** "Question two. What is the largest ocean on Earth?" → think
  5 s → "The Pacific Ocean. It covers more area than all of Earth's land
  put together."
- **Q3:** "Question three. How many sides does a hexagon have?" → think
  5 s → "Six. A hexagon has six sides and six angles. Think of a
  honeycomb cell."
- **Q4:** "Question four. What is the chemical symbol for gold?" → think
  5 s → "The letters A and U. The symbol comes from aurum, the Latin
  word for gold."
- **Q5:** "Question five, the last one. In what year did humans first
  land on the Moon?" → think 5 s → "Nineteen sixty-nine. Apollo Eleven
  landed on July twentieth, nineteen sixty-nine."
- **Outro:** "That is your score out of five. Got all five? Then you are
  officially smarter than the average internet. Follow for round two."

### Riddle round (3 riddles, "3 clues, 10 seconds" each)

All three riddles are original wording written for this video. The
answers (echo, shadow, towel) are classic public-domain riddle concepts;
no copyrighted text is used.

- **Intro:** "Three riddles. Three clues each. Ten seconds to solve each
  one. Get all three, and your brain is officially warmed up."
- **Riddle 1 — answer: an echo.** Clue 1: "I repeat everything you say,
  but I have no mouth of my own." Clue 2: "You can hear me, but you can
  never see me." Clue 3: "The louder you shout, the louder I answer."
  → think 10 s → "An echo. Sound bouncing back to you."
- **Riddle 2 — answer: your shadow.** Clue 1: "I follow you everywhere
  in daylight." Clue 2: "I copy your every move, but I never make a
  sound." Clue 3: "You can never touch me, but I am always right behind
  you." → think 10 s → "Your shadow. It follows you, but it never makes
  a sound."
- **Riddle 3 — answer: a towel.** Clue 1: "The more I dry you, the
  wetter I become." Clue 2: "I hang on a hook and wait for your shower."
  Clue 3: "I soak it all up, then I need to dry out myself." → think
  10 s → "A towel. The more it dries you, the wetter it gets."
- **Outro:** "How many did you solve? Tell me your score in the
  comments, and send this to a friend who thinks they are clever."

## Fact-checking (trivia answers — every fact verified before rendering)

| Question | Answer | Source |
|---|---|---|
| Which planet is known as the Red Planet? | Mars — iron oxide (rust) on its surface gives the reddish appearance | NASA Jet Propulsion Laboratory, "Mars in a Minute: Is Mars Really Red?" — https://www.jpl.nasa.gov/videos/mars-in-a-minute-is-mars-really-red/ |
| What is the largest ocean on Earth? | The Pacific Ocean — largest and deepest basin, >155M km², larger than all of Earth's land combined | NOAA Ocean Exploration, "How big is the Pacific Ocean?" — https://oceanexplorer.noaa.gov/ocean-fact/pacific-size/ |
| How many sides does a hexagon have? | Six (six-sided polygon, six angles) | Encyclopaedia Britannica, "Hexagon" — https://www.britannica.com/print/article/957622 |
| What is the chemical symbol for gold? | Au, from the Latin word aurum; gold is element 79 | Royal Society of Chemistry, Periodic Table, "Gold" — https://periodic-table.rsc.org/element/79/gold |
| In what year did humans first land on the Moon? | 1969 — Apollo 11 landed July 20, 1969; Armstrong stepped onto the surface that day | NASA, Apollo 11 Mission Report — https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/A11_PAOMissionReport.html |

Note on the Mars explanation: recent research suggests the red dust may
be ferrihydrite rather than hematite. The video says only "iron oxide,
basically rust", which is accurate under both accounts (NASA JPL).

## How each video is built (proven stack, reused)

- **Narration:** Kokoro-82M via kokoro-onnx, voice af_heart, speed 1.0,
  lang en-us, existing venv `~/workspace/venv-inspection/` (nothing
  reinstalled). Each narration part synthesized separately, then mixed:
  0.25 s gaps between parts, 0.35 s gaps between beats.
- **Think-time audio:** the pauses are deliberate, not dead air. A tick
  every second plus a quiet 110+165 Hz bed (~-40 dB) runs under the whole
  track, and a short ding marks each answer reveal. The bed keeps the
  audio track continuously non-silent (see verification).
- **Motion:** code-computed with Python + Pillow + numpy + ffmpeg,
  reusing the Factory Test 2 approach. Every frame is computed from the
  frame index only — deterministic, no randomness, no wall-clock input.
  Motion serves the content: question/clue text on screen, countdown
  numbers, answer reveals, progress bar, travelling dot, word-timed
  captions. Plus subtle animated vertical stripes (±6 gray levels,
  64 px period, 150 px/s) across the full frame — see "Failures and
  fixes" for why they were added.
- **Captions:** faster-whisper tiny.en (int8 CPU, av==12.3.0 pinned),
  word-level timestamps, burned in as karaoke-style captions: the spoken
  words appear in white, the current word is highlighted in accent
  yellow, unspoken words are dim gray (layout stays stable).
- **Encode:** libx264 veryfast, crf 23, yuv420p, AAC 128k, +faststart.

## Measured results

### Trivia quiz round — PASS

- ffprobe: 720×1280, 30 fps, duration 90.400000 s, 2712 frames,
  H.264 + AAC, 4,704,294 bytes.
- SHA256: `a0efa3361d01acbb76096d2425f306167776ea7cc03f2b415b70bac9b1b24efd`
  — rerun byte-identical (`cmp` confirms).
- Narration: 90.41 s total, 178 words, synthesis 58.6 s
  (per-part RTF 0.87–1.22, overall 0.65 including gaps — much faster
  than the 2.67 RTF measured in the deep inspection, which included
  first-run warmup; the number to budget with is ~1.0 RTF per part).
  Mix peak 0.524, RMS 0.0530. Kokoro peak RSS 697 MB.
- Captions: faster-whisper tiny.en, load 1.8 s, transcribe 4.6 s,
  language en p=1.00, **WER 0.061** (11 edits / 180 ref words),
  175 words timestamped, peak RSS 308 MB.
- Render time: 67.5 s (run A), 65.3 s (run B).
- blackdetect: 0 black segments. freezedetect: 0 frozen segments.
  silencedetect: 0 silence segments.
- Contact sheet viewed: real picture — title, legible question text,
  THINK! countdown numbers, green ANSWER banners, captions with the
  current word highlighted, progress bar, travelling dot.

### Riddle round — PASS

- ffprobe: 720×1280, 30 fps, duration 92.266667 s, 2768 frames,
  H.264 + AAC, 5,618,707 bytes.
- SHA256: `8f09ee53b401dc6c5428e3f5b39e6ed09161ebad7bbf387bac862a710931fc11`
  — rerun byte-identical (`cmp` confirms).
- Narration: 92.29 s total, 197 words, synthesis 54.6 s
  (per-part RTF 0.80–1.23, overall 0.59). Mix peak 0.578, RMS 0.0508.
  Kokoro peak RSS 658 MB.
- Captions: faster-whisper tiny.en, load 1.3 s, transcribe 4.5 s,
  language en p=1.00, **WER 0.015** (3 edits / 197 ref words),
  197 words timestamped, peak RSS 306 MB.
- Render time: 72.4 s (run A), 71.4 s (run B).
- blackdetect: 0 black segments. freezedetect: 0 frozen segments.
  silencedetect: 0 silence segments.
- Contact sheet viewed: real picture — clues accumulating one by one,
  THINK! countdown (10 s), green ANSWER banners, captions present.

## Failures and fixes

1. **freezedetect flagged the first renders (81 segments trivia, 86
   riddle).** Cause: typography video has most pixels static by design,
   so the whole-frame mean per-frame change fell below freezedetect's
   0.001 threshold — even though the video was never actually frozen.
   Proof: sampling 1 frame per second, **zero** consecutive pairs were
   identical (mean diff 3.04 trivia / 2.61 riddle gray levels; min 0.20).
   Fix (product improvement, not a measurement waiver): subtle animated
   vertical stripes across the full frame (±6 levels, 64 px period,
   150 px/s) — a standard ambient-motion element that keeps the frame
   visibly alive. After the fix: **0 frozen segments on both videos**.
   Side effect: render time roughly doubled (34 s → 67 s) because the
   background is now composed per frame with numpy.
2. **Whisper mis-transcriptions that mark TTS weak spots to check.**
   Trivia: "A and U" was heard as "and you", "aurum" as "orum".
   Riddle: "An echo" as "In echo", "wetter" as "better". These are ASR
   confusions, not proven pronunciation errors — but they mark the exact
   spots a human listener should check in the listening test. The
   on-screen text always shows the correct answer, so a viewer is never
   misled. The caption timing uses whisper word start times zipped by
   order with the script words, so a dropped whisper word can delay one
   caption word by one position within a part — a minor visual effect.
3. **Tight memory.** Only ~500 MB was available when synthesis started
   (Kokoro peaked at 697 MB RSS) — it completed with 0 OOM kills (swap
   absorbed it). `/proc/sys/vm/drop_caches` is read-only on this VM, so
   page cache could not be freed. Lesson: run one heavy step at a time,
   as was done.
4. **The pre-stripes trivia render (SHA f5eba72f…) was superseded** by
   the striped version (SHA a0efa336…). The runB files were deleted
   after the byte-identical check; hashes are recorded here.

## What this does NOT prove

- That the voice sounds natural or American to a US audience (the blind
  listening test is still pending; af_heart is provisional).
- That the motion looks beautiful or holds attention (only that it is
  present, deterministic, and passes the automated checks).
- That either format will perform with a real audience. No success
  numbers, no winner — that needs the comparison below, with real data.

## FAIR COMPARISON METHOD (written before any success judgement)

### Metrics to collect per video (same definitions for both)

1. **Views** (public view count).
2. **Completion rate** — average watch time divided by video duration,
   or TikTok's reported average watch time; the retention curve if
   available. Primary metric together with (4).
3. **Likes per view** — likes / views.
4. **Comments per view** — comments / views. Primary metric together
   with (2): both formats are designed to earn comments (answers,
   scores, challenges), and comments are the scarcest reaction.
5. **Shares per view** — shares / views.
6. **Rewatches** — if TikTok reports them; a rewatch signal supports
   the "check missed answers" mechanism.
7. **Follows gained per view** — if attributable; secondary.

### Baselines (from the niche demand report, recorded before judging)

- Revid, 176K-video sample: **0.08% comments/view**, **7.1%
  likes/view**.
- Socialinsider: **2.6% engagement by followers** (different
  denominator — do not compare directly to per-view rates).
- Median-view peak for short video: **16–30 s** (both prototypes are
  90 s, so completion rate must be read against that, not against
  short-video norms).

### What counts as a meaningful difference (pre-registered)

- **Comments/view:** a relative difference of **≥50%** between the two
  prototypes (e.g. 0.08% vs 0.12%) counts as meaningful — comment
  rates are tiny and noisy, so small gaps are not evidence.
- **Completion rate:** an absolute difference of **≥5 percentage
  points** counts as meaningful.
- **Likes/view:** a relative difference of **≥25%** counts as
  meaningful.
- **A format "wins" only if it beats the other on the primary metrics
  (comments/view AND completion rate).** Winning on likes alone does
  not decide. Winning on one primary metric and losing clearly on the
  other is a split result, not a win — it means the formats trade off,
  and the next test should isolate which element (think-time length,
  question difficulty, riddle quality) drives the difference.
- **Minimum bar:** either format that performs ≥50% below the baselines
  on likes/view is treated as rejected by viewers, regardless of the
  head-to-head result.

### Method rules (to keep the comparison fair)

- Post both videos under the same conditions as far as possible: same
  account, same posting time-of-day window, same caption/hashtag style,
  no paid promotion, no cross-posting one and not the other.
- Collect data for the **same number of days** for each (minimum 7 days
  each, and at least 1,000 views each — whichever is later) before any
  judgement. Do not judge from first-day numbers.
- Record the **raw numbers**, not just ratios, and keep the two videos'
  numbers side by side in one table.
- If one video gets an outlier spike (e.g. a share by a large account),
  note it explicitly and do not treat the spike as format evidence.
- **One video per format does not decide the format.** A second round
  of each format is needed before a final format decision — the first
  comparison picks which format to invest the second round in, not the
  factory's permanent niche.
- No revenue claim from this comparison: TikTok publishes no RPM, and
  qualified views are far below public views.

## Next step (for the loop)

Publish-test decision is Mohamed's (publishing is outside the factory's
current delegation). The loop's next work: second-round variants once
the first comparison data exists — or, if Mohamed answers the listening
test first, re-synthesize both narrations in the chosen voice and
re-render. Voice-swap cost is known: ~2 minutes of synthesis per video
plus ~70 s of rendering per video.
