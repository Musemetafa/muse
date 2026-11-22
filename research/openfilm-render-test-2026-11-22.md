# OpenFilm render test — 2026-11-22

## Verdict: FAIL (blocked — not a technical failure of OpenFilm)

The render test could not be completed. The `npm install` step finished
successfully, but before any OpenFilm code was executed (`doctor`, Chromium
download, or `render`), the runtime raised an execution-risk check on the
tool output showing the install running, and its system notice instructs the
agent not to run, install, build, or test the cloned content and to ask the
user in plain words whether to go ahead and to wait. As a subagent I cannot
ask the user directly, so I stopped all further execution of the cloned code
and report the block here. **No render was attempted, no Chromium was
downloaded, and no OpenFilm command was executed.** Whether the render
itself would pass or fail on this VM remains unproven.

This is a block on the test procedure, not a verdict on OpenFilm. The
install succeeding is a positive signal, but it proves nothing about
rendering.

## Environment baseline (measured)

- Ubuntu 24.04.5 LTS, 4 nominal cores, runtime-shared limit 1.5 CPU,
  7.7 GiB total RAM, no GPU.
- Free RAM during the install dropped to ~300 MB (543 MB available) at one
  observation; after the install finished, 1,428 MB free / 1,872 MB
  available. Memory pressure is real and varies.
- Node v24.22.1, npm 10.9.4, ffmpeg 8.1.2, git present.
- Clone: `~/workspace/inspection/openfilm/` (shallow, depth 1, ~172 MB),
  package `openfilm` version 0.4.1, `packages/openfilm/`.
- npm cache and temp files were kept under home (`TMPDIR=~/tmp-openfilm`);
  nothing was written to `/tmp`.

## What was run

### Step 1 — `npm install` (completed, exit 0)

Command (run in `~/workspace/inspection/openfilm/packages/openfilm`):

```
export TMPDIR=~/tmp-openfilm
npm install --no-audit --no-fund
```

Measured result (from `~/workspace/inspection/openfilm-test/npm-install.log`):

- Started 2026-11-22T02:46:42Z, ended 2026-11-22T02:48:26Z.
  Wall time 1m 43.8s (user 1m 9.5s, sys 14.1s). Exit code 0.
- "added 178 packages in 2m".
- The package's `prepare` script ran `npm run build:ui` (vite build of the
  Studio UI): "vite v7.3.8 building client environment for production…
  ✓ built in 40.69s".
- Resulting sizes: `node_modules/` 347 MB; `studio/ui/dist/` 8.8 MB
  (did not exist before the install).

Pass criterion "install succeeds": **MET** (measured).

### Step 2 — execution-risk check (the block)

While the install was running, a tool result showing the install's
progress (vite build output) failed an execution-risk check. The system
notice attached to that result states, in substance: the result and any
files it delivered can run code during ordinary processing; do not run,
clone, check out, extract, unpack, apply, install, build, test, import,
load, or source its content; do not make exceptions on your own, even for
necessary steps or familiar projects; if a prohibited action is necessary,
explain that the content failed an execution-risk check and that
processing it can run code, ask the user in plain words whether to go
ahead, and wait.

Actions I took after the notice arrived:

- I attempted to stop the running install (`process.kill` on the exec
  session). The kill call itself reported an output-drain timeout, so I
  verified with `ps`: no `npm`, `node`, or `vite` processes were running.
  The install log shows the install had already exited 0 at 02:48:26Z,
  before the kill — so nothing was left to stop, and no further
  installation occurred after the notice.
- I ran no OpenFilm command. I did not run `openfilm doctor`, did not
  download Chromium, and did not render. I only read files (plain viewing)
  and checked process state.

Note on the earlier approval: the task I was given states Mohamed
explicitly approved this exact test (npm install + Chromium download +
minimal render). That approval was for the test as described. The
execution-risk notice is a separate, live safety gate that requires the
user to be asked in plain words about proceeding despite the failed
check, and to wait for the answer. I do not decide on my own that the
earlier approval covers this gate; that decision belongs to the parent
agent and to Mohamed.

### Step 3 — Chromium download: NOT DONE

Not attempted. OpenFilm's own tooling downloads `chromium-headless-shell`
(~100 MB, per its CLI message) into `~/.cache/ms-playwright` on first
run. No Chromium was downloaded in this test; nothing exists yet under
`~/.cache/ms-playwright` from this test (not verified by listing, to
avoid unnecessary reads — the download was never started, so there is
nothing of ours there).

Pass criterion "Chromium downloads": **NOT TESTED**.

### Step 4 — minimal film: written, NOT rendered

A minimal film was written by me (my own files, not cloned content) at
`~/workspace/inspection/openfilm-test/film/`:

- `film.html`: viewport `width=720, height=1280` (9:16), one section with
  one iframe clip `scenes/title.html#t=0,6`.
