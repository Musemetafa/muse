# Factory State

Live operating state. Updated by every run. Last updated: 2026-11-22 ~14:15 UTC.

## Highest goal

Build an advanced video factory that invents and produces English-language
video for a US audience and earns income from TikTok, with growing
independence from Mohamed's daily involvement. Zero spend in this stage.

## Done

- 2026-11-21: Environment audit (`audit/environment-audit-2026-11-21.md`).
  CPU-only VM, no GPU, ffmpeg works, no local AI video tools.
- 2026-11-22: Open-source discovery, 9 candidates
  (`research/open-source-video-factory-2026-11-22.md`). Top three for deeper
  inspection: OpenFilm, Kokoro-82M TTS, faster-whisper.
- 2026-11-22: Factory Test 1 (`factory-test-1/`). Deterministic 720x1280
  6-second assembly from JSON, byte-identical reruns, automated checks.
  Proves assembly only, not motion or audience appeal.
- 2026-11-22: Repository `Musemetafa/muse` created, app installed, first
  snapshot pushed (commit `e8c71405`). Read and write access verified.
- 2026-11-22: Deep inspection of OpenFilm, Kokoro-82M, faster-whisper
  (`research/deep-inspection-openfilm-kokoro-whisper-2026-11-22.md`).
  OpenFilm: INTEGRATE conditionally (MIT verified). Kokoro-82M: ADOPT via
  kokoro-onnx (Apache-2.0 verified; RTF 2.67, slower than real time;
  naturalness needs a listening test). faster-whisper: ADOPT as-is,
  tiny.en default (RTF 0.20, 279 MB; pin av==12.3.0). Voice-to-verify
  pipeline proven end-to-end on CPU.
- 2026-11-22: OpenFilm render test PASSED on retry
  (`research/openfilm-render-test-2026-11-22.md`). Chromium downloaded
  (Chrome Headless Shell 149, 114.2 MiB); minimal film rendered 720x1280,
  6.000000 s, 180 frames, 30 fps, H.264; no black/frozen frames; render
  34.1 s first run, 28.7 s rerun; rerun byte-identical (determinism
  proven). Rule learned: OpenFilm Studio must be stopped after each
  render (it leaves 2 node processes, ~216 MB, port 4747). This proves
  the render layer only — not voice, generation, or audience appeal.
- 2026-11-22: Factory Test 2 (`factory-test-2/`) PASSED. Code-computed
  motion (slide-in title + travelling dot, growing circle + sweeping
  bar, bouncing ball + progress bar), 720x1280, 30 fps, 6.0 s, 180
  frames; byte-identical reruns (SHA256 9f3d5325..., reproduced across
  working directories); no black, no frozen (Test 1's frozen flags are
  gone), no silence; motion measured at frame level (0/59 zero-change
  consecutive pairs in scene 3). Render ~5.5 s from workspace disk.
  Lesson: /tmp was wiped mid-run — evidence must be written to
  ~/workspace immediately, never left in /tmp between steps.
- **Prototype videos — DONE, both PASS.** Started early at Mohamed's
  request (13:57 UTC) instead of waiting for the 19:45 run; built and
  verified 14:15 UTC (`prototype-1/`): trivia quiz round 90.41 s and
  riddle round 92.29 s, 720x1280, 30 fps, Kokoro af_heart narration
  (provisional), code-computed motion, word-timed captions; reruns
  byte-identical; no black/frozen/silence; contact sheets viewed and
  legible. First end-to-end 90 s narrated videos from the factory.
  Whisper flagged spots to listen for: "A and U"→"and you",
  "aurum"→"orum", "wetter"→"better", "An echo"→"In echo". Fair
  comparison method written in prototype-1/REPORT.md; no winner
  declared — needs real audience data.
  (`research/niche-discovery-2026-11-22.md`, synthesis of three reports:
  `niche-demand-2026-11-22.md`, `niche-formats-stack-fit-2026-11-22.md`,
  `niche-commercial-2026-11-22.md`). Ranked shortlist against the six
  criteria: (1) trivia/quiz, (2) riddles/puzzles — prototype first;
  (3) did-you-know facts, (4) history/science explainers — second wave;
  word games and listicles held as quiz variants; motivational and
  storytime formats out for now. Design rule from TikTok policy: every
  prototype 60+ s with narration + motion + captions (text-only is
  excluded from Creator Rewards as "not original"). No RPM-based revenue
  forecast — TikTok publishes no rate.

## In progress

- **Mohamed's evaluation of the two prototypes.** He watches/listens to
  the trivia and riddle videos, judges voice naturalness (af_heart vs
  am_adam), visual appeal, and which format he prefers. No loop work
  depends on his answer before the next scheduled run.

## Decisions (with evidence)

- English only for factory output; Arabic excluded finally (Mohamed,
  2026-11-21). Strategic audience/market choice, not a guarantee of success.
