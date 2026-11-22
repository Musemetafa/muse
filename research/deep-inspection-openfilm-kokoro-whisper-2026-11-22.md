# Deep inspection: OpenFilm, Kokoro-82M TTS, faster-whisper
Date checked: 2026-11-22
Scope: the three top candidates from the open-source discovery report
(`research/open-source-video-factory-2026-11-22.md`). No spending, no paid
accounts, no paid API keys. Free downloads and installs inside the VM only.
No final factory architecture is chosen here; each candidate gets its own
recommendation.

## How evidence is labelled
- **[M]** — measured by me on this VM, 2026-11-22 (command output in hand).
- **[P]** — read by me from a primary source (project's own GitHub repo,
  LICENSE file, Hugging Face model card/API, official docs). URL given.
- **[S]** — secondary source (someone else's summary/benchmark); not
  re-verified.
- **[U]** — unknown / not verified in this inspection.

No claim in this report is legal advice. License files must be re-read
before shipping commercial work.

## Environment baseline [M]
Measured 2026-11-22 at inspection start: Ubuntu 24.04.5 LTS, 4 nominal
cores, runtime-shared limit 1.5 CPU, 7.7 GiB total RAM with **874 MiB
available** at that moment (memory pressure is real and varies),
`/home/hatch` 150 G with 149 G free, `/tmp` 512 MB (empty), no GPU.
Python 3.12.3, Node v24.22.1, npm 10.9.4, ffmpeg 8.1.2, git present.
`espeak-ng` was **not** installed at start.

Inspection footprint (all inside the VM, no spending): a Python venv at
`~/workspace/venv-inspection/` (484 MB), `~/workspace/inspection/kokoro/`
(339 MB: ONNX weights + voices + test WAVs + scripts),
`~/workspace/inspection/openfilm/` (172 MB: shallow git clone, depth 1),
`~/.cache/huggingface/` (539 MB: tiny.en + small.en Whisper models).
Total ~1.5 GB of 148 GB free. Nothing was pushed to GitHub.

---

## 1. OpenFilm — openfilm/openfilm

### License [P]
- GitHub repo header: "License: MIT License (MIT)"
  (https://github.com/openfilm/openfilm, crawled 2026-11-22 02:28 UTC).
- LICENSE file read in full from the clone: standard MIT text,
  **"Copyright (c) 2026 OpenFilm contributors"**, granting use, copy,
  modify, merge, publish, distribute, sublicense, and sell.
  (`openfilm/LICENSE` in the local clone.)
- `packages/openfilm/package.json`: `"license": "MIT"`, version **0.4.1**,
  `"engines": {"node": ">=22.2"}`.
- **Trademark is separate from the license** [P]: TRADEMARK.md says "The
  license covers the code, not the OpenFilm name and logo." A published
  fork needs its own name; the name/logo must not be used in a way that
  looks official; no implying endorsement. Practical consequence: we can
  use and modify the code freely, but the factory's product must not be
  called "OpenFilm" and must not use its logo.
- No commercial-use restriction on the code was found in the LICENSE file
  or README. US commercial use of the MIT code is permitted by the
  license text itself.

### What it is, from its own README [P]
- "The open source AI video agent: turns any coding agent into a video
  agent, with editors to change anything it makes."
- "A film is a folder with a `film.html`: tracks of clips, styled with
  CSS. Each shot is a web page whose one function, `frame(t)`, draws any
  moment … and always the same picture for the same `t`, so it renders
  the same on any machine."
- SPEC.md §3 (the one rule): "For the same `t`, `frame` MUST produce the
  same picture, whatever was drawn before it and in whatever order frames
  are requested. Hosts rely on this to scrub, to render frames in
  parallel … and to re-render one shot without the rest."
- Four editors share one library: Screening, Edit (timeline), Canvas,
  Color. Edits land in the clip's `overrides`, not in the page's code.
- Desktop app is **macOS or Windows only** ("Download it for macOS or
  Windows"). On this Ubuntu VM the usable path is the CLI/skill, not the
  desktop app.

### What it does NOT ship [P]
- README: the agent "finds footage, music and voices"; the Canvas editor:
  "Generate each with your services, then send them to the timeline."
- Release notes (v0.4): "service keys are sealed with your system's
  keychain"; connectors to Dropbox, Frame.io, Notion, Vimeo, Adobe,
  Canva; new models named (Seedance 2.5 Flash, Seedream 5.5, Doubao
  voices) are all external services.
- No bundled TTS, image/video generator, or LLM is claimed anywhere in
  the README. The desktop app includes "a built-in agent" and works with
  Claude Code/Codex — both paid/external.
- The published npm package's `files` list **excludes** `library/voices`,
  `library/audio`, `library/stickers/emoji`, `library/models`,
  `library/examples`. So even the "free music, sound effects, voices"
  mentioned in the README do not ship inside the npm package.
- Consequence: OpenFilm is a **render/edit layer only**. Voice, visuals,
  music, and planning must come from other components (which is exactly
  what Kokoro and faster-whisper are for) or from paid services.

### Hardware requirements, from its own source [P]
- Package README (line 12): "Requires Node 22.2+ and ffmpeg, on macOS,
  Windows or Linux; **the first run downloads a headless Chromium**."
  Linux is supported for the CLI. The Chromium download is a first-run
  download, not a shipped binary.
- `package.json` runtime dependencies: `playwright-core 1.61.1`,
  `@mediapipe/tasks-vision 1.2.2`, `onnxruntime-web 1.31.1`.
  `playwright-core` does **not** bundle a browser binary; a Chromium
  executable must be downloaded separately (e.g. `npx playwright install
  chromium`, ~150 MB, cached under `~/.cache/ms-playwright` in home —
  not in `/tmp`). This was verified in source text
  (`src/host.mjs`: `import { chromium } from 'playwright-core'` and
  `chromium.launch({headless: !headed, ...})`).
- **Memory design, from source** (`src/render.mjs`, `src/browser-memory.mjs`):
  - `WORKER_MEMORY = 1.5 GiB` per rendering browser; `RESERVE = 2 GiB`;
    `FRAMES_PER_WORKER = 60`; `MAX_WORKERS = 4`.
  - `defaultWorkers()` computes workers from cores and free memory and
    is clamped to at least 1. On this VM: `machine()` reports
    `cores = floor(availableParallelism()/2) = 2`, so the CPU term is
    `min(4, cores-1) = 1`. The memory term is
    `floor((available - 2 GiB) / 1.5 GiB)`, which is ≤ 0 whenever free
    memory is under 2 GiB (it was 874 MiB at inspection start) — so the
    default is **1 worker** on this VM.
  - Each browser is watched and killed past `MEMORY_MAX_MB` =
    clamp(25% of total RAM, 2–8 GB) → **2,048 MB** on this VM.
  - The code itself anticipates OOM: "ffmpeg ran out of memory with N
    browsers rendering at once: try fewer, for example --workers N/2".
  - CLI exposes `--workers <n>` explicitly (`openfilm render --workers`).
  - `openfilm doctor` exists as a diagnostics command.
- **`/tmp` (512 MB) assessment:** nothing in the render path is
  documented to use `/tmp` as scratch. The Chromium download goes to the
  Playwright cache in home; render output goes beside `film.html`
  (`<project>/<folder name>.mp4`) and ranges go to `.film/cache/render/`
  under the project. A 720x1280 render's per-frame PNGs are piped to
  ffmpeg, not staged in `/tmp` as far as the source shows. /tmp size is
  therefore **not** the binding constraint; free RAM is.
- **Plausibility verdict (not a test):** a single-worker render (1
  Chromium capped at ~2 GB + ffmpeg + Node) plausibly fits in 6 GiB,
  but only just, given this VM routinely sits under 1 GiB free. Render
  speed on 1.5 shared CPU is unmeasured and will be slow per frame for
  heavy pages (WebGL/three.js). Parallel rendering (the project's main
  speed lever) is **not** available here: the worker budget allows 1.

### Render test — NOT performed, and why [M]
- I cloned the repo (shallow, depth 1, 172 MB) and read its code and
  docs as plain text. I did **not** run `npm install`, `npx openfilm`,
  or any render.
- Reason: the clone's tool output failed an execution-risk check, and the
  standing instruction for that check is not to run, install, build, or
  test the delivered content without the user's explicit go-ahead. This
  is a **blocker to report, not a verdict on OpenFilm**: the render test
  requires the user to explicitly approve executing this project's code
  in the VM (npm install + Chromium download + `openfilm render` on a
  minimal film). Until that approval exists, the render path is
  **plausible by design, unproven by test**.
- What the test would need to settle: `openfilm doctor` output on this
  VM; first-run Chromium download size/time; a minimal 720x1280 film
  render with `--workers 1` (wall time, peak RSS, output verified by
  ffprobe + blackdetect); whether `render` first forces the Studio UI
  open (the CLI help says a project "Studio has not shown yet is opened
  in Studio first" — on a headless VM that step needs checking).

### Maintenance [P]
- Created 2026-10-04; 8,884 stars; 899 forks; 289 commits; 18 releases;
  latest release **0.4.1** (released ~Nov 18, 2026 per the releases page;
  exact date of 0.4.1 not rendered in the fetch — [U] on the precise
  date). Commits on Nov 20, 18, 17, 16, 15, 12, 9, 8, 2026: very
  active. Not archived. Very young project (7 weeks old at inspection)
  — the API/format may still change; pin to a release, do not track
  `main` blindly.

### Recommendation: INTEGRATE (conditional)
Adopt OpenFilm as the **render/edit layer**, not as a whole factory and
not as a fork: use the published `openfilm` CLI (npm) and the `film.html`
/ `frame(t)` format as-is, and build the missing layers (script, voice,
visuals, verification) around it. Reasons: MIT licence verified from the
primary source; deterministic rendering is real and is enforced by the
format spec, not just claimed; the worker/memory design explicitly
throttles to 1 browser on a small machine and exposes `--workers`;
Linux CLI is supported; the project is actively maintained. Risks: no
render test yet (blocked on approval — see above); 7 weeks old, format
may change; no built-in voice/generation/LLM, so it solves only
rendering; desktop app is macOS/Windows only; the trademark bars using
the OpenFilm name for our product. Alternatives: Remotion (mature but
not MIT — paid tier for automated/hosted use or >3 people), or the
already-proven plain Python+Pillow+FFmpeg renderer from Factory Test 1
(deterministic, zero new dependencies, but no timeline editor, no
Studio, and every effect must be hand-coded). Next step: get approval
and run the minimal render test; if it fails or is unusably slow,
fall back to the Python renderer and keep OpenFilm's format ideas.

---

## 2. Kokoro-82M TTS — hexgrad/Kokoro-82M (via kokoro-onnx)

### License [P]
- Hugging Face API metadata for `hexgrad/Kokoro-82M` (read directly
  2026-11-22): `"cardData":{"license":"apache-2.0",…}`, tags include
  `"license:apache-2.0"`. Not gated. 13,254,461 downloads.
  Last modified 2025-04-10; created 2024-12-26.
- Model card text: "With Apache-licensed weights, Kokoro can be deployed
  anywhere from production environments to personal projects." /
  "This is an Apache-licensed model, and Kokoro has been deployed in
  numerous projects and commercial APIs."
- Code repo `hexgrad/kokoro`: "License: Apache License 2.0 (Apache-2.0)",
  10,291 stars, 71 commits, 0 releases. README: `KPipeline(lang_code='a')`
  where `'a'` = American English, `'b'` = British English.
- Wrapper used here, `thewh1teagle/kokoro-onnx`: "License: MIT License
  (MIT)"; its README states exactly: "kokoro-onnx: MIT / kokoro model:
  Apache 2.0". 2,918 stars, 230 commits, 3 releases.
- No usage restriction was found on the model card or in the code README.
  Apache-2.0 permits US commercial use. No claim here is legal advice.
- Provenance note: the card lists training data including Koniwa audio
  (CC BY 3.0) and SIWIS audio (CC BY 4.0), and base model
  `yl4579/StyleTTS2-LJSpeech`. That is a training-data attribution fact,
  not a restriction on the Apache-2.0 weights — but it is worth a
  re-read before any commercial claim about the voices.

### Weight source and sizes [M + P]
- The ONNX weights do **not** live in the hexgrad repo. The hexgrad repo
  ships `kokoro-v1_0.pth` (327 MB). The ONNX export lives in
  `thewh1teagle/kokoro-onnx` releases — a different author. Verified via
  the GitHub releases API (read directly 2026-11-22), release tag
  `model-files-v1.1` (published 2025-03-01):
  - `kokoro-v1.0.onnx` — **325,505,369 bytes** (325.5 MB), full precision.
    SHA256 `beb0d1848dee9a49da392cc3df26958d46cfa35d321edf434f52949153f0df3a`
    [M, downloaded and hashed here].
  - `voices-v1.0.bin` — **28,214,398 bytes** (28.2 MB), 54 voices.
    SHA256 `bca610b8308e8d99f32e6fe4197e7ec01679264efed0cac9140fe9c29f1fbf7d`
    [M].
  - Also available: `kokoro-v1.0.fp16.onnx` 163.5 MB,
    `kokoro-v1.0.int8.onnx` 114.1 MB (quantized, smaller/faster, quality
    untested here — [U]).
- The model-card security note is worth recording [P]: "Fake websites
  like kokorottsai_com … are likely scams" and "Any website containing
  'kokoro' in its root domain … is NOT owned by and NOT affiliated with
  this model page or its author." Download weights only from the two
  sources above (huggingface.co/hexgrad/Kokoro-82M or the
  thewh1teagle GitHub releases), never from a kokoro-named website.

### Voices [P]
- `VOICES.md` (hexgrad/Kokoro-82M): "American English: 11F 9M"
  (20 voices). Female (`af_`): af_heart (**grade A**), af_alloy,
  af_aoede, af_bella (A-), af_jessica, af_kore, af_nicole (B-), af_nova,
  af_river, af_sarah, af_sky. Male (`am_`): am_adam, am_echo, am_eric,
  am_fenrir, am_liam, am_michael, am_onyx, am_puck, am_santa. Also
  British (4F 4M), Japanese, Mandarin, Spanish, French, Hindi, Italian,
  Brazilian Portuguese — 54 voices, 8 languages total.

### espeak-ng requirement [M]
- The model card and README prescribe `apt-get install espeak-ng`
  (English out-of-distribution fallback).
- I attempted the system install: `apt-get update` through the VM proxy
  was very slow (one mirror failed to fetch, lists incomplete) and the
  install took **~9 minutes** wall time, completing at 02:38 UTC:
  **espeak-ng 1.51** at `/usr/bin/espeak-ng` [M].
- **But the install proved unnecessary for this stack:** the synthesis
  test below ran and succeeded using only the pip package
  `espeakng-loader 0.2.4` (bundled with kokoro-onnx) — before the system
  install had finished. Record this: with kokoro-onnx 0.6.1, system
  espeak-ng is a fallback, not a hard requirement. (The hexgrad `kokoro`
  PyTorch path may differ — [U], not tested.)

### Synthesis test [M] — the important result
Installed in a fresh venv (`~/workspace/venv-inspection/`):
`kokoro-onnx 0.6.1`, `onnxruntime 1.32.0`, `phonemizer 3.6.0`,
`numpy 2.5.5`, `soundfile 0.14.0`, `espeakng-loader 0.2.4`.
Test script: `~/workspace/inspection/kokoro/test_synth.py`.
Test text (42 words, 225 chars, plain US English):
"Here's something most people never notice. The videos that keep you
watching until the very end all do the same thing in the first three
seconds: they promise you an answer, and they make you wait just long
enough to want it."

| Voice | Load | Synth wall | Audio | RTF | Peak RSS | Output |
|---|---|---|---|---|---|---|
| af_heart (US female, grade A) | 4.2 s (shared) | 33.8 s | 12.68 s | **2.67** | 665 MB (process peak) | 24 kHz mono WAV, 608,748 B, RMS 0.061, peak 0.47 |
| am_adam (US male) | — | 32.3 s | 11.80 s | **2.73** | 665 MB (process peak) | 24 kHz mono WAV, 566,282 B, RMS 0.097, peak 0.79 |

- **RTF ~2.7 means synthesis is 2.7x SLOWER than real time on this VM.**
  That directly contradicts the secondary claim in the discovery report
  ("~6x faster than real time", from a hands-on test on an Apple M3
  Pro). The M3 number is not wrong for its machine; it is wrong for
  this one. On 1.5 shared CPU, a 60-second narration costs ~2.7 minutes
  of synthesis. That is still usable — narration is an offline batch
  step, and 10 videos a day × 60 s ≈ 27 minutes of synthesis — but any
  plan that assumed faster-than-real-time TTS on this VM must be
  corrected. The int8/fp16 ONNX variants (114 MB / 164 MB) may be
  faster; they were not tested ([U] — worth one test, it is cheap).
- Memory is a non-issue: **665 MB peak RSS** for the whole Python
  process including the 325 MB model. It fits easily in 6 GiB, even
  alongside other components.
- Audio is real speech, not noise [M]: 24 kHz mono PCM (ffprobe);
  0.5 s-window RMS varies 0.012–0.087 (af_heart) and 0.028–0.137
  (am_adam) — speech-like dynamics with quieter windows at phrase
  boundaries. Decisively: faster-whisper transcribed the af_heart audio
  with **WER 0.000** (see §3) — the words are exactly the script, so
  pronunciation of this test sentence is correct and intelligible.

### Naturalness for a US audience — NOT settled [U]
- **I cannot hear audio, so I cannot judge whether these voices sound
  natural, pleasant, or American enough.** Saying otherwise would be
  fabrication. What exists as evidence: the model card's grades
  (af_heart = A), the perfect transcription above (intelligibility,
  not pleasantness), and 13M+ downloads (popularity, not quality).
- What would settle it: a **blind listening test** — render the same
  script with af_heart, af_bella, am_adam, am_michael and one paid
  reference voice, and have US-English listeners (or a documented
  panel) rate naturalness/accent/pleasantness without knowing which is
  which. The WAVs for that test already exist for two voices
  (`test-af_heart.wav`, `test-am_adam.wav`); the listening itself needs
  human ears, which this VM does not have.
- Also untested: prosody control (speed/pitch), SSML, long-form
  stability (does a 60 s narration drift or degrade?), and the fp16/int8
  quality/speed trade-off.

### Recommendation: ADOPT (as the voice layer, via kokoro-onnx)
Integrate `kokoro-onnx` as-is as the factory's TTS component: Apache-2.0
weights verified from the primary source, no API key, no per-use cost,
offline after a one-time 354 MB download, 665 MB peak RAM, and proven
here to produce intelligible, correctly pronounced US-English speech
(WER 0.000 on the test sentence). Reasons are measured, not assumed.
Risks: RTF ~2.7 on this VM (budget synthesis time accordingly; test
the int8 model for speed); US-voice naturalness unproven until a
listening test; weights come from a third-party ONNX export (thewh1teagle),
not from hexgrad directly — verify the SHA256 above on every fresh
download; the project is a one-maintainer wrapper around a research
model. Alternatives: Piper (MIT original, but development moved to a
GPL-3.0 fork — licence of the shipped binary must be checked; also
generally judged less natural), or a paid TTS later if listening tests
fail — not now, zero-spend stage. Next step: run the int8 speed test
and prepare the blind listening test; do not commit to a single voice
before it.

---

## 3. faster-whisper — SYSTRAN/faster-whisper

### License [P]
- Repo header: "License: MIT License (MIT)"
  (https://github.com/SYSTRAN/faster-whisper). LICENSE file read
  directly: standard MIT text (the fetch collapses the copyright line,
  so the "Copyright 2023 SYSTRAN" line itself is [U] from this fetch —
  the MIT grant text is verified).
- **Whisper model weights — a real, verified discrepancy:**
  - OpenAI's repo (https://github.com/openai/whisper), README License
    section, quoted exactly: "Whisper's code and model weights are
    released under the MIT License. See LICENSE for further details."
  - Hugging Face API metadata for `openai/whisper-small` and
    `openai/whisper-tiny` (both read directly 2026-11-22):
    `"cardData":{"license":"apache-2.0"}` and tag
    `"license:apache-2.0"`. The HF model-card prose itself states no
    license in its text.
  - So the same weights are labelled MIT on GitHub and Apache-2.0 on
    Hugging Face. **Both licences are permissive and neither source
    states any commercial-use restriction**, so this is a paperwork
    discrepancy, not a blocker — but it must be recorded, and the
    factory should pin one source (the SYSTRAN CTranslate2 models on
    the Hugging Face Hub, as used in the test below) and keep this note
    with it. If a lawyer ever asks, the answer is "both sources are
    permissive; the label differs" — not "it is MIT".
- faster-whisper needs no system FFmpeg [P]: "Unlike openai-whisper,
  FFmpeg does not need to be installed on the system. The audio is
  decoded with the Python library PyAV which bundles the FFmpeg
  libraries." Python 3.9+.

### Maintenance [P]
- Created 2023-02-11; 26,929 stars; 2,277 forks; 279 commits; 21
  releases; not archived. Latest release **v1.2.1** (version bump
  commit Oct 31, 2025 — the releases page did not render version/date
  labels in the fetch, the commit history corroborates the date).
- Commits page: latest commit **Nov 12, 2026** ("Accept one full window
  in batched transcription without VAD (#1701)"), then Nov 11, 10, 6, 2
  and Oct 16, 15, 10, 6, 5, 1, 2026 — active through November 2026
  after a quiet gap (prior commit Nov 19, 2025). Maintenance is
  stop-start but currently active; the release is ~13 months old while
  commits continue. Treat as maintained, not fast-releasing.

### README CPU benchmarks [P] (for comparison with my measurements)
Small model on CPU (8 threads, Intel Core i7-12700K), beam size 5,
13 minutes of audio: faster-whisper int8 **1m42s, 1,477 MB RAM**;
int8 batched 51 s, 3,608 MB; fp32 2m37s, 2,257 MB. No tiny-model CPU
table exists in the README — tiny-model RAM/speed figures could not be
verified from this primary source (now measured below instead).

### Transcription test [M] — the strongest result in this inspection
Installed in the same venv: `faster-whisper 1.2.1`,
`ctranslate2 4.9.0`, `huggingface-hub 2.4.0`, `tokenizers 0.23.3`.
Test script: `~/workspace/inspection/kokoro/test_whisper.py`.
Input: the Kokoro-generated `test-af_heart.wav` (12.68 s, known script,
42 words). Word error rate computed against the known script.

**Failure first (honest):** the first run crashed in audio decoding:
`TypeError: open() got an unexpected keyword argument 'metadata_errors'`
in `faster_whisper/audio.py` → `av.open(...)`. Cause: pip installed
**PyAV 19.0.2**, which removed the `metadata_errors` keyword that
faster-whisper 1.2.1 passes. Fix applied and verified: pin
**`av==12.3.0`**. This is a real dependency-fragility finding:
faster-whisper 1.2.1's declared requirement (`av>=11`) allows a PyAV
version it cannot run with. Any future install must pin `av==12.3.0`
(or re-test a newer faster-whisper). The pin is now in the venv.

| Model | Download | Load | Transcribe 12.68 s | RTF | WER (42 words) | Words timestamped | Peak RSS |
|---|---|---|---|---|---|---|---|
| tiny.en | 75 MB (HF cache) | 3.3 s | 2.5 s | **0.20** | **0.000** (0 edits) | 42/42, 6 segments | **279 MB** |
| small.en | ~464 MB (HF cache; 539 MB total cache) | 128.2 s incl. first download | 13.4 s | 1.06 | **0.000** (0 edits) | 42/42, 5 segments | **983 MB** |

- Both models transcribed the Kokoro audio **perfectly**: the transcript
  is the script word for word, language detected `en` with probability
  1.00. Sample word timestamps (tiny.en): `0.00–0.46 " Here's"`,
  `0.46–0.70 " something"`, `0.70–1.00 " most"` … all 42 words carry
  start/end times usable directly for captions.
- Caveat: this is a clean, single-speaker, studio-quiet 12.68 s sample
  with a 42-word vocabulary. WER 0.000 here proves the pipeline works
  and the Kokoro audio is intelligible; it does **not** prove WER 0.000
  on noisy, accented, or proper-noun-heavy audio. Proper nouns and
  numbers still need proofreading in production use.
- **Memory fit [M]:** tiny.en peaks at 279 MB; small.en at 983 MB.
  Either fits in 6 GiB with room to spare. Even the small model leaves
  ~5 GB headroom.
- **Fit alongside a renderer [M, by arithmetic from measured peaks]:**
  Kokoro 665 MB + faster-whisper small 983 MB + OpenFilm one worker
  (1.5 GiB budget) ≈ 3.1 GB plus OS/Node/ffmpeg overhead — fits in
  6 GiB **if run sequentially or with care**. Simultaneous peak use is
  the risk: this VM often has under 1 GiB free, so the safe design is a
  **sequential pipeline** (synthesize → verify/transcribe → render),
  not three heavy processes at once. With tiny.en instead of small.en
  the combined peak drops by ~0.7 GB.

### Recommendation: ADOPT AS-IS
Adopt faster-whisper as the factory's transcription component for two
jobs: (1) **captions** — word timestamps are exact and ready to burn
in; (2) **verification loop** — transcribe every rendered narration
and diff it against the script (WER + missing/extra words) as an
automated quality gate, exactly as demonstrated here. Default to
**tiny.en** (RTF 0.20, 279 MB, WER 0.000 on the test); use small.en
when accuracy on harder audio matters (RTF 1.06, 983 MB — still
faster than real time in wall clock only marginally, so budget it).
Reasons: MIT code verified; no commercial restriction found on the
weights (with the MIT/Apache-2.0 label discrepancy recorded above);
no API cost; no GPU; measured performance beats the README's own
benchmarks on this small sample. Risks: stop-start maintenance and a
13-month-old release (mitigated: commits are active again as of Nov
2026); the PyAV pin (`av==12.3.0`) must be recorded in every install
recipe or the decode step crashes; accuracy on proper nouns/numbers
needs proofreading; medium/large models were not tested and medium is
borderline on RAM per the README (~5 GB) — do not use them here.
Alternative: whisper.cpp (lighter, also CPU) if faster-whisper ever
proves too heavy — not needed on current evidence.

---

## 4. The three together: a measured pipeline

What was proven end-to-end on this VM, 2026-11-22 [M]:
1. Kokoro-82M (kokoro-onnx) synthesizes a 42-word US-English paragraph
   into a 24 kHz WAV in ~34 s (RTF 2.67), peak RSS 665 MB.
2. faster-whisper tiny.en transcribes that WAV in 2.5 s (RTF 0.20),
   WER 0.000 against the known script, with word timestamps for all
   42 words, peak RSS 279 MB.
3. The voice→verify loop therefore works, offline, for free, on CPU.

What was **not** proven: OpenFilm rendering (blocked on approval to
execute the cloned code — see §1); Kokoro voice naturalness (no ears
here); any video with motion; any audience response. The pipeline above
is a voice-and-verification backbone, not a factory.

Sequencing that follows from the measurements: synthesize first
(slowest step, RTF 2.7), verify with tiny.en (fastest step, RTF 0.2),
render last with OpenFilm at `--workers 1`. Do not run Kokoro,
faster-whisper small, and a Chromium render concurrently on this VM.

## 5. What remains unknown
- OpenFilm: actual render time/RAM on this VM; first-run Chromium
  download size/time; whether `render` forces the Studio UI open on a
  headless machine; behaviour under sustained memory pressure.
- Kokoro: listening-test verdict on US-voice naturalness; int8/fp16
  speed and quality; long-form (60 s+) stability and prosody; whether
  the hexgrad PyTorch path needs system espeak-ng where kokoro-onnx
  did not.
- faster-whisper: accuracy on proper nouns, numbers, and less clean
  audio; medium-model fit (not tested, README says ~5 GB — skip it).
- Whisper weights: the MIT (GitHub) vs Apache-2.0 (Hugging Face)
  licence label discrepancy is recorded, not resolved.
- None of this says anything about which video idea a US audience
  wants. That is a separate discovery task.

## 6. Recommendations (summary)

| Candidate | Recommendation | Strongest evidence |
|---|---|---|
| **OpenFilm** | **INTEGRATE (conditional)** — render/edit layer via the published CLI + `film.html`/`frame(t)` format; do not fork; do not use the OpenFilm name. Conditional on a render test that still needs user approval to run. | MIT licence verified from LICENSE file ("Copyright (c) 2026 OpenFilm contributors"); deterministic `frame(t)` enforced by the format spec; worker/memory design throttles to 1 browser on this VM (`WORKER_MEMORY` 1.5 GiB, `RESERVE` 2 GiB, per-browser cap 2,048 MB) with a `--workers` flag; Linux CLI supported; Chromium is a first-run download, not a `/tmp` problem. |
| **Kokoro-82M** | **ADOPT** — voice layer via kokoro-onnx, as-is. | Apache-2.0 weights verified via HF API (`"license":"apache-2.0"`, 13.25M downloads, not gated); ONNX weights downloaded and SHA256-verified (325.5 MB + 28.2 MB); synthesis measured here: RTF 2.67, peak RSS 665 MB; audio proven intelligible (faster-whisper WER 0.000 on the test sentence). Caveat: 2.7x slower than real time on this VM, and naturalness still needs a listening test. |
| **faster-whisper** | **ADOPT AS-IS** — captions + verification loop. Default tiny.en. | MIT code verified; no commercial restriction found on weights (MIT/Apache-2.0 label discrepancy recorded); measured here: tiny.en RTF 0.20, WER 0.000, 42/42 words timestamped, peak RSS 279 MB; small.en RTF 1.06, WER 0.000, peak RSS 983 MB. Caveat: requires pinning `av==12.3.0` (PyAV 19 breaks decoding). |

## Sources (checked 2026-11-22)
- https://github.com/openfilm/openfilm (repo page, README, releases)
- Local clone: `~/workspace/inspection/openfilm/` — `LICENSE`,
  `packages/openfilm/package.json`, `packages/openfilm/README.md`,
  `packages/openfilm/SPEC.md`, `packages/openfilm/bin/openfilm.mjs`,
  `packages/openfilm/src/render.mjs`, `src/host.mjs`,
  `src/browser-memory.mjs`, `TRADEMARK.md`
- https://huggingface.co/api/models/hexgrad/Kokoro-82M
- https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md
- https://github.com/hexgrad/kokoro
- https://github.com/thewh1teagle/kokoro-onnx
- https://api.github.com/repos/thewh1teagle/kokoro-onnx/releases
  (model-files-v1.1, 2025-03-01)
- https://github.com/SYSTRAN/faster-whisper (repo page, README, LICENSE)
- https://github.com/openai/whisper (README License section)
- https://huggingface.co/api/models/openai/whisper-small
- https://huggingface.co/api/models/openai/whisper-tiny
- Local test artefacts: `~/workspace/inspection/kokoro/test_synth.py`,
  `test_whisper.py`, `test-af_heart.wav`, `test-am_adam.wav`;
  venv `~/workspace/venv-inspection/` (kokoro-onnx 0.6.1, onnxruntime
  1.32.0, faster-whisper 1.2.1, ctranslate2 4.9.0, av 12.3.0,
  soundfile 0.14.0, phonemizer 3.6.0, numpy 2.5.5)
- System: espeak-ng 1.51 installed via apt 2026-11-22 (`/usr/bin/espeak-ng`)
