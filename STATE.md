# Factory State

Live operating state. Updated by every run. Last updated: 2026-11-22 ~07:50 UTC.

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

## In progress

- **Opportunity/niche discovery — ready to start.** Evaluate candidate
  niches/formats against the six evidence criteria, with experimental
  prototypes and comparison. No success numbers set before studying
  the data.

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

## Evidence pointers

- `audit/environment-audit-2026-11-21.md`
- `research/open-source-video-factory-2026-11-22.md`
- `factory-test-1/REPORT.md`
- `factory-test-2/REPORT.md` (motion: deterministic, no frozen segments)
- `OPERATIONS.md` (the loop), `RUNLOG.md` (run history)

## Blockers

- **Push pending approval (2026-11-22 ~07:55 UTC).** Factory Test 2
  PASSED and is recorded locally (STATE.md, RUNLOG.md, OPERATIONS.md,
  factory-test-2/REPORT.md, render2.py, script2.json), but the snapshot
  push to Musemetafa/muse main did NOT land: the push-files call was
  interrupted by a service restart, remote head is still bfbaf20f, and
  no write approval is pending. Per the loop rules the push was not
  retried in this run. Next run: re-verify head (still bfbaf20f unless
  someone else pushed), then push the same six text files with the
  manifest at ~/workspace/.factory-test-2-push-paths.txt; update the
  sync record only after a confirmed commit SHA. Binaries
  (factory-test-2/runA.mp4, contact-sheet.jpg) are local-only and are
  never pushed (snapshot pushes are text-only).
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

1. Opportunity/niche discovery — evaluate candidate niches/formats
   against the six evidence criteria (audience demand, spreadability,
   differentiation, repeatability, production feasibility, commercial
   viability), with experimental prototypes and comparison. No success
   numbers set before studying the data. Start with desk research:
   what formats are demonstrably repeatable with the proven stack
   (deterministic render + motion + Kokoro voice + faster-whisper
   captions), then prototype the strongest 2–3.
2. Then: build the first prototype videos for the leading candidate(s)
   and define a fair comparison method before any success judgement.

## Next step criteria (for the niche discovery)

- Each candidate judged against all six evidence criteria, with cited
  primary sources for demand (not vibes or a single viral video).
- Repeatability shown concretely: at least 10 distinct video ideas per
  candidate that the proven stack could produce.
- Production feasibility tied to measured capabilities (Test 1/2 render,
  Kokoro RTF 2.67, faster-whisper RTF 0.20), not assumed tools.
- A ranked shortlist with reasons, risks, and alternatives — not a list
  of names.
