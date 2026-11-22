# Open-source discovery for an automated video factory
Date checked: 2026-11-22
Scope: English-only short-form vertical video, zero spending in this stage, no predetermined tech/architecture/niche. No installation, no registration, no purchase, no video produced. Hardware constraint noted, not decided: CPU-only VM, 1.5 shared CPU, 6 GB RAM, no GPU (from prior audit).

## How this was checked
- Primary sources opened directly: github.com/remotion-dev/remotion, github.com/openfilm/openfilm, github.com/scrollmark/showrunner.
- Primary sources via search-result excerpts that quote GitHub README / Hugging Face model card / license file: ManimCommunity/manim, SYSTRAN/faster-whisper, rhasspy/piper, hexgrad/Kokoro-82M, Wan-Video/Wan2.2, Lightricks/LTX-2, kandinskylab/kandinsky-6, Tencent-Hunyuan/HunyuanVideo-1.5, Comfy-Org/ComfyUI, WyattBlue/auto-editor.
- Secondary summaries are marked as such where I did not open the license file itself. No claim below should be treated as legal advice; license files must be re-read before shipping commercial work.

## Candidates (9)

### 1. OpenFilm — openfilm/openfilm
- What: A film is a folder with film.html (tracks of clips, CSS). Each shot is a web page with one function frame(t) that draws any moment; same t always draws same picture, so renders are deterministic and parallelisable. Studio is a local browser editor for hand edits. https://github.com/openfilm/openfilm
- Functions: code-driven rendering, timeline/assembly, motion graphics (CSS/SVG/canvas/WebGL/three.js/GSAP), editing.
- License: MIT for code/format/CLI/Studio (verified on GitHub page: License: MIT). Name/logo are trademarked (TRADEMARK.md). Generated voice/music/images/video require third-party services with your own keys — not self-contained.
- Runtime: Node 22.2+, ffmpeg, git (for versions), ~100 MB headless Chromium on first run. No GPU stated.
- Free operation: code free; operation free if you supply only local assets. Paid services only if you use them for voice/music/images/video.
- Maintenance: Created 2026-10-04, 8,876 stars, 899 forks, 289 commits, 18 releases (checked 2026-11-22). Very new, fast-moving.
- Limits: No built-in TTS, image/video generation, or LLM; those are connectors. Very young project — API/format may change.
- Use: As-is for rendering/editing, or modified/integrated as the render layer. Needs new components for script/voice/visuals.

### 2. Remotion — remotion-dev/remotion
- What: Make videos programmatically with React. A video is a React component tree; every frame is a pure function of frame number, screenshotted by headless Chromium and muxed by FFmpeg. Batch rendering, templates, captions, Lambda/CloudRun options. https://github.com/remotion-dev/remotion
- Functions: code-driven rendering, data-driven templates, batch rendering.
- License: NOT MIT. GitHub shows License: Other (NOASSERTION); README warns of a special license requiring a company license in some cases. Secondary sources quoting LICENSE.md: free for individuals, non-profits, and for-profits with up to 3 employees; paid Company License otherwise. From v5, telemetry/reporting and Automators tier ($0.01/render, $100/mo minimum) for hosted/automated rendering are reported. This is a load-bearing caveat — do not assume free commercial use at scale.
- Runtime: Node.js, headless Chrome/Chromium + FFmpeg. No GPU required for DOM rendering.
- Free operation: Free only within the ≤3-employee / evaluation boundary; automated/hosted factory use may trigger paid tier. Must re-check remotion.dev/docs/license before any commitment.
- Maintenance: Created 2020-06-23, 74,760 stars, 6,364 forks, 42,170 commits, 704 releases (checked 2026-11-22). Mature, heavily documented.
- Limits: React/TS only; no built-in generation, TTS, or LLM. License risk if the factory grows or is hosted.
- Use: As-is for rendering if license boundary fits; otherwise as a reference design, not as the base to fork for sale.