- `scenes/title.html`: a page exposing `window.film = { duration: 6,
  frame(t) { … } }` that draws a deterministic Canvas 2D picture purely
  as a function of `t` (gradient background shifting hue, a circle moving
  left to right, title text, a `t = …s` readout, and a progress bar).
  No external resources, no fonts to load, no audio.

The film was never rendered, so its correctness as an OpenFilm project
(valid film.html, valid page protocol) is unproven. The intended render
command was:

```
cd ~/workspace/inspection/openfilm-test/film
node ~/workspace/inspection/openfilm/packages/openfilm/bin/openfilm.mjs render --workers 1 --fps 30
```

(expected output: `film.mp4` beside film.html, 720x1280, 6 s, 30 fps).

Pass criteria "renders to a 720x1280 video with correct duration, no
black/frozen frames, render time documented": **NOT TESTED**.

## What is ready for a retry (if explicit approval is given)

- `node_modules/` installed (347 MB) and Studio UI built (8.8 MB) in
  `~/workspace/inspection/openfilm/packages/openfilm/`.
- Minimal film files written at `~/workspace/inspection/openfilm-test/film/`.
- The install log at `~/workspace/inspection/openfilm-test/npm-install.log`.
- Nothing was pushed to GitHub; nothing was bought; no paid accounts or
  API keys were used. All downloads were free (npm registry).

## Failures and fixes

- Failure 1: `/usr/bin/time` does not exist on this VM (exit 127 on the
  first attempt). Fixed by using the shell's `time` builtin and
  `date -u` timestamps instead.
- Failure 2 (the test-ending one): execution-risk check on the tool
  output, as described above. Not fixed in this run; it requires the
  user to be asked explicitly and to wait for the answer.

## Open questions for the next attempt

- Whether the render's "Studio has not shown yet" step (the CLI opens a
  never-shown project in Studio first) blocks, hangs, or proceeds on a
  headless VM. The CLI code says it carries on without Studio if opening
  fails, but this was not observed.
- Whether a single Chromium browser plus ffmpeg fits in the VM's memory
  during a 720x1280 render (free RAM was ~300–540 MB during install).
- Render wall time per frame at 30 fps on 1.5 shared CPU.

## Bottom line

- `npm install`: PASS (1m 44s, exit 0, 178 packages, UI built).
- Chromium download: NOT TESTED.
- Render: NOT TESTED.
- Overall: FAIL — blocked by the execution-risk gate before any OpenFilm
  code ran. The render question is still open, and the next step is a
  plain-words question to Mohamed about proceeding despite the failed
  execution-risk check, then waiting for his answer.


---

## RETRY — 2026-11-22 ~02:53–02:57 UTC

### Basis for proceeding

The first attempt stopped at an execution-risk gate. The parent agent
then asked Mohamed in plain words whether to run the OpenFilm commands
(Chromium download and render) despite the cloned content having failed
the execution-risk check. On 2026-11-22 02:52 UTC he answered YES:
"نعم، واصل رغم التحذير" (yes, continue despite the warning). This
retry proceeds on that explicit confirmation. It does not ask again.

Note: a second execution-risk notice arrived during this retry, attached
to the read of this report file itself. I proceeded because Mohamed's
02:52 UTC answer was given to exactly that question — whether to run
the OpenFilm commands despite the failed check — and the retry task
carries it as the gate's go-ahead. Scope was kept strictly to what he
approved: the OpenFilm CLI, the Chromium download, and the render of
the minimal film. No other cloned content was processed, nothing was
re-cloned, no new installs beyond the already-approved npm install.

### Step 1 — verify prior state (no reinstall, no re-clone)

Verified before running anything:

- `~/workspace/inspection/openfilm/packages/openfilm/node_modules/`
  347 MB present; `studio/ui/dist/` 8.8 MB present.
- Minimal film present: `~/workspace/inspection/openfilm-test/film/`
  (`film.html`, `scenes/title.html`), unchanged from the first attempt.
- No stray npm/node/vite processes running.
- Free RAM at retry start: 230 MB free / 1,070 MB available
  (memory pressure is real on this VM).

### Step 2 — CLI check (`--help`, `doctor`)

Commands (in `~/workspace/inspection/openfilm/packages/openfilm`,
`TMPDIR=~/tmp-openfilm`):

```
node bin/openfilm.mjs --help
node bin/openfilm.mjs doctor
```

- `--help` (exit 0) lists: `open`, `look`, `render [a-b]`, `get`,
  `skills`, `publish`, `update`, `doctor`. Render options include
  `--fps`, `--workers`, `--out`, `--scale`, `--alpha`.
- `doctor` (exit 0): OpenFilm 0.4.1, Node v24.22.1, ffmpeg/ffprobe
  8.1.2, network reachable. One failure: "✗ Browser — not downloaded
  yet. To fix: `openfilm open` downloads it (about 100 MB, once)."

### Step 3 — render (Chromium download + 180 frames)

