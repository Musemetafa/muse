# Factory Experiment Protocol — learning from the real market

**Status:** prepared 2026-11-22, **before the dedicated TikTok account arrives. No account exists yet.** Nothing in this file is a result; it is the operating protocol the factory will follow once the account exists and the first videos are published.

**Purpose:** turn the TikTok account into a learning system, not a publishing queue. Every video the factory publishes is an experiment. Every experiment must produce reusable knowledge — a finding the factory can build on — not just a video and a view count.

**Source of the comparison rules:** this protocol builds on the fair comparison method already registered in `prototype-1/REPORT.md` (metrics, thresholds, minimum window, win condition). It does not replace it. Where the two disagree, the registered method wins.

---

## 1. Principles

1. **One hypothesis, one variable.** Each experiment tests a single testable claim and isolates one variable where possible (idea, niche, hook, storytelling, visuals, motion, icons, voice, editing, caption style). If two things change at once, the result is confounded and the experiment teaches nothing.
2. **Every experiment produces knowledge.** A video that "did well" with no recorded reason is a wasted experiment. The learning record (Section 6) is the deliverable; the video is the instrument.
3. **Judge by the audience, not by taste.** Creative quality, audience response, and commercial feasibility are three separate judgements (see `STATE.md`). A video Mohamed likes that underperforms is a finding, not a failure to defend. A video he dislikes that performs is a finding, not a mistake.
4. **Honesty is a standing rule.** Monetization status is recorded truthfully from real evidence only — see Section 7. Never claim the account is monetized, never record revenue that has not actually happened, never forecast revenue as fact.
5. **The content boundaries are non-negotiable** (from `STATE.md`): no content encouraging harm or dangerous challenges; no exploitation or sexual targeting of children; no hate, racism, bullying, or deliberate humiliation; no fraud, deliberate deception, or fabricated information presented as fact; no impersonating real people or using their images/voices misleadingly or without regard for rights; no stealing others' work or republishing without rights or licence. These apply to every published video, every experiment, every variant. They do not ban fiction, comedy, or controversial topics handled responsibly.
6. **Every published video is labelled as AI-generated** where TikTok requires it: the factory's videos are AI-narrated and code-rendered. TikTok's Help Center ("About AI-generated content") requires creators to label AI-generated content containing realistic images, audio, and video; the label is applied with the in-app toggle at posting, or the `is_aigc` flag where the Content Posting API is used. No video goes out without the label.
7. **No experiment may sacrifice what already works.** See the stability rule, Section 5.

---

## 2. Hypothesis format

One experiment = one claim, written before the video is built, in this form:

```
Experiment ID:   EXP-###
Date written:    YYYY-MM-DD
Claim:           [One sentence. Testable. Falsifiable.]
                 "If we change X, then Y will happen, because Z."
Variable:        [exactly one: idea / niche / hook / storytelling /
                  visuals / motion / icons / voice / editing /
                  caption style / posting time / caption-hashtag style]
Control:         [the current best format, as published before]
Variant:         [the one thing that changes, and nothing else]
Prediction:      [the direction and the metric that will show it]
                 e.g. "comments/view will be ≥50% higher than control"
Falsifier:       [the result that would prove the claim wrong]
                 e.g. "comments/view within ±10% of control after
                       7 days and 1,000 views each"
Deciding metric: [from Section 4 — the metric that decides win/loss]
```

A hypothesis that cannot state its falsifier is not ready to run. "This will probably do well" is not a hypothesis. "A 10-second think time will raise completion by ≥5 points versus the 5-second control, because the riddle feels solvable rather than rushed" is one.

**Variable queue** (for after the first comparison — one per experiment, in no fixed order until data says otherwise):
- Hook wording (first 3 seconds): question vs statement vs challenge.
- Think time: 5 s vs 10 s (trivia already uses 5 s; riddles use 10 s — do not conflate this with the format comparison).
- Voice: af_heart (provisional) vs am_adam — pending Mohamed's listening test. Do not run this experiment until the listening test is answered; the voice choice is a judgement call, not a blind test.
- Caption style: word-by-word highlight vs whole-line captions.
- Icon density: one icon per beat vs icons only on answers.
- Question difficulty (trivia): easy vs hard mix.
- Riddle structure: 3 clues vs 1 clue.
- Posting time of day.
- Caption and hashtag style.

