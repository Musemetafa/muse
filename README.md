# Video Factory

An advanced system being built to invent and produce English-language video
for a US audience, with the goal of earning income from TikTok. This
repository is the factory's working home: research, decisions, evidence, and
the code that has actually been tested.

## Status: discovery phase

No architecture, niche, production method, or technology stack has been
chosen yet. Nothing here is a final design. What exists so far is evidence
from audits, research, and small reversible tests.

## Fixed decisions

- **Language:** English only. Arabic is excluded from the factory's identity
  and outputs.
- **Audience:** English-speaking, with special interest in the US market.
- **Spending:** zero in this stage. No purchases, subscriptions, paid API
  keys, or paid cloud resources. Free source is not the same as free
  operation, and both are checked.
- **Boundaries:** no content that harms people, exploits children, incites
  hatred, deceives, impersonates real people, or steals others' work.

## What is in this repository

- `audit/environment-audit-2026-11-21.md` — what the current environment can
  and cannot do, proven by actual tests (CPU-only VM, no GPU, ffmpeg works).
- `research/open-source-video-factory-2026-11-22.md` — open-source discovery:
  9 candidates, licenses, hardware needs, and operating costs. The three
  most worth deeper inspection are OpenFilm, Kokoro-82M TTS, and
  faster-whisper. Remotion's license, Showrunner's paid LLM key, and the
  GPU needs of Wan 2.2, Kandinsky 6.0, and ComfyUI are documented risks.
- `factory-test-1/` — the first rendering test: a deterministic 720x1280,
  6-second video assembled from a JSON script with Python, Pillow, and
  ffmpeg, plus its report (`REPORT.md`), renderer (`render.py`), and script
  (`script.json`). It proves deterministic assembly and automated checks
  only, not motion, content quality, or audience appeal.

## How decisions are made

Evidence first: audience demand, spreadability, differentiation,
repeatability, production feasibility, and commercial feasibility. One
successful video proves nothing, and one failed experiment kills nothing.
Performance data, not personal taste, judges audience response.
