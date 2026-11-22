# Factory Test 1 — Parameterized render from data
Date: 2026-11-22 00:46 UTC
Tools used only: Python 3.12 + Pillow + ffmpeg 8.1.2 (already proven in audit). No installation, no registration, no purchase, no account change.

## What was tested
A small parameterized renderer: JSON script → 3 scenes → 720x1280 vertical video, 30 fps, 6.0 s total (3 × 2.0 s), H.264 + AAC, with a 440 Hz tone as audio placeholder.

Input: script.json (3 scenes, titles and body text, background colors, durations)
Code: render.py (Pillow draws each scene, ffmpeg assembles segments)

## Result — PASS for determinism and assembly
- ffprobe: 720x1280, 30/1 fps, duration 6.000000, nb_frames 180, codec h264
- Run A and Run B: identical SHA256 3483328e611a60e180db61780da3444222757e5300fce0fec6128e5445dc1be9
- Render time: ~4.2 s real (4.188 s, then 4.343 s on rerun)
- blackdetect: no black segments detected
- silencedetect (noise -50 dB, d 0.5 s): no silence segments detected
- Contact sheet: 6 frames at 1 fps, text legible, scene labels correct

## Failures found and fixed — documented, not hidden
1. First run: video duration 4.04 s, nb_frames 3, avg_frame_rate 75/101. Cause: concat demuxer with still PNGs treats each image as a single frame; duration is not expanded to fps.
2. Second attempt: added -framerate 30 before concat input. ffmpeg rejected it: "Option framerate not found" for concat demuxer, exit 8.
3. Fix that worked: build a real video segment per scene with `-loop 1 -t duration -i scene.png`, then concat the video segments. Result: 180 frames, 6.0 s, 30 fps.

## Honest limitation
- freezedetect flagged 0–2 s and 2–4 s as frozen. That is expected: each scene is a static slide held for 2 s. This test proves deterministic assembly and automated checking, not motion. Motion is a separate capability, not proven here.
- This does NOT prove viral content, English quality, voice quality, or audience appeal. It proves only the rendering backbone: same input → same verifiable output, with checks.

## Files
- factory-test-1-720x1280-6s.mp4 (132K, SHA256 above)
- contact-sheet.jpg
- render.py, script.json