---

## 3. Experiment lifecycle

```
Hypothesis → Design → Build → Publish → Measure → Learn → Next hypothesis
```

| Stage | Exit criterion |
|---|---|
| **Hypothesis** | Written in the format of Section 2, with a falsifier. |
| **Design** | Control and variant are defined; exactly one variable differs; both videos follow `factory/DESIGN_RULES.md` (safe zone, subtitle band, icons, motion) and pass the automated checks. |
| **Build** | Video rendered, verified (Section: verification in `factory/REPORT.md`), byte-identical rerun confirmed, narration and captions word-timed. |
| **Publish** | Published under the publishing checklist (below). The publish date/time is recorded. |
| **Measure** | **Minimum window: 7 days AND 1,000 views each** — whichever comes later. No verdict before both conditions are met. Raw numbers are recorded verbatim with the date they were read. |
| **Learn** | Learning record written (Section 6). What changed, what the numbers say, what was learned, what changes next. |
| **Next hypothesis** | The next experiment is chosen from the result — the winner's next variable, or a new hypothesis the result suggested. Never run two variants of the same variable at once. |

**Publishing checklist** (every video, every time):
- [ ] Video ≥ 60 s, original, English, code-rendered by the factory.
- [ ] Safe-zone checker PASS on all frames (no text in the covered zones).
- [ ] AI-generated label applied (in-app toggle, or `is_aigc` via API).
- [ ] Caption written: hook first, no clickbait that the video does not deliver, no fabricated claim presented as fact.
- [ ] Hashtags: 3–5, relevant to the format, no banned/misleading tags.
- [ ] Privacy: PUBLIC. Comments: ON. Duet/stitch: per the experiment's decision, recorded.
- [ ] Cover frame chosen from inside the safe zone.
- [ ] Publish date/time recorded in the experiment log.

---

## 4. Metrics — what is recorded for every published video

Recorded per video, verbatim, with the date each number was read. Two sources: the Display API (counts) and TikTok Studio (retention — the API does not provide it; see `research/tiktok-connection-2026-11-22.md`).

| Metric | Definition | Source |
|---|---|---|
| Views | Total views at the measurement date | Display API `video/query/` or TikTok Studio |
| Completion rate | Share of viewers who watched the whole video (watched-full-video rate; average watch time ÷ duration as a cross-check) | **TikTok Studio only** — the API does not return it |
| Likes / view | like_count ÷ views | Display API / Studio |
| Comments / view | comment_count ÷ views | Display API / Studio |
| Shares / view | share_count ÷ views | Display API / Studio |
| Rewatches | Rewatch count or rate, as TikTok Studio reports it; record `N/A` if Studio does not expose it for that video | TikTok Studio |
| Follows / view | New followers attributed to the video ÷ views | TikTok Studio |

**Baselines** (from the niche discovery, `research/niche-discovery-2026-11-22.md`):
- Comments/view: **0.08%** (Revid, 176K-video sample).
- Likes/view: **7.1%** (Revid, 176K-video sample).
- Overall engagement by followers: 2.6% (Socialinsider). Use only as context — the per-view ratios above are the comparison basis.

**Pre-registered thresholds** (from `prototype-1/REPORT.md` — binding):
- A format **wins only on comments/view AND completion together**:
  - comments/view ≥ **50% relative** difference, AND
  - completion ≥ **5 percentage points absolute** difference.
- likes/view ≥ **25% relative** difference is supporting evidence, not a win on its own.
- **Rejection rule:** a format ≥ **50% below** the Revid baselines on likes/view is rejected as not viable in its current form.
- **Minimum sample:** 7 days and 1,000 views each before any judgement.
- **One video per format does not decide the format.** A win must be confirmed by a second video in the same format before the factory treats it as the new control.

**How the numbers are read:** counts (views, likes, comments, shares) come from the Display API once the connection is live, or from TikTok Studio before then. Completion rate, average watch time, watched-full-video rate, traffic sources, and follows come from TikTok Studio and are read by the person holding the account (Mohamed) and recorded into the log verbatim with the date. Until the API connection exists, all numbers are read from TikTok Studio by hand — that is legitimate and expected, not a failure of the system.

---

## 5. Stability rule — do not sacrifice what works