### 3. Showrunner — scrollmark/showrunner
- What: Open-source AI video generation framework. Pluggable formats, swappable providers, one CLI. Topic → storyboard → assets → rendered MP4; formats include faceless-explainer (Remotion) and ai-video (FFmpeg assembly); manim-explainer format exists; render→repair loop feeds render errors back to the LLM (default 2 retries); export to OTIO/FCPXML/EDL/AAF. https://github.com/scrollmark/showrunner
- Functions: orchestration across plan/assets/compose/render, TTS via Kokoro, LLM planning, captions, music ducking.
- License: MIT for Showrunner itself (verified on GitHub). Does NOT grant rights to Remotion or other providers — the Remotion obligation falls on whoever runs the render. Default format uses Remotion (see above).
- Runtime: Python 3.11+, Node.js 18+ (for Remotion), Anthropic API key required (ANTHROPIC_API_KEY). That key is a paid dependency — it breaks the zero-spend constraint unless replaced with a local/free LLM provider, which is not the default.
- Free operation: Code free; operation is NOT free as configured (Anthropic API). The ai-video/FFmpeg format avoids Remotion licensing but still needs LLM/TTS/video providers.
- Maintenance: Created 2026-03-19, 19 stars, 4 forks, 105 commits, 0 releases (checked 2026-11-22). Very small, early, single-purpose project.
- Limits: Tiny community, no releases, paid LLM by default, cloud analysis (SocialGPT) is optional but separate.
- Use: Study as an integration pattern (pluggable formats/providers, repair loop, work_dir checkpoints), or modify to swap in free/local providers. Do not adopt as-is under zero-spend.

### 4. Manim — ManimCommunity/manim (community edition)
- What: Animation engine for explanatory math videos, used for 3Blue1Brown-style precise programmatic animations. A Scene class with a construct method; renders vector shapes, graphs, text, camera moves deterministically from code. https://github.com/ManimCommunity/manim
- Functions: precise motion graphics / explanatory animation.
- License: MIT (double-licensed MIT, 3blue1brown LLC + Manim Community). Verified in search excerpts quoting GitHub.
- Runtime: Python 3.10+, FFmpeg, OpenGL, LaTeX optional. CPU rendering; no GPU required for most scenes. Needs Cairo etc. via system packages.
- Free operation: Free — code and operation are free. Cost is render time on CPU.
- Maintenance: Long-lived, community-maintained fork of 3b1b/manim; active ecosystem, Docker image available. Exact star/commit counts not re-verified in this pass — treat as secondary.
- Limits: Narrow aesthetic (diagrammatic/explanatory). No TTS, no image/video generation, no timeline editor, no vertical-video presets out of the box; vertical 720x1280 is configurable but not the default idiom. Slow for complex scenes on 1.5 CPU.
- Use: As a component for one visual style (diagrams, counters, animated text/graphs), modified/integrated. Not a whole factory.

### 5. ComfyUI — Comfy-Org/ComfyUI
- What: Node/graph/flowchart interface to design and execute diffusion pipelines (image, video, audio, 3D) locally, with a local API. Workflows are saved as JSON and are repeatable. Supports SD/SDXL/Flux, Wan and LTX-Video for video, ACE-Step for audio (per secondary summary of README).
- Functions: orchestration / generation host for open image/video models.
- License: GPL-3.0 for the core (verified in search excerpts). Models carry their own licences — ComfyUI ships no weights. GPL-3.0 affects redistribution/modification, not merely running it to produce videos, but must be read before embedding it in a product.
- Runtime: Python, GPU strongly expected for reasonable speed; large disk for models. No GPU on the target VM is the hard mismatch.
- Free operation: Code free; operation free if you run local models, but you still need GPU time somewhere — that is the real cost.
- Maintenance: Created Jan 2023, ~139,849 stars and 163 releases per secondary review (v0.42.1, 2026-10-19). Weekly releases. Very large ecosystem (800+ registry node authors).
- Limits: Learning curve, GPU-bound, model licences vary, custom nodes are third-party code.
- Use: As a host/orchestrator for open video/image models when GPU is available elsewhere; not runnable usefully on the CPU-only VM for video. Study its workflow-as-JSON pattern.

