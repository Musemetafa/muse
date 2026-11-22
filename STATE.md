# Factory State

Live operating state. Updated by every run. Last updated: 2026-11-22 ~15:50 UTC.

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
- **Factory design rules — DONE, both PASS.** Built 2026-11-22 ~15:07
  UTC (`factory/`): safe-zone layout system (layout.py: TikTok template
  constants, named zones, automated checker on every frame's text
  boxes) + original code-drawn icon/micro-animation library (icons.py:
  9 icons, 5 motion primitives) + DESIGN_RULES.md. Proof: both
  prototypes re-rendered as v2 with the new system (trivia 90.41 s,
  riddle 92.29 s; checker PASS on all 2713/2769 frames, 0 failed;
  byte-identical reruns; no black/frozen/silence). The checker caught
  3 real defects eyeballing had missed (incl. a font-size-dependent
  width bug and a 6 px stack overflow). Narration reused from v1
  (af_heart provisional).
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
- **Real-market experiment system — DONE.** Built 2026-11-22 ~15:28 UTC:
  `factory/EXPERIMENTS.md` (hypothesis format with falsifier, 7-stage
  lifecycle, metrics + baselines, kill switch, honesty rules, 1
  video/day cadence) + `factory/EXPERIMENT_LOG.md` (empty, ready) +
  `research/tiktok-connection-2026-11-22.md` (legitimate connection
  options, all claims cited). Recommended path: manual publishing from
  day one; Content Posting API in Upload (draft) mode in parallel;
  Direct Post as a bonus that will likely fail TikTok's intended-use
  audit for a single-account internal tool. Analytics: Display API for
  counts; TikTok Studio, read by a human, permanently for completion
  rate, watch time, traffic, and monetization status. First
  experiments defined: EXP-001 trivia vs EXP-002 riddles.
- **Professional learning program — Module 1 DONE.** Built 2026-11-22
  ~15:34 UTC: `factory/LEARNING.md` (curriculum: honest starting
  level NONE in all 10 domains, level scale NONE → LEARNING → TESTED
  → PROVEN → RULE, 4-tier source discipline, learning loop, 10-module
  queue) + `research/tiktok-mastery-1-2026-11-22.md` (TikTok mechanics,
  discovery, SEO, policies, monetization — from TikTok's own pages,
  claims tagged official / practitioner / unproven). Key confirmed
  facts: follower count is NOT a direct For You factor; finishing a
  longer video is the strongest signal TikTok names; search value is a
  paid metric in the Creator Rewards formula. Rules adopted: completion
  stays a deciding metric, AI-generated label mandatory on every video,
  60-second minimum stands, no volume strategy.
- **Learning program — RESTRUCTURED into open discovery, DONE.**
  2026-11-22 ~15:43 UTC: `factory/LEARNING.md` revised (354 → 825
  lines): the open-ended principle at the top (listed domains are a
  floor, not a ceiling), a permanent discovery protocol (scheduled
  horizon scans after every two modules, at least monthly; triggered
  scans; cross-domain linking; unfamiliar-idea probes; re-audit
  triggers), an open revisable queue, and a discovered-domains log.
  First horizon scan: `research/discovery-scan-1-2026-11-22.md` (13
  candidates). Queue grew 10 → 17 domains/modules (D11 curiosity-gap
  & retrieval science → M3; D12 gamification & habit → M4; D13
  follow/share psychology → M9; D14 sound design & loudness → M10;
  D17 cross-platform distribution → M13; D15 community → M16; D16
  monetisation ladder → M17). New domains sit at level NONE —
  hypotheses, not knowledge.
- **Competitive-advantage discovery — DONE.** Built 2026-11-22 ~15:50
  UTC: `factory/ADVANTAGE.md` (646 lines: advantage discovered not
  copied; per-account diagnosis before any strategy; gap discovery
  method; asset vs vanity metrics; operational independence with an
  escalation table — escalate only when an action legally or
  technically requires the owner; assumption audit + weakness scan;
  benchmarking with 7 comparability rules, legitimate evidence only;
  8 named asset sacrifices; transferability of the method) +
  `factory/ACCOUNT_DIAGNOSIS.md` (198 lines, 12-section template, one
  copy per account under `accounts/<handle>/DIAGNOSIS.md`). Current
  status, stated honestly: level NONE; 0 accounts diagnosed, 0
  competitors observed, 0 benchmarks, 0 proven gaps. The Morocco
  browser-location fact is recorded in both files. Single most
  important rule: no strategy is chosen before the diagnosis, and no
  strategy transfers between accounts by assumption.

## In progress

- **TikTok account creation — BLOCKED on the country decision.**
  2026-11-22 ~15:49 UTC: the cloud browser's location was verified
  before creating the account — it appears from Fes, Morocco
  (IP 104.29.199.94, Africa/Casablanca), NOT the US, even though the
  VM's own egress shows New York. An account created in this browser
  would likely register as Morocco-based, and Morocco is not on
  TikTok's Creator Rewards eligible-country list (per current
  research), so it would likely not be eligible for Creator Rewards.
  The browser is open on the TikTok signup page with nothing entered.
  Mohamed decides: create it anyway, or pause and find a US route.