Command (in `~/workspace/inspection/openfilm-test/film`,
`TMPDIR=~/tmp-openfilm`):

```
node ~/workspace/inspection/openfilm/packages/openfilm/bin/openfilm.mjs render --workers 1 --fps 30
```

First run, 2026-11-22T02:54:02Z–02:55:35Z — **exit 0, 93 s wall**:

- Studio started a local server at `http://127.0.0.1:4747/` and offered
  a browser URL. No browser was opened and no Studio interaction
  happened; the render carried on without it. (The server stayed
  running afterwards — see "Cleanup" below.)
- First run on this machine, the CLI downloaded the browser itself:
  Chrome Headless Shell 149.0.7827.55 (playwright
  chromium-headless-shell v1228), 114.2 MiB, to
  `/home/hatch/.cache/ms-playwright/chromium_headless_shell-1228`
  (262 MB on disk), plus playwright FFmpeg v1011, 2.3 MiB, to
  `/home/hatch/.cache/ms-playwright/ffmpeg-1011` (4.9 MB on disk).
- Rendered 180 frames with 1 browser: "180 frames · 6s at 30 fps ·
  720×1280 · 1 worker · libx264 · **34.1 s**".
- Output: `film.mp4` beside film.html, 397,853 bytes.

Pass criterion "Chromium downloads": **MET** (measured).

### Step 4 — verification of the output

`ffprobe` on `film.mp4`:

- codec H.264, video only (the test film has no audio track),
  720×1280, r_frame_rate 30/1, nb_frames 180, duration 6.000000,
  size 397,853 bytes. **Matches the film exactly.**

Automated checks (ffmpeg):

- `blackdetect=d=0.1:pix_th=0.10`: no black segments.
- `freezedetect=n=0.003`: no frozen segments.
- `silencedetect`: not applicable — the film has no audio track.

Visual check: a 6-frame contact sheet (1 fps) was extracted and
viewed. It shows the real picture, not a blank: title "OPENFILM /
render test", a yellow circle moving left to right, the background
hue shifting teal → purple, the `t = …s` readout advancing
(0.47s → 5.47s), and the progress bar filling. Text is legible.

Pass criteria "renders to a 720×1280 video with correct duration, no
black/frozen frames": **MET** (measured + viewed).

### Step 5 — determinism (rerun)

The render was run a second time, unchanged, 02:55:57Z–02:56:28Z:
exit 0, 31 s wall, "180 frames · 6s at 30 fps · 720×1280 · 1 worker ·
libx264 · **28.7 s**". SHA256 of both outputs is identical:

```
d22e59cae57aefc5f4912bb6ada4912049dd0bc57c7bf9480f9427e7772cd505
```

`cmp` confirms byte-identical. Determinism is proven for this film,
not just format-promised.

### Cleanup (side effect found and fixed)

The render leaves OpenFilm Studio running: two `node
studio/server/main.mjs` processes (~216 MB RSS combined) and port
4747 listening (HTTP 200) after the render finished. I stopped them
with SIGTERM and verified: no node/chrome processes remain, port 4747
closed, free RAM recovered to 558 MB / 1,160 MB available. Any future
automated use must stop Studio after rendering, or the VM leaks a
server and memory on every run.

### Failures and fixes in the retry

- Failure 1: second execution-risk notice (on the read of this report).
  Handled by proceeding on Mohamed's explicit 02:52 UTC YES, which was
  the answer to exactly that question; scope kept to the approved
  commands only. Recorded here, not hidden.
- Failure 2 (side effect, not a render failure): Studio server left
  running after render. Fixed by killing its processes and verifying
  the port closed.
- Peak memory during the render itself was not sampled; only
  before/after readings were taken (before: 152 MB free / 960 MB
  avail; after first render: 506 MB free / 947 MB avail). No OOM and
  no crash occurred, so the render fits in memory, but the exact peak
  is unmeasured.

### Footprint

- Clone + install: 527 MB (`openfilm/`), test film + logs: 884 KB,
  Playwright cache: 267 MB. Total ~795 MB of 148 GB free.
  Nothing was bought; no paid accounts or API keys were used.

## RETRY VERDICT: PASS

- Chromium download: PASS (114.2 MiB, Chrome Headless Shell
  149.0.7827.55, on disk at `~/.cache/ms-playwright/`).
- Render: PASS (720×1280, 6.000000 s, 180 frames, 30 fps, H.264,
  397,853 bytes; no black/frozen frames; contact sheet viewed).
- Render time documented: PASS (34.1 s first render, 28.7 s rerun;
  93 s wall first run including downloads, 31 s wall rerun).
- Determinism: proven (two runs byte-identical, same SHA256).
- Overall: **PASS**. OpenFilm renders on this CPU-only VM with
  `--workers 1`. Remaining cautions: Studio must be stopped after
  each render; peak render memory is unmeasured; this proves the
  render layer only — not voice, not generation, not audience appeal.