### 6. Wan 2.2 — Wan-Video/Wan2.2 (Alibaba)
- What: Open-weights text-to-video / image-to-video family. TI2V-5B is the consumer checkpoint; T2V-A14B/I2V-A14B are heavier MoE variants; S2V-14B is speech-to-video; Animate-14B for character animation. About 5 s clips at 480p/720p, no audio in 2.2.
- Functions: generative video (T2V/I2V).
- License: Apache 2.0 for code and weights (verified in secondary excerpts quoting README/model card: license apache-2.0, gated false; makers claim no rights over generated contents). Cleanest commercial licence in this set for the US.
- Runtime: Official generate.py: TI2V-5B needs at least 24 GB VRAM (e.g. RTX 4090) with offload flags; A14B needs at least 80 GB single-GPU. In ComfyUI, 5B “should fit well on 8 GB VRAM with native offloading” — still a GPU, and ~9 min for a 5 s 720p clip on a 4090 per README. Wan 2.5–3.0 are API-only, not open weights.
- Free operation: Source free; operation is NOT free on the target VM (no GPU). Renting a GPU is a paid cost.
- Maintenance: Released July 2025; ~18,804 GitHub stars per secondary summary. Still the newest downloadable Wan family.
- Limits: 5 s clips, no audio, slow, character consistency is weak in T2V (use I2V/reference for consistency).
- Use: As a generative component when GPU is available; not as-is on CPU-only VM. Its Apache-2.0 licence makes it the safest generative model to keep in view.

### 7. Kandinsky 6.0 Video — kandinskylab/kandinsky-6
- What: Family of diffusion models for synchronised text-to-audio-video and image-to-audio-video. Lite (3B) and Pro (29B) generate 5 s clips with synchronised 44 kHz audio, including lip-sync; super-resolution model upscales to 1920x1080. Available in Diffusers, ComfyUI, vLLM-Omni, SGLang, FastVideo. https://github.com/kandinskylab/kandinsky-6
- Functions: generative video + synchronised audio in one pass.
- License: MIT for code, checkpoints, and Diffusers integration (verified in search excerpts quoting GitHub/arXiv 2610.05608, 2026-10-06). No revenue cap, no region exclusions stated, no gate on download. This is the most permissive audio-video model in this set.
- Runtime: CUDA GPU required. Lite Distill: RTX 5060 Ti 16 GB (~174 s for 5 s SD) / RTX 4090 24 GB (~68 s); Pro Distill: RTX 4090 24 GB (~235 s) / H100 80 GB (~88 s) per secondary benchmark table. Python 3.13/3.14, uv, just, nvcc (SageAttention compiles on RTX).
- Free operation: Source free; operation is NOT free on CPU-only VM. Needs a GPU.
- Maintenance: Created 2026-10-05, released 2026-10-06, very new. SPEED update 2026-11-08 (+14% Pro). No long track record yet.
- Limits: 5 s clips only, slow even on GPU, very new, quality on leaderboards not yet established.
- Use: As a future generative component if GPU becomes available; its MIT licence and built-in audio make it worth tracking. Not runnable now.

### 8. Kokoro-82M TTS — hexgrad/Kokoro-82M (via Kokoro-FastAPI / kokoro-onnx)
- What: Open-weight TTS model, 82M parameters, ~330 MB weights, ~28 bundled English voices (60+ voices in some wrappers), multi-language. Served via remsky/Kokoro-FastAPI (Apache-2.0, OpenAI-compatible /v1/audio/speech) or kokoro-onnx (MIT) for CPU.
- Functions: English narration / voiceover, the factory's voice layer.
- License: Apache-2.0 for model code and weights (verified in secondary excerpts). Kokoro-FastAPI wrapper is also Apache-2.0. No seats, quotas, or usage reporting per secondary summary.
- Runtime: CPU-friendly. Minimum 2 vCPU / 2 GB RAM per Railway template summary; PyTorch CPU. On CPU, ~6x faster than real time in one hands-on test (22 s narration in 3.5 s on Apple M3 Pro, RTF ~0.16). Needs espeak-ng for phonemes; pip package ships code, not the model — download kokoro-v1.0.onnx (310 MB) + voices-v1.0.bin (27 MB) separately.
- Free operation: Free — local, offline after download, no API key, no per-character billing. This is the strongest free-operation fit in this set.
- Maintenance: hexgrad/kokoro ~7,900 stars (July 2026 secondary). Kokoro-FastAPI is actively maintained; note a Nov 2026 security-demonstration note about Hugging Face takeover was stated as no action needed — re-verify before downloading weights from any source.
- Limits: Voice quality is good but not identical to paid ElevenLabs-style voices; English voices are US/UK variants — need listening tests for US audience fit. No built-in SSML/prosody control beyond wrapper features.
- Use: As-is (or via FastAPI wrapper) as the TTS component. Deserves deeper inspection next.