- **Mohamed's evaluation of the v2 prototypes.** He watches/listens to
  the trivia and riddle v2 videos, judges voice naturalness (af_heart
  vs am_adam), whether the icons and safe-zone layout read better, and
  which format he prefers. No loop work depends on his answer before
  the next scheduled run.

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

1. Next learning module in the loop: M2 retention science + hooks
   (factory/LEARNING.md queue, now 17 modules).
2. When Mohamed hands over the dedicated TikTok account, verify access
   and publish the v2 prototypes as the first experiments (EXP-001
   trivia vs EXP-002 riddles), by the manual path first. Record the
   monetization status truthfully from TikTok Studio — currently
   UNKNOWN, no account exists yet.
2. Mohamed evaluates the two prototype videos (voice, visuals, format
   preference). Then decide the audience-test route: the TikTok account
   is managed by the other agent and Muse does not publish — publishing
   a test needs Mohamed's explicit assignment for that task.
3. If he picks am_adam, re-synthesize narration and re-render both
   videos with that voice (~2 min synthesis + ~70 s render per video).

## Commercial discipline (standing rule, 2026-11-22)

- The dedicated TikTok account is a real commercial project: every
  decision serves building a real audience and sustainable income, not
  views alone. Experiments test ideas, niches, storytelling, visuals,
  motion, icons, voice, editing, and hooks; every experiment produces
  reusable knowledge for the next one.
- No successful style is final; keep searching for better performance
  without sacrificing the stability of what works.
- Monetization status is recorded truthfully and only from evidence.
  Current status: NO dedicated account exists yet — status UNKNOWN.
  Never claim the account is monetized and never record revenue that
  has not actually happened.
- Mohamed decides niche, style, tools, and test method no longer — the
  factory does, within the standing boundaries (zero spend, content
  boundaries, no private-data sharing, no irreversible changes except
  on a clear assignment).
- **Series/Rewards conflict (from Scan 1, practitioner-checked, to be
  re-verified against TikTok's official pages before any Series
  decision):** videos linked to a paid TikTok Series do not earn
  Creator Rewards. A future premium product must not silently
  cannibalise the main income stream.

## Professional expertise (standing rule, 2026-11-22)

- The factory has NO proven professional expertise yet in TikTok, SEO,
  audience understanding, or competitive content creation. It must not
  claim skills it has not earned, and must not manage the account on
  a strategy built from incomplete knowledge.
- First responsibility: become a professional, continuously, with no
  ceiling — TikTok mechanics/discovery/policies/monetization, TikTok
  SEO, Google SEO for video, US audience study, retention science,
  hooks of all kinds, brand/identity, storytelling and craft, and any
  further field the work reveals as necessary.
- The listed domains are a starting point, not a map and not a
  boundary. The factory's responsibility is to discover the field in
  the widest possible picture, including capabilities, techniques, and
  opportunities that never occurred to us and that we may not know
  exist. It must discover what it does not know by itself, connect
  domains, test unfamiliar ideas, and continuously re-check whether
  its current conceptions are incomplete or overtaken. No style,
  school, recipe, or ready-made strategy bounds it, and the learning
  program itself must be able to rediscover, expand, and develop
  itself.
- Source discipline: distinguish official confirmed information from
  experiments, inferences, and unproven claims; update knowledge when
  platforms change; never present an unproven claim as a rule; never
  copy a famous creator's style or follow a ready-made recipe.
- Learning and experimenting go together: do not wait for claimed
  mastery, and do not treat first experiments as proof of expertise.
  Use results to correct knowledge; turn what is learned into
  permanent factory capabilities.

## Competitive advantage (standing rule, 2026-11-22)

- The factory's job is not only to learn named fields but to
  continuously discover what neither Mohamed nor it currently knows,
  acquire it, test it, and turn it into real advantage. This ability
  itself has no knowledge or operational ceiling.
- Every account is an independent project (circumstances, history,
  audience, capabilities). Diagnose each account first; no strategy
  is assumed to transfer between accounts.
- Competition is not copying successful accounts: find unexploited
  opportunities, gaps competitors missed, and new ways to create value
  and identity that are hard to imitate.
- Views alone are not the success criterion; temporary virality is not
  building a commercial asset with an audience that remembers,
  searches for, returns to, and trusts the account.
- Operational independence: discover, prioritise, research, decide,
  execute, measure, learn, rebuild strategy without waiting for
  Mohamed. Escalate only when an action legally or technically cannot
  be completed without the account owner.
- Self-evaluation: review assumptions and find weaknesses before
  results reveal them; current tools and current thinking are never
  assumed best. Benchmark against the strongest creators and
  professional teams with comparable evidence; never claim superiority
  results do not prove.
- Protect the asset: account safety, content rights, monetization
  eligibility, audience trust — never sacrificed for short-term gain.

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