The factory tests improvements **without risking the audience it has already earned**.

How it works in practice:
1. **The control line keeps publishing.** Once a format has won a comparison and been confirmed by a second video, it becomes the control. The control keeps publishing on the steady cadence (Section 8) while variants are tested.
2. **One variant at a time.** At most one experimental video per week deviates from the control. The rest of the week's videos are the control format, unchanged. A variant that fails costs one video, not the week.
3. **A variant never replaces the control until it wins** on the pre-registered rule (Section 4) and is confirmed by a second video. Until then the control is the default.
4. **Kill switch:** if a variant falls ≥50% below the Revid baselines on likes/view, or its completion is ≥5 points below the control, stop testing that direction and return to the control. Do not "give it one more try" without a new hypothesis explaining why the first attempt was unfair.
5. **Never test a variant on the account's only video slot of the day if the control line is unproven.** While no format has yet won, the first comparison (Section 9) is the whole schedule — there is nothing to protect yet. The stability rule binds from the first confirmed win onward.
6. **Cadence is never sacrificed for an experiment.** If a variant is not ready, publish the control. A missed experiment is a delay; a missed day is a broken habit for the audience.

---

## 6. Learning record — the experiment log

Every experiment ends in one log entry. The log lives at `factory/EXPERIMENT_LOG.md` (created when the first experiment publishes). One entry per experiment, in this form:

```
## EXP-### — [short title] — YYYY-MM-DD (published)
Hypothesis:     [the claim, copied from Section 2]
Variable:       [the one variable]
Control:        [what the control was]
Variant:        [what changed, and nothing else]
Published:      [date and time, UTC]
Measured on:    [date the numbers were read; must be ≥7 days after publish]
Results:
  | Video   | Views | Completion | Likes/view | Comments/view | Shares/view | Rewatches | Follows/view |
  | Control |       |            |            |               |             |           |              |
  | Variant |       |            |            |               |             |           |              |
Verdict:        [won / lost / inconclusive — against the pre-registered rule]
What was learned: [one paragraph: what the numbers mean, not just what they are]
What changes next: [the next hypothesis, or the change to the control]
Monetization status at measurement: [UNKNOWN / NOT ELIGIBLE — reason /
  ELIGIBLE — NOT APPLIED / APPLIED — PENDING / ENROLLED — date /
  REJECTED — reason. See Section 7.]
```

**Rules for the log:**
- Numbers are recorded verbatim from their source, with the source named (Display API or TikTok Studio) and the read date. Never back-fill, never round away a difference, never "correct" a number to fit the hypothesis.
- Inconclusive is a valid verdict. A 7-day window with fewer than 1,000 views is inconclusive, not a loss.
- Every entry ends with "what changes next". An experiment with no next step is unfinished.
- The log is the factory's memory. When a format is changed, the log entry is the reason — not "we felt like it".

---

## 7. Honesty rules — monetization status

Standing rules, binding on every record the factory keeps:

- **Monetization status is UNKNOWN until verified with real evidence.** The only evidence that counts is what TikTok Studio → Monetization → Creator Rewards Program shows for the actual account, read by the person holding the account, with the date it was checked. Until that is read: status is **UNKNOWN**. It is never assumed, never inferred from the other agent's account, never guessed from views.
- **Allowed status values:** `UNKNOWN` · `NOT ELIGIBLE — <reason as Studio states it>` · `ELIGIBLE — NOT APPLIED` · `APPLIED — PENDING` · `ENROLLED — <date>` · `REJECTED — <reason>`. Nothing else.
- **Revenue is recorded only as TikTok Studio's own "estimated rewards" figure**, with the date it was read. No revenue is ever recorded that has not actually happened. No RPM-based revenue forecast is ever written as a fact — TikTok publishes no RPM, so none exists to cite.
- **The account's eligibility is separate from any other account's.** The other agent's monetized TikTok account is not this account. Its status says nothing about this account's status.
- **Creator Rewards eligibility (for reference, from the niche discovery):** 18+, Personal account (not Business), 10,000 followers, 100,000 views in the last 30 days, based in an eligible country with the account registered there, original videos ≥ 1 minute, ≥ 1,000 qualified For You views per video. The factory's videos are designed to meet the content side (≥ 60 s, original); the audience side (followers, views, country) is unknown until the account exists and grows.

