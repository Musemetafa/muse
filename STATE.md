# Factory State

Live operating state. Updated by every run. Last updated: 2026-11-22 ~02:30 UTC.

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
- 2026-11-22: Self-running operations designed (`OPERATIONS.md`) and goal
  `مصنع الفيديو` created as the loop's owner. Cron loop being set up.

## In progress

- **Deep inspection of OpenFilm, Kokoro-82M, faster-whisper.**
  Started 2026-11-22 ~02:30 UTC, delegated to a research worker.
  Deliverable: `research/deep-inspection-openfilm-kokoro-whisper-2026-11-22.md`.
  Must verify from primary sources: licenses (code and weights), commercial
  use in the US, real hardware needs on 1.5 CPU / 6 GiB, Kokoro US-voice
  naturalness and verified weight source, faster-whisper small/tiny memory
  fit alongside a renderer. No adoption decision yet.

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
- GitHub identity: account `Musemetafa`, linked to a different Gmail than
  Mohamed's main one; he said that is not a problem.

## Evidence pointers

- `audit/environment-audit-2026-11-21.md`
- `research/open-source-video-factory-2026-11-22.md`
- `factory-test-1/REPORT.md`
- `OPERATIONS.md` (the loop), `RUNLOG.md` (run history)

## Blockers

- None open. Previous blocker (GitHub App not installed on the repo, push
  rejected 403) was resolved by Mohamed installing the app and selecting
  the repo; the retry push succeeded and was verified.
- Watch: GitHub writes ask for approval on every call; no standing approval
  exists. Background pushes may stall on approval. To be measured by the
  test run.

## Known limits

- Runs are periodic wake-ups, not continuous execution (see OPERATIONS.md).
- State survives only if written to the home directory or this repository.
- A run's time budget is bounded by its schedule timeout; long work is
  split or delegated.

## Next step

1. Finish the deep inspection of OpenFilm, Kokoro-82M, faster-whisper;
   record a documented recommendation (adopt / modify / integrate / reject
   each, with reasons, risks, alternatives).
2. Then: Factory Test 2 — add simple code-computed motion inside a scene,
   re-measure determinism and automated checks (stated after Test 1, not
   yet executed).
3. Then: opportunity/niche discovery against the six evidence criteria,
   with experimental prototypes and comparison — no success numbers set
   before studying the data.

## Next step criteria (for the deep inspection)

- Each candidate: license verified from its primary source (code AND
  weights/models), US commercial use confirmed or flagged, hardware needs
  measured or quoted from the primary source against 1.5 CPU / 6 GiB,
  failure modes named.
- Recommendation per candidate, not a list of names.