### 9. faster-whisper — SYSTRAN/faster-whisper
- What: Reimplementation of OpenAI Whisper using CTranslate2. Transcription with word-level timestamps, VAD filtering, batched mode. Used for captioning, clipping (find passages), and checking rendered narration against the script. https://github.com/SYSTRAN/faster-whisper
- Functions: transcription / caption timing / quality check (transcribe the finished audio and compare to script).
- License: MIT (verified in search excerpts quoting GitHub). Whisper model weights themselves are under their own terms — check the specific model size's card before commercial use.
- Runtime: Python 3.8+, no system FFmpeg needed (PyAV bundles it). CPU with int8: small model ~995 MB RAM, 13 min audio in ~2m04s on 8-thread Xeon (README benchmark); tiny ~1 GB RAM, small ~2 GB, medium ~5 GB per secondary guide. GPU needs CUDA 12 + cuDNN 9.
- Free operation: Free — local, no API cost. Small/tiny models plausibly fit in 6 GB RAM; medium is borderline.
- Maintenance: ~26,885 stars, 2,272 forks (secondary, Nov 2026). Last release v1.2.1 from Oct 2025; repo was quiet late 2025 until Oct 2026 fixes resumed — maintenance is stop-start, not dead.
- Limits: Transcription only — no diarisation, no HTTP server, no live streaming in the core library. Accuracy needs proofreading for proper nouns (documented in other pipelines).
- Use: As-is as a component for captions and verification. Deserves deeper inspection next, alongside Kokoro.

## Also checked briefly (not in the 9)
- LTX-2.5 (Lightricks): code Apache-2.0, weights LTX-2.x Community Licence — free only under $10M annual revenue, gated download, ~66 GB download, 32 GB VRAM minimum. Audio+video in one pass, 22B. US-commercially usable under the threshold, but not MIT/Apache for weights, and GPU-bound. Not chosen for the 9 because the revenue cap + gate + GPU make it weaker than Kandinsky on licence and Wan on simplicity.
- HunyuanVideo 1.5 (Tencent): 8.3B, T2V/I2V, ~14 GB with offloading, ~75 s for a distilled 5 s clip on RTX 4090. Licence is Tencent Hunyuan Community — does NOT apply in EU/UK/South Korea; US is inside the Territory, commercial use allowed with conditions (100M MAU threshold, no training other models on outputs). GPU-bound. Not chosen because the territory carve-out and GPU need outweigh its consumer-GPU advantage.
- Piper TTS (rhasspy/piper): MIT for the original binary, voices MIT, CPU-friendly (61 MB voice, RTF ~0.066 in one test). BUT development moved to OHF-Voice/piper1-gpl (GPL-3.0) — the licence of the binary you ship must be checked. Kokoro is cleaner (Apache-2.0, more natural) and therefore preferred in this comparison.
- Auto-Editor (WyattBlue/auto-editor): Public Domain/Unlicense (with non-free elements noted in README), CLI that cuts by audio loudness / motion, exports to Premiere/Resolve/Final Cut. CPU-friendly, useful for tightening silences, but it only edits existing footage — it does not invent content. A useful utility, not a factory core.

## Comparison (summary)
| Candidate | Repeatability / determinism | Free operation on CPU-only VM | US commercial licence safety | Hardware fit (1.5 CPU / 6 GB, no GPU) | English vertical short-form |
|---|---|---|---|---|---|
| OpenFilm | High — frame(t) is pure function of t | Yes, if local assets only | High — MIT | Good — Node+Chromium+ffmpeg, no GPU stated | Yes — any size, incl. 720x1280 |
| Remotion | High — frame is pure function of number | Conditional — paid tier for automated/hosted or 4+ people | Medium — source-available, not MIT; re-check | Good — headless Chromium+ffmpeg, no GPU | Yes — any size |
| Showrunner | Medium — pipeline + repair loop, but LLM-dependent | No as configured — Anthropic API key required | Medium — MIT code, but Remotion + paid LLM | Partial — Python+Node, CPU for render, but LLM is remote | Yes — 9:16 in config |
| Manim | High — code → same animation | Yes — CPU | High — MIT | Partial — CPU, but slow on 1.5 CPU for complex scenes | Configurable, not native idiom |
| ComfyUI | High — workflow JSON is repeatable | No on this VM — GPU needed | Medium — GPL-3.0 core, model licences vary | Poor — GPU-bound | Yes, via workflows |
| Wan 2.2 | Medium — diffusion is stochastic, seed-dependent | No — GPU needed | High — Apache-2.0 | Poor — 24 GB VRAM min (official), 8 GB in ComfyUI offload | Yes — 720p, 5 s clips |
| Kandinsky 6.0 | Medium — diffusion, stochastic | No — GPU needed | High — MIT | Poor — 16 GB GPU min (offload) | Yes — 5 s clips, up to 1080p |
| Kokoro TTS | High — same text+voice → same audio (deterministic inference) | Yes — CPU, ~2 GB RAM, faster than real time | High — Apache-2.0 | Good — CPU, fits 6 GB | Yes — English voices, needs listening test |
| faster-whisper | High — same audio+model → same transcript (modulo threading) | Yes — CPU int8, small/tiny fit | High — MIT (code); check Whisper weight terms | Good — small ~1-2 GB RAM | Yes — word timestamps for captions |