---

## 8. Cadence — what the factory can actually sustain

Grounded in **measured** compute times on this machine (sources: `prototype-1/REPORT.md` for synthesis and captioning; `factory/REPORT.md` for v2 render times). No capacity is invented.

**Measured per 90-second video:**
| Step | Measured time |
|---|---|
| Voice synthesis (Kokoro, ~90 s narration) | **54.6–58.6 s** (RTF 0.80–1.23 per part after warmup; budget RTF 1.0 per part) |
| Captioning (faster-whisper tiny.en) | **~6 s** (model load 1.3–1.8 s + transcribe 4.5–4.6 s) |
| Render (v2, safe zone + icons) | **62.3–64.3 s** (trivia) / **73.5–82.2 s** (riddle) |
| Verification (ffprobe, black/freeze/silence detects, contact sheet) | **~1–2 min** |
| **Total machine time per video** | **~3–4 minutes, sequential** |

**Proposed cadence: 1 video per day (7 per week).**
- Why it is sustainable: 1 video is ~4 minutes of machine time; the loop wakes every 6 hours, so a day holds far more compute headroom than one video needs. The binding constraints are not compute — they are (a) the human steps that cannot be automated yet (publishing, reading TikTok Studio for retention) and (b) the need for ideas that stay fresh. One video a day is a pace a single person can sustain for the manual steps and a pace the factory can sustain for ideas.
- Why not more: publishing more than 1/day would shrink each video's measurement window (the 7-day / 1,000-view rule needs time and views per video) and would burn through the idea queue before the factory has learned what works. Volume without learning is the opposite of this protocol.
- Why not less: fewer than ~5/week makes each experiment take too long to judge and gives the audience too little to return to.
- **API caps check:** Direct Post is capped at about 15 posts/day per creator account and Upload (draft) at 5 pending shares per 24 h (see the connection research). A 1/day cadence is far below both — the caps are not binding.
- **Weekly rhythm:** publish daily; read and record numbers when each video's window closes (staggered, 7 days after its publish date); hold one learning review per week — read the log, write the next hypothesis, update the control if a variant won and was confirmed. The review is the factory's heartbeat, not a report for its own sake.

---

## 9. First experiments — the v2 prototypes as the first A/B comparison

The first comparison is already built: the two v2 prototype videos (`prototype-1/`, re-rendered with the safe-zone layout and icon system). They are the first A/B comparison, not a demo.

**EXP-001 — Trivia quiz round (control arm)**
- Video: trivia quiz round, 90.41 s, 5 fact-checked questions, 5-second think time, answer reveals, Kokoro af_heart narration (provisional voice).
- Hypothesis: *"A trivia quiz round earns more comments per view than a riddle round, because every question invites the viewer to answer in the comments — the question itself is the call to comment."*
- Deciding metric: comments/view, with completion as the joint condition (Section 4).

**EXP-002 — Riddle round (variant arm)**
- Video: riddle round, 92.29 s, 3 original riddles, "3 clues, 10 seconds", answer reveals, Kokoro af_heart narration (provisional voice).
- Hypothesis: *"A riddle round earns more shares per view than a trivia round, because a riddle is a challenge to send to a friend — 'bet you can't solve this' — while a trivia question is answered alone."*
- Deciding metric: shares/view as the supporting signal; the format still wins or loses on comments/view AND completion (Section 4). If riddles win shares but lose comments and completion, they do not win the comparison — they teach the factory that riddles are a sharing format, and the next hypothesis tests a riddle variant designed to convert sharing into commenting.

**Shared prediction (H3):** completion will be equal or higher for trivia, because its 5-second think time keeps a faster pace than the riddles' 10-second clue time. If riddles win completion instead, the factory learns that suspense holds viewers longer than pace — and the next experiment isolates think time (5 s vs 10 s) inside one format.

**What is NOT being tested yet:** voice (af_heart vs am_adam — pending the listening test), caption style, icon density, hook wording, posting time. Those wait for the comparison to report; testing them now would confound the format comparison.

**When the account arrives:** publish EXP-001 and EXP-002 on consecutive days, both under the publishing checklist, both with the AI-generated label, and measure each after 7 days and 1,000 views. The first learning review happens when both windows have closed.