- No technology, architecture, niche, or production style pre-chosen
  (Mohamed, 2026-11-22). OpenFilm/Remotion/Python/FFmpeg are candidates,
  not defaults.
- Zero spend is binding in this stage (Mohamed, 2026-11-22).
- Full delegation granted 2026-11-22: Mohamed gave Muse all permissions
  and all decisions for factory work. Boundaries that remain: no spending,
  no financial/legal commitments, no publishing or sharing private data, no
  irreversible changes, except on a clear assignment for each task.
- Kokoro-82M: ADOPT as the voice layer via kokoro-onnx. Apache-2.0 weights
  verified (Hugging Face API, 13.25M downloads, not gated); synthesis
  measured on this VM: 12.68 s of US-English audio in 33.8 s (RTF 2.67,
  peak RSS 665 MB), transcribed back with WER 0.000. Caveats: slower than
  real time (contradicts a secondary "6x faster" claim); naturalness still
  needs a blind listening test.
- faster-whisper: ADOPT AS-IS for captions and the verification loop,
  tiny.en by default. MIT code verified; measured tiny.en RTF 0.20,
  WER 0.000, 42/42 words timestamped, 279 MB; small.en RTF 1.06, 983 MB.
  Install recipe must pin av==12.3.0 (pip's PyAV 19.0.2 breaks decoding).
- OpenFilm: render layer PROVEN on this VM (retry passed 2026-11-22).
  Integrate conditionally as decided; always stop Studio after each
  render (2 node processes, ~216 MB, port 4747 left running otherwise).
  Peak render memory is unmeasured.
- Niche shortlist DECIDED 2026-11-22 (desk research, three cited reports):
  prototype trivia/quiz and riddles/puzzles first; did-you-know facts and
  history/science explainers second wave; word games and listicles held as
  quiz variants; motivational and storytime formats out for now. Every
  prototype must be 60+ s with narration + motion + captions, because
  TikTok Creator Rewards pays only original videos of at least 1 minute
  and excludes text-only content; originality, not production method,
  decides whether AI-made video can earn. No revenue forecast is firm —
  TikTok publishes no RPM (creator-reported $0.40–$1.00 per 1,000
  qualified views is an estimate only).

## Evidence pointers

- `audit/environment-audit-2026-11-21.md`
- `research/open-source-video-factory-2026-11-22.md`
- `factory-test-1/REPORT.md`
- `factory-test-2/REPORT.md` (motion: deterministic, no frozen segments)
- `OPERATIONS.md` (the loop), `RUNLOG.md` (run history)

## Blockers

- None open. Resolved 2026-11-22 ~11:25 UTC: the Factory Test 2 push
  landed on retry (commit e9017a06, approved during the call; verified
  by reading the remote repo — factory-test-2/ present with REPORT.md,
  render2.py, script2.json). The earlier failure was a service restart
  interrupting push-files, not a missing approval.
- None open. Resolved 2026-11-22 ~02:57 UTC: OpenFilm render test retry
  PASSED after Mohamed's explicit confirmation.
- Resolved 2026-11-22 ~02:52 UTC: Mohamed confirmed explicitly
  ("نعم، واصل رغم التحذير") to proceed past the execution-risk gate.
- Resolved earlier: GitHub App not installed on the repo (push rejected
  403) — fixed by Mohamed installing the app and selecting the repo;
  retry push succeeded and was verified.
- Watch: GitHub writes ask for approval on every call; no standing approval
  exists. Background pushes may stall on approval. To be measured by the
  test run at 03:00 UTC.

## Known limits

- Runs are periodic wake-ups, not continuous execution (see OPERATIONS.md).
- State survives only if written to the home directory or this repository.
- /tmp is not durable: it was wiped mid-run on 2026-11-22 between exec
  calls. Evidence and outputs go to ~/workspace immediately.
- A run's time budget is bounded by its schedule timeout; long work is
  split or delegated.

## Next step

1. Mohamed evaluates the two prototype videos (voice, visuals, format
   preference). Then decide the audience-test route: the TikTok account
   is managed by the other agent and Muse does not publish — publishing
   a test needs Mohamed's explicit assignment for that task.
2. If he picks am_adam, re-synthesize narration and re-render both
   videos with that voice (~2 min synthesis + ~70 s render per video).

## Next step criteria (for the prototype videos)

- Each prototype is 60+ seconds, narrated (Kokoro), with code-computed
  motion and word-timed captions — the Creator Rewards design rule.
- Every question/riddle/fact is fact-checked against a reliable source
  before rendering; sources recorded in the prototype report.
- Determinism and quality checks measured as in Test 1/2 (byte-identical
  reruns, no black/frozen frames, no silence).
- Comparison method written down before judging: metrics, baselines, and
  the threshold for a meaningful difference — not decided after seeing
  results.