## What this does NOT prove
- That any of these will produce content a US audience wants, or that any generative model will keep a character consistent across a 60 s video.
- That OpenFilm/Remotion will render fast enough on 1.5 shared CPU for daily volume — render time was not tested here (no installation, per task).
- That Kokoro's English voices sound natural enough for the target audience — that needs a listening test, not a licence check.
- That faster-whisper small/tiny will fit alongside a renderer in 6 GB RAM at the same time — memory was not tested.

## What remains unknown
- Exact current release/commit and issue counts for Manim, Wan, LTX, Hunyuan, Piper — taken from secondary summaries, not re-verified live in this pass.
- Whether OpenFilm's Chromium download and parallel rendering work on this VM's 1.5 CPU / 6 GB RAM and 512 MB /tmp — needs a read-only docs check, then a small authorised test.
- Whether Kokoro voices include a US English voice that passes a blind listening check vs. a paid reference.
- Whether the Whisper weights used by faster-whisper carry any commercial-use restriction beyond MIT code.
- How Showrunner's repair loop behaves without an Anthropic key, and whether a local LLM provider can replace it without breaking the pipeline.

## Candidates deserving deeper inspection next (no final architecture chosen)
1. OpenFilm — Reasons: MIT, deterministic frame(t), no GPU, newest code-driven renderer, Studio editor for hand fixes, format is plain HTML/folders (easy to diff/version). Risks: very young (created Oct 2026), no built-in TTS/generation/LLM, Chromium + Node 22.2+ on a small VM untested. Alternative: Remotion if the team stays ≤3 people and manual rendering, or a plain Python+Pillow+FFmpeg renderer if Chromium proves too heavy.
2. Kokoro-82M TTS — Reasons: Apache-2.0, CPU-friendly, ~82M params / ~330 MB, faster than real time on CPU, no API key, no per-use cost — the cleanest free voice layer found. Risks: voice naturalness for US audience unproven, espeak-ng setup trap, weight-download source must be verified. Alternative: Piper (MIT original, but GPL fork confusion) or a paid TTS later if listening tests fail — not now, zero-spend stage.
3. faster-whisper — Reasons: MIT, CPU int8, small/tiny models fit 6 GB, word timestamps enable captions and a verification loop (transcribe the render and compare to script). Risks: maintenance stop-start, last release Oct 2025, accuracy needs proofreading, medium model is borderline on RAM. Alternative: whisper.cpp (lighter, also CPU) if faster-whisper proves too heavy — to be checked in the same inspection, not assumed.

## Sources (checked 2026-11-22)
- https://github.com/remotion-dev/remotion
- https://github.com/openfilm/openfilm
- https://github.com/scrollmark/showrunner
- https://github.com/ManimCommunity/manim
- https://github.com/SYSTRAN/faster-whisper
- https://github.com/rhasspy/piper
- https://github.com/hexgrad/kokoro (via Kokoro-FastAPI / kokoro-onnx summaries)
- https://github.com/Wan-Video/Wan2.2
- https://github.com/Lightricks/LTX-2
- https://github.com/kandinskylab/kandinsky-6
- https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- https://github.com/Comfy-Org/ComfyUI
- https://github.com/WyattBlue/auto-editor
- https://huggingface.co/tencent/HunyuanVideo-1.5/blob/main/LICENSE
- https://ltx.io/lp/ltx-ai-video-licensing
