# Factory Test 2 — Code-computed motion, deterministic render
Date: 2026-11-22 ~07:47 UTC
Tools used only: Python 3.12 + Pillow 10.2 + numpy 1.26 + ffmpeg 8.1.2
(already proven in audit / Test 1). No installation, no registration,
no purchase, no account change.

## What was tested
Three kinds of code-computed motion inside a 720x1280, 30 fps, 6.0 s
vertical video (3 scenes x 2.0 s), each frame computed from the frame
index only — no randomness, no wall-clock input:
- Scene 1 "slide": title slides in from the left (ease-out cubic, first
  0.5 s); a dot travels left -> right; a line grows under it.
- Scene 2 "grow": a filled circle grows from the centre; a bar sweeps
  top -> bottom.
- Scene 3 "bounce": a ball bounces on two parabolas; a progress bar
  fills left -> right.

Frames are drawn with Pillow (gradient background precomputed once per
scene with numpy) and piped as raw RGB to ffmpeg (libx264, veryfast,
crf 23, yuv420p) with a 440 Hz tone as audio placeholder, same encode
settings as Test 1.

## Result — PASS
- ffprobe: 720x1280, 30/1 fps, duration 6.000000, nb_frames 180,
  codec h264 + aac, 224,436 bytes.
- Run A and Run B: identical SHA256
  `9f3d5325de8b7e76ede247dbb47d42f482d68705ce870e5cbdb0fbf28a558f90`
  (`cmp` confirms byte-identical).
- The same SHA256 was produced earlier in this run from /tmp and again
  from the workspace directory — reproducible across working directories.
- Render time: ~2.5 s from /tmp, ~5.5 s from the workspace directory
  (slower disk); both far below OpenFilm's 28–34 s for the same size.
- blackdetect (d=0.5, pix_th=0.10): no black segments.
- freezedetect (n=0.001, d=0.5): **no frozen segments** — Test 1 flagged
  0–2 s and 2–4 s as frozen (static slides). Motion is now continuous.
- silencedetect (noise -50 dB, d=0.5): no silence segments.

## Motion measured, not just claimed
- Frames sampled every 0.5 s (12 frames): mean absolute pixel
  difference vs the previous sample 0.84–43.42, all > 0.
- Scene 3 at full frame rate (60 frames, 59 consecutive pairs):
  mean|diff| min 0.06, max 0.80, mean 0.55; **0 of 59 pairs identical**.
  The 0.5 s samples in scene 3 looked nearly still (diff ~0.85) because
  the ball's bounce period is 0.5 s and sampling at the same phase
  repeats its position — a sampling artifact, not stillness; the
  consecutive-frame check above rules that out.
- Contact sheet: 4 frames (n=0, 60, 120, 179) show the three motions
  at their start/end states.

## Failure found and fixed — documented, not hidden
1. First run crashed in Python: `proc.communicate()` after an explicit
   `proc.stdin.close()` raises "ValueError: flush of closed file".
   Fix: let `communicate()` close stdin itself. No ffmpeg change needed.
2. **/tmp was wiped mid-run.** Between two exec calls the whole
   /tmp/factory-test-2 directory (runA.mp4, runB.mp4, samples, contact
   sheet) disappeared; /tmp showed 0% used. The renders were re-run from
   the workspace directory and reproduced the identical SHA256, so no
   result was lost — but this proves /tmp is not durable here.
   Fix applied: render2.py now writes into its own (workspace) directory.
   Lesson recorded in STATE.md: never treat /tmp as storage for evidence
   between steps; write outputs to ~/workspace immediately.

## Honest limitation
- This proves code-computed motion renders deterministically and passes
  automated checks. It does NOT prove motion looks good, feels natural,
  or holds attention — that needs human viewing and, later, audience data.
- Motion here is geometric (shapes, text, bars). No generated video, no
  voice, no real footage. Those are separate capabilities, not proven here.
- This does NOT prove viral content, English quality, voice quality, or
  audience appeal.

## Files
- `render2.py`, `script2.json` (pushed to repo)
- `runA.mp4` (224,436 bytes, SHA256 above) — local only, binary, not
  pushed (snapshot pushes are text-only)
- `contact-sheet.jpg` — local only, binary, not pushed
- `runB.mp4` / `output.mp4` deleted after the byte-identity check
  (identical copies of runA.mp4)

## Success criteria (set in advance, all met)
- 720x1280, 30 fps, 6.0 s, 180 frames: met.
- Byte-identical reruns: met (SHA256 match, twice, across directories).
- No black / no frozen / no silence: met.
- Motion measurable at frame level (no zero-change consecutive pairs
  in a motion scene): met (0/59 zero-change pairs).
