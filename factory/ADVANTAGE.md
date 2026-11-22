# Competitive-Advantage Discovery System

**Status:** created 2026-11-22. **Level: NONE.** No TikTok account exists
yet; no competitor has been observed; no benchmark has been measured.
Nothing in this file is a proven advantage. It is the system that
*finds* advantages — and it is itself unproven until the account's own
data confirms or corrects it.

**Purpose:** give the factory a capability above the learning program.
The learning program (`factory/LEARNING.md`) teaches the factory named
fields and discovers new ones. This system does something different:
it continuously discovers what neither Mohamed nor the factory
currently knows, acquires it, tests it, and turns it into a real
advantage — an edge that is hard to imitate and that compounds into a
commercial asset. It is the difference between executing a strategy
well and discovering the strategy in the first place.

**The agent this builds:** not one that executes a fixed strategy
efficiently, but one that discovers the strategy, tests its validity,
changes it when better knowledge appears, and transfers its experience
to new accounts and circumstances without a memorized recipe. This
ability itself has no knowledge ceiling and no operational ceiling.
It is re-audited like everything else in the factory (see §9).

---

## 0. The principle — advantage is discovered, not copied

1. **A strategy is a hypothesis, not a possession.** Every strategy
   the factory holds — including the trivia-vs-riddles comparison
   already built — is a claim about *one* account, at *one* time,
   waiting for evidence. A strategy that has not been tested on the
   account it is meant for is an untested hypothesis, not a plan.
2. **Copying a winner is not an advantage.** If a format, hook, or
   style can be copied by watching one video, it is available to every
   competitor too. A real advantage is something a competitor cannot
   get by watching: a capability (a checker, a spec, a voice, a
   rendering system), a body of knowledge (what *this* audience
   responds to, measured on *this* account), or an identity (a
   promise, a ritual, a voice the audience recognises).
3. **Views are not advantage.** A video can go viral and leave nothing
   behind. Advantage is what remains after the spike: an audience that
   remembers, searches, returns, and trusts. §3 defines the metrics
   that separate the two.
4. **The method is the portable asset.** What transfers between
   accounts is how the factory finds an advantage — diagnosis, gap
   method, experiment protocol, source discipline — not the advantage
   itself. §8 states exactly what is carried over and what is
   re-discovered per account.

---

## 1. Per-account diagnosis — before any strategy is chosen

Every account handed to the factory is an independent project with its
own circumstances, history, audience, and capabilities. **No strategy
is chosen before the diagnosis, and no strategy transfers between
accounts by assumption.**

### 1.1 What the diagnosis measures

The diagnosis is recorded in a per-account file using the template
`factory/ACCOUNT_DIAGNOSIS.md` (one copy per account, e.g.
`accounts/<handle>/DIAGNOSIS.md`). It measures, in this order:

| Area | What is recorded |
|---|---|
| **Account facts** | Handle, creation date, account type (Personal / Business), country of registration, follower count, following count, video count, account age, posting history, any strikes / removals / reviews, monetization status **with evidence and the date it was read** (see `EXPERIMENTS.md` §7 — status is UNKNOWN until TikTok Studio → Monetization is read for that account). |
| **Audience** | What is known (from TikTok Studio: follower demographics, activity times, traffic sources, search queries) and what is unknown. Unknowns are written down, not guessed. For a new account the honest entry is: *audience unknown; the first videos are the measurement instrument.* |
| **Capabilities** | What the factory can produce for *this* account right now: formats built, voices available, render pipeline, checkers, audio spec, caption system. Plus what it cannot produce (see `DESIGN_RULES.md` "What the current stack cannot do"). |
| **Constraints** | Policies that bind this account (Community Guidelines version in force, Creator Rewards eligibility state, Series/Rewards conflict), and every owner-only action (see §4.3). **Country of registration is a constraint decided before creation, not after** — it determines Creator Rewards eligibility. Recorded 2026-11-22: the Muse cloud browser egresses from Fez, Morocco, not the US; creating an account from it would likely register it as Moroccan, and Morocco is not on the current Creator Rewards country list, so the account would likely not be eligible. Account creation is paused pending Mohamed's decision. |
| **Current strategy hypothesis** | One sentence, with a falsifier, in the format of `EXPERIMENTS.md` §2. For a new account the honest entry is: *no strategy yet — the first experiments are the diagnosis.* |
| **Advantage map** | Claimed advantages for this account, each with an evidence level on the LEARNING scale (NONE → LEARNING → TESTED → PROVEN → RULE). At diagnosis time the map is empty except for the *methods* (which are capabilities, not advantages). |
| **Assumption register** | Every assumption the factory is carrying into this account, its evidence, and what would falsify it (see §5.1). |
| **What we do NOT assume** | The explicit list of things the factory refuses to assume about this account (see §1.3). |

### 1.2 How the diagnosis is done — legitimate observation only

The diagnosis uses only two kinds of evidence:

1. **The account's own data.** TikTok Studio (retention, traffic,
   search queries, demographics, monetization status) read by the
   person holding the account, recorded verbatim with the read date;
   the Display API for counts, once the connection exists (see
   `research/tiktok-connection-2026-11-22.md`).
2. **Legitimate public observation.** Public videos, public profiles,
   and public pages, viewed by a human or read through TikTok's own
   tools (Creator Search Insights, Creative Center, TikTok Studio).
   Published datasets with stated methods (e.g. Revid baselines,
   Metricool's Short Video Report).

**Forbidden, always:** scraping, crawling, or automated extraction
of TikTok data; automation bots; credential-based browser automation;
cookie-based scrapers; bot-detection evasion; buying views,
followers, or engagement. TikTok's Terms of Service prohibit automated
collection and interaction without written approval, and the
Community Guidelines prohibit automation tools and fake engagement.
These are not shortcuts — they are risks to the account itself (see
§7). The connection research records the same line; this system
inherits it.

### 1.3 What is never assumed about an account

- That a strategy that worked on another account will work here.
- That the audience of a similar account is this account's audience.
- That a format's success in desk research predicts its success here.
- That followers, views, or a viral video equal an asset (§3).
- That the factory's current tools or current thinking are the best
  available (§5.3).
- That a competitor's visible numbers tell the whole story (see §6
  on incomparable numbers).

**Honest current state (2026-11-22):** no account exists, so no
diagnosis has been run. The factory's current strategy (trivia vs
riddles first) comes from desk research, not from any account's data.
That is acceptable as a *starting hypothesis* for the first account —
it is not acceptable as a strategy for any account, including the
first, until the diagnosis and the first experiments speak. The first
comparison (EXP-001/EXP-002) is therefore a learning instrument about
*this* account, not a decision imported from research.

---

## 2. Opportunity / gap discovery — a method, not a list

Competition is not copying winners. It is finding what is unexploited
and proving it is real. The method below is the factory's standing
procedure for finding gaps. It is not a list of gaps — lists go stale;
the method is what survives.

### 2.1 Where to look

| Source of gaps | What to look for |
|---|---|
| **Creator Search Insights — content gaps** | Topics people search for often that few videos cover. TikTok's own tool; the official route to demand evidence (§3.1 of Module 1). A gap flagged here has demand evidence built in. |
| **Underserved topics** | Questions, facts, or riddle types the factory's audience asks about (in comments, once they exist) that no account answers well. A comment asking a question is demand evidence from a real viewer. |
| **Formats competitors avoid** | Formats that are hard to produce (longer structured rounds, deterministic series, multi-part challenges) or that need a capability the factory has and others do not (code-rendered motion, automated checks, measured audio). Difficulty is a moat — if it is easy for everyone, it is not a gap. |
| **Identity / value angles that are hard to imitate** | A promise, a ritual, a voice, a series structure, a visual system that a competitor would have to rebuild from scratch to copy. See D7 (brand) and D13 (follow/share psychology) in `LEARNING.md`. |
| **The factory's own experiment data** | A variable that wins unexpectedly, a comment pattern that repeats, a retention curve with a shape no module predicted. The account's own data outranks every external source. |
| **Adjacent fields (horizon scans)** | Psychology, game design, education, comedy, community building — the discovery protocol in `LEARNING.md` exists for exactly this. Scan 1 already found D11–D17 this way. |
| **What the account's own comments ask for** | The comment bank (D15, M16) is the cheapest demand source the factory has — once comments exist. Before that, it is an empty source, recorded as such. |

### 2.2 How to judge whether a gap is real

A gap is **real** only when demand evidence exists. A gap with no
demand evidence is **empty** — an absence nobody wants filled — until
proven otherwise. The test, in order:

1. **Demand evidence first.** One of: a Creator Search Insights
   content-gap flag with a popularity score; repeated comments asking
   for it; search traffic on our own videos for the topic; a
   published dataset showing the demand. *No demand evidence = not a
   gap, a guess.* Record it as a guess, not a gap.
2. **Supply evidence second.** Show that few videos cover it *well*.
   "Few videos" is not enough — few videos may mean nobody wants it.
   "Few *good* videos" plus demand evidence is a gap.
3. **Fit evidence third.** Show the factory can serve it better than
   the current supply — a capability, a format, or a system the
   competitors lack. If the factory has no edge in serving it, the
   gap belongs to someone else.
4. **Falsifier, stated in advance.** What result would prove the gap
   is empty? (e.g. "a video on this topic earns <50% of the control's
   views after 7 days and 1,000 views" — then the gap is dropped, not
   re-tested without a new reason.)
5. **Probe, don't commit.** A gap is tested with one probe under the
   experiment protocol (one variable, 7 days + 1,000 views, win only
   on comments/view AND completion together). A probe that wins is
   promoted to a strategy candidate; a probe that loses is recorded
   and dropped. The stability rule applies: the control line keeps
   publishing while the gap is probed.

**What is NOT gap discovery:** watching a successful account and
copying its format, its hook, or its style. That is imitation, and
imitation is available to every competitor. Studying a successful
account's *mechanics* (why a structure works) is research; copying
its *surface* (what it looks like) is the opposite of this system.
The source discipline in `LEARNING.md` applies: a module may analyse
a format's mechanics; it may not prescribe imitating a specific
creator.

---

## 3. Advantage criteria — asset-building vs view-chasing

### 3.1 What counts as a real advantage

A real advantage has three properties, all three:

1. **Hard to imitate.** A competitor cannot get it by watching one
   video. It is a capability (a checker, a spec, a rendering system,
   a voice), a body of measured knowledge about *this* audience, or
   an identity (a promise, a ritual, a voice the audience
   recognises).
2. **Compounding.** It makes the next video easier to make, easier to
   find, or more valuable than the last one — a format library, a
   search-topic queue, a comment bank, a returning audience.
3. **Audience-side.** It shows up in the audience's behaviour, not in
   the factory's opinion of its own work: viewers remember the
   account, search for it, return to it, and trust it.

### 3.2 Metrics that separate asset-building from view-chasing

| Asset metrics (what advantage looks like) | Vanity metrics (what it does not look like) |
|---|---|
| **Follows / view** — viewers who convert a watch into a follow. The single best proxy for "remembered". | Raw views on one video, with no follow, comment, or return attached. |
| **Return viewers** — share of views from followers / returning viewers in TikTok Studio. | A spike driven by one video's For You push, with no change in the follower base. |
| **Search-driven views** — views arriving from search, and search queries naming the account or its topics (TikTok Studio search analytics). Search value is a paid metric under Creator Rewards. | Views that arrive only from the For You feed and stop when the push stops. |
| **Comments / view with substance** — comments that answer, argue, ask, or challenge (the experiment protocol's deciding metric, jointly with completion). | Comment counts inflated by generic replies, or comments the factory solicited without a real question behind them. |
| **Shares / view** — viewers who send the video to someone ("bet you can't solve this"). A share is a vote of identity, not just attention. | Likes alone. A like is the cheapest signal a viewer can give. |
| **Completion rate, sustained across videos** — the deciding metric, measured per video and as a trend, not as a single best video. | One video's high completion that never repeats. |
| **Trust signals** — corrections accepted gracefully, no strikes, no removals, comments that defend the account's accuracy, viewers who cite the account to others. | Growth bought, gamed, or borrowed from a misleading hook. |

**The rule:** a format or tactic is an advantage only when it moves
an asset metric *repeatedly* — across at least two videos, measured
after the 7-day / 1,000-view window, against the pre-registered
thresholds in `EXPERIMENTS.md` §4. One viral video is a data point,
not an advantage. A format that wins views and loses follows is a
liability wearing a success costume.

### 3.3 The four audience tests

An advantage must pass all four, stated as questions the factory
asks about its own account:

1. **Remember:** does the viewer remember the account's name, promise,
   or ritual a day later — or only the video?
2. **Search:** does the viewer search for the account or its topics
   (branded search, topic search), or only stumble on it?
3. **Return:** does the viewer come back tomorrow — for the next
   round, the streak, the ritual — or watch once and leave?
4. **Trust:** does the viewer believe the account's answers, defend
   its accuracy, and accept its corrections — or treat it as
   entertainment with no credibility?

A tactic that fails any of the four is not an advantage, however many
views it earns. The four tests are recorded in each account's
diagnosis file, with the evidence for each.

---

## 4. Operational independence — the full loop, run without waiting

### 4.1 The loop

```
Discover → Prioritize → Research → Decide → Execute → Measure
  → Learn → Rebuild strategy → (back to Discover)
```

This loop is the factory's operating loop (`OPERATIONS.md`), extended
with a discovery front-end and a strategy-rebuild step. It runs
without waiting for Mohamed and without depending on him for daily
decisions or tasks. The loop's cadence is the loop's cadence: a run
every 6 hours, one step per run minimum, state written to the
repository so the next run resumes from evidence, not from memory.

| Stage | What happens | Who decides |
|---|---|---|
| **Discover** | Horizon scan, gap method (§2), assumption audit (§5.1), weakness scan (§5.2), competitor observation (§6). Produces candidates, not decisions. | The factory, by the discovery protocol in `LEARNING.md`. |
| **Prioritize** | Candidates are ranked (see §4.2). The ranking is written down with its reasons, so a later run can challenge it. | The factory. |
| **Research** | The top candidate is studied under the source discipline (official / data / practitioner / unproven). A module report or a desk probe is the output. | The factory. |
| **Decide** | The candidate becomes a hypothesis with a falsifier (`EXPERIMENTS.md` §2) — or is dropped, with the reason recorded. | The factory. |
| **Execute** | The video is built, verified, and published under the publishing checklist. | The factory builds; the owner publishes (see §4.3 — the publishing tap is an owner action until the API path changes it). |
| **Measure** | Numbers recorded verbatim with source and read date, after the 7-day / 1,000-view window. | The factory records; the owner reads TikTok Studio (the API does not return completion). |
| **Learn** | The experiment log entry: verdict, what was learned, what changes next. | The factory. |
| **Rebuild strategy** | If the result contradicts the strategy, the strategy changes — the knowledge is wrong, not the result. The change is recorded in the account's diagnosis file with its evidence. | The factory. |

### 4.2 Prioritization — how the factory chooses what to do next

Candidates are ranked on four factors, each scored honestly (no
invented precision — high / medium / low is enough):

1. **Impact on an asset metric** (§3.2). Does it move follows/view,
   return viewers, search traffic, or trust — or only raw views?
2. **Evidence strength.** Official or own-data evidence outranks
   practitioner claims; practitioner claims outrank guesses. A
   candidate with no evidence is a probe, not a priority.
3. **Cost.** Machine time (measured: ~3–4 minutes per 90-second
   video), human steps (publishing, Studio reads), and idea
   consumption. A candidate that burns the idea queue without
   learning is expensive even if the machine time is small.
4. **Reversibility.** A probe that can be dropped after one video
   outranks a commitment that changes the account's identity,
   format, or monetization position. Irreversible or hard-to-reverse
   changes are never prioritised without an explicit decision and a
   recorded reason.

**What is never prioritised:** a tactic whose only evidence is that
a famous creator does it; a format copied from a competitor; a
volume increase without a learning reason (the no-volume-strategy
rule from Module 1); anything that trades asset protection for a
short-term gain (§7).

### 4.3 Escalation — only when the owner is legally or technically required

The factory does not turn obstacles into questions for Mohamed. It
searches for solutions and alternatives itself. Escalation happens
**only** when an action legally or technically cannot be completed
without the account owner.

| ESCALATES — owner action required | NEVER ESCALATES — factory decides alone |
|---|---|
| Account registration (creating the TikTok account). | Research, reading, and module reports. |
| Authorization / OAuth consent (Login Kit, API scopes, developer-app registration and review submissions). | Hypothesis writing, falsifiers, experiment design, variable choice. |
| Publishing taps (posting a video in the app or TikTok Studio; finishing an API-uploaded draft). Until the Direct Post path is approved — which the connection research says is unlikely for a single-account internal tool — every publish is a human tap. | Production: rendering, verification, captions, icons, audio, safe-zone checks. |
| Monetization application (Creator Rewards application, Series setup, LIVE / Subscription enrolment). | Strategy changes within the standing boundaries, including dropping a losing format and promoting a winning one. |
| Any payment, subscription, or financial commitment. | Measurement, log entries, learning reviews, benchmark comparisons. |
| Any use of Mohamed's private data, or any sharing of private data. | Learning-module order, horizon-scan targets, probe design, prioritization. |
| Any irreversible change (account deletion, username change, Series pricing once set, linking free episodes into a Series). | Re-auditing its own assumptions and demoting its own knowledge levels. |
| A strike, removal, or review that needs an appeal — the appeal text is drafted by the factory, but submission is the owner's decision and action. | Choosing which gap to probe next, and which hypothesis to test. |

**The test for escalation:** "Can this be completed without the
account owner, legally and technically, within the standing
boundaries?" If yes, the factory does it. If no, it prepares
everything the owner needs (the exact text, the exact steps, the
exact decision) and asks once, with the work already done — not with
a question that transfers the work to Mohamed.

---

## 5. Self-evaluation — finding weaknesses before results do

### 5.1 Assumption audit — the register

Every strategy the factory holds rests on assumptions. The audit
makes them visible, then tests them. The register lives in each
account's diagnosis file, in this form:

```
Assumption:   [one sentence — what the factory believes]
Evidence:     [official / data / practitioner / own result / none — with source and date]
Falsifier:    [the result that would prove it wrong]
Last checked: [date]
Status:       [held / corrected / dropped]
```

**Rules:**
- An assumption with no evidence is labelled as such. It is not
  treated as knowledge because it feels true.
- The register is audited at every learning review (weekly, per
  `EXPERIMENTS.md` §8) and at every horizon scan. An audit that
  finds nothing to correct is a suspicion, not a success — it means
  the audit was not looking hard enough.
- A correction is progress, not failure. A demotion of a knowledge
  level is recorded with the trigger and what replaces the old
  knowledge (the same rule as `LEARNING.md` §d).

**Current assumptions the factory is carrying (2026-11-22, to be
audited, not believed):**
- Trivia earns more comments/view than riddles; riddles earn more
  shares/view. (Evidence: none yet — it is EXP-001/EXP-002's
  hypothesis. Falsifier: the comparison's pre-registered thresholds.)
- A 5-second think time beats a 10-second think time on completion.
  (Evidence: none — H3 prediction. Falsifier: riddles winning
  completion.)
- The three-layer SEO practice (caption + on-screen + spoken topic
  phrase) improves search discovery. (Evidence: practitioner only.
  Falsifier: no search-traffic difference in a controlled test.)
- One video per day is the right cadence. (Evidence: measured compute
  times + the no-volume rule. Falsifier: the account's own data
  showing a different cadence earns more per video.)
- The factory's current renderer and voice are good enough to compete.
  (Evidence: none about competitiveness — only that they render.
  Falsifier: benchmark comparison showing a systematic gap.)

### 5.2 Weakness scan — red-teaming the factory

Before results expose a weakness, the factory looks for it itself.
Four standing practices, run at every learning review:

1. **Red-team the video.** Watch the factory's own video as a
   stranger would: first 3 seconds, then the middle, then the end.
   Write down every second you would swipe, every line that reads as
   translated, every motion element that is decoration, every moment
   the audio feels flat. A video that survives its own red-team is
   the minimum standard for publishing — a video the factory cannot
   criticise is a video it has not looked at.
2. **Compare against stronger creators.** Take the strongest
   quiz/riddle accounts the factory can observe legitimately (§6) and
   ask, for each: what do they do that we do not? What do they do
   that we should not? What do we do that they cannot? The third
   question is the advantage question; the first two are the weakness
   questions. Record the answers, not the feelings.
3. **Audit the tools and the methods.** Each tool and each method gets
   a periodic review: is there a better renderer, a better voice, a
   better sourcing route, a better measurement routine? The review
   uses the same evidence standard as a module (official / data /
   practitioner / own result). **Standing rule: the current tools and
   the current thinking are never assumed best.** A tool is kept
   because the evidence keeps it, not because it was chosen first.
   (Scan 1, C12, already lists the renderer candidates to re-check;
   the voice decision is still provisional.)
4. **Audit the strategy's blind spots.** Ask what the current strategy
   cannot see: which audience is it ignoring, which surface is it
   not using (Search? Following? LIVE?), which monetization rung is
   it not building toward, which failure mode has it never tested?
   The discovery backlog in `LEARNING.md` is the standing list of
   known blind spots; the audit's job is to find the unknown ones.

### 5.3 The standard — compete with the strongest, not the nearest

The factory's benchmark is the strongest creators and professional
teams in its field, not the average account and not its own past
performance. Competing with the strongest is a discipline, not a
claim: it means measuring against them (§6), learning what they do
that the factory cannot yet do, and searching continuously for how to
exceed their level. **Never claim superiority the results do not
prove.** A claim of being better than a named creator or team
requires comparable, measured evidence — and until the factory has
it, the honest statement is: *we do not yet know how we compare.*

---

## 6. Benchmarking — measuring against the strongest, honestly

### 6.1 What may be used

Only legitimate, comparable evidence:

| Source | What it gives | Limits |
|---|---|---|
| **Public videos (viewed, not scraped)** | Visible counts: views, likes, comments, shares, reposts; format, length, hook, caption style, posting cadence. | No completion rate, no retention curve, no traffic source, no follower demographics. Never guess these for a competitor. |
| **TikTok's own tools** | Creator Search Insights (demand, content gaps); Creative Center (trending, keyword insights); TikTok Studio (own account only). | Studio shows only the factory's own account. Insights show demand, not a competitor's performance. |
| **Published datasets** | Revid baselines (comments/view 0.08%, likes/view 7.1%, 176K-video sample); Metricool Short Video Report 2026 (6M+ videos); Socialinsider engagement by followers (2.6%). | Vendor datasets, not peer-reviewed; samples differ; treat as a floor, not a target. |
| **The factory's own account data** | Completion, retention, traffic, search queries, follows/view, return viewers. | Only its own account. Never used to infer a competitor's numbers. |

### 6.2 Comparability rules — how to avoid fooling yourself

1. **Same format.** Compare quiz rounds with quiz rounds, riddles
   with riddles. A riddle's shares/view against a dance video's
   likes/view is not a comparison.
2. **Same video age.** Compare videos measured at the same age (e.g.
   7 days after publish). A 30-day-old video's views against a
   1-day-old video's views is not a comparison.
3. **Same audience-size band.** A 1,000-follower account's per-view
   ratios against a 1M-follower account's are not the same
   measurement — the audiences differ. Compare within a band, and
   record the band.
4. **Per-view ratios, not raw counts.** Comments/view, likes/view,
   shares/view, follows/view. Raw counts favour whoever has more
   followers — and follower count is not a direct For You factor
   (Module 1), so raw counts mostly measure audience size, not
   quality.
5. **Medians, not peaks.** Compare the median of a competitor's last
   10–20 videos in the format, not their best video. A peak is a
   lottery ticket; a median is a capability.
6. **Never guess what cannot be seen.** A competitor's completion
   rate, retention curve, and search traffic are invisible. Do not
   estimate them, do not infer them from views, do not present them
   as numbers. Record them as unknown.
7. **Report the gap honestly.** The benchmark record states the
   factory's number, the comparator's number, the method, and the
   gap — including when the gap is against the factory. A benchmark
   that only ever flatters is not a measurement.

### 6.3 The benchmark record

Kept in each account's diagnosis file, one row per comparator:

```
Comparator:   [account or dataset — public handle, or dataset name]
Format:       [the format compared]
Videos used:  [count, date range, median age at measurement]
Metric:       [comments/view | likes/view | shares/view | follows/view]
Comparator:   [median value, with source and date]
Factory:      [median value, with source and date]
Gap:          [difference, direction, and what it would take to close it]
```

**Honest current state (2026-11-22):** no benchmark exists. No
competitor has been observed (Scan 1, gap 5: no systematic viewing or
measurement of quiz/riddle accounts was possible without TikTok
contact, which the limits forbid). The Revid baselines are the only
comparators on record, and they are a floor for the whole platform,
not a bar for the strongest quiz accounts. The first benchmark is
built when the account exists and legitimate public observation
becomes possible — and it is built from medians, not from one viral
video.

---

## 7. Asset protection — a hard constraint, never a trade

Account safety, content rights, monetization eligibility, and
audience trust are **never traded for a short-term gain**. A tactic
that earns views and costs standing is a loss, recorded as a loss.
This is not a preference; it is a constraint on every decision in
this system, in the experiment protocol, and in the learning program.

### 7.1 What counts as a sacrifice

Any of these is a sacrifice of the asset, however many views it
earns:

- **A misleading hook** — a promise the video does not deliver
  (clickbait). It trades trust for a swipe-stop, and the viewers it
  keeps are the ones who leave angriest.
- **Engagement bait** — asking for likes, comments, or follows
  without a real question or reason behind the ask. It inflates a
  metric and degrades the comment quality the factory is trying to
  build.
- **Bought or gamed engagement** — buying views, followers, likes,
  or comments; follow/like/comment bots; engagement panels. Banned
  by the Community Guidelines and by the Creator Rewards rules;
  artificial activity can remove an account from the program.
- **Unlicensed or mis-licensed assets** — a music track or SFX file
  whose licence does not cover commercial use in monetised content,
  or a CC-BY file used without attribution logged. A licence
  violation on a monetised video is an account-standing event, not
  a paperwork error (see D14 / C6 in `LEARNING.md`).
- **Copied work** — another creator's questions, scripts, format,
  or style reproduced without rights or licence. The factory writes
  every question and riddle itself and draws every icon in code for
  exactly this reason.
- **A Series link without a decision** — linking a free episode into
  a paid Series without an explicit decision weighing the lost
  Creator Rewards income (LEARNING.md rule 7). The loss is silent
  and permanent per video.
- **A misleading AI label** — labelling unaltered content as
  AI-generated, or failing to label AI-generated content TikTok
  requires labelled. Both are violations (Module 1, §5.2).
- **Any of the six standing content boundaries** (from `STATE.md`,
  binding on every video): no content encouraging harm or dangerous
  challenges; no exploitation or sexual targeting of children; no
  hate, racism, bullying, or deliberate humiliation; no fraud,
  deliberate deception, or fabricated information presented as fact;
  no impersonating real people or using their images/voices
  misleadingly or without regard for rights; no stealing others'
  work. These do not ban fiction, comedy, or controversial topics
  handled responsibly — they ban trading safety, credibility, and
  rights for views.

### 7.2 The check

Before any tactic is adopted, it passes one question: *"If every
competitor did this, and TikTok enforced its own rules on it, would
the account still be standing, eligible, and trusted?"* If the
answer is no, the tactic is not adopted. If the answer is uncertain,
the tactic is probed only in a form that cannot damage the account
(one video, reversible, no policy risk) — and the uncertainty is
recorded.

---

## 8. Transferability — what moves to a new account, and what does not

The factory will, in time, work on more than one account. The
experience must transfer — but a strategy must not transfer by
assumption. The portable asset is the discovery method.

### 8.1 Carried over (the method)

| Carried over | Form |
|---|---|
| The diagnosis template and method (§1) | `factory/ACCOUNT_DIAGNOSIS.md` |
| The gap method (§2) | This file, §2 |
| The experiment protocol and its thresholds | `factory/EXPERIMENTS.md` |
| The source discipline and level scale | `factory/LEARNING.md` |
| The discovery protocol and horizon scans | `factory/LEARNING.md` |
| The checkers and specs (safe zone, audio spec, icon library) | `factory/layout.py`, `factory/icons.py`, audio spec (D14) |
| The failure record | `factory/EXPERIMENT_LOG.md` — what did not work, and why. Failures transfer; they are the cheapest knowledge the factory owns. |
| The assumption-audit and weakness-scan routines | This file, §5 |
| The benchmark method and comparability rules | This file, §6 |

### 8.2 Re-discovered per account (the conclusions)

| Re-discovered | Why it cannot transfer |
|---|---|
| Strategy and positioning | Different circumstances, history, audience, capabilities. |
| Format mix | What this audience responds to is measured on this account. |
| Hook style and voice | What sounds natural to this audience is tested here. |
| Cadence and posting time | Audience activity times differ per account (TikTok Studio). |
| Monetization ladder position | Follower count, eligibility, and country differ per account. |
| Content-gap topics | Search demand and content gaps differ per account and per time. |
| The control format | The control is the winner *on this account*. A new account has no control until it earns one. |

### 8.3 The transfer protocol — how a new account starts

1. **Diagnose first.** A fresh `ACCOUNT_DIAGNOSIS.md` is opened for
   the new account. Nothing from the old account's strategy is
   written into it except as a *hypothesis to re-test*, labelled as
   such.
2. **Re-test transferred hypotheses.** A hypothesis that won on the
   old account is tested on the new account as a probe (one variable,
   7 days + 1,000 views). If it wins again, it is adopted for the new
   account with its own evidence. If it loses, it is recorded as a
   transfer failure — which is itself a finding about what differs
   between the accounts.
3. **No memorized recipe.** If the factory finds itself applying the
   old account's playbook without re-testing, that is a failure of
   this system, not efficiency. The diagnosis file is the check: a
   strategy entry without a diagnosis entry behind it is an
   unexamined transfer.

---

## 9. How this layer connects — and how it is itself re-audited

### 9.1 Connections

| This system | Connects to | How |
|---|---|---|
| Advantage hypotheses | `EXPERIMENTS.md` | An advantage hypothesis becomes an experiment: one variable, a falsifier, 7 days + 1,000 views, win only on comments/view AND completion together. The experiment protocol is the test bench for advantage claims. |
| Experiment results | Advantage map | A result that confirms an advantage is written into the account's advantage map with its evidence level (TESTED → PROVEN → RULE). A result that contradicts one demotes it. The map is a living record, not a trophy shelf. |
| Advantage questions | `LEARNING.md` | A question the advantage system cannot answer becomes a learning module or a horizon-scan target. (Example: "why do viewers follow?" became D13; "what does sound do to retention?" became D14.) |
| Learning results | Advantage hypotheses | A module's findings become advantage hypotheses to test — never rules on their own authority. A practitioner claim becomes a hypothesis; only our own measured result or an official document becomes a rule. |
| Proven advantages | `DESIGN_RULES.md` | An advantage that reaches RULE is written into factory law: a checker, a spec, a template. The safe-zone system and the icon library are the existing examples — capabilities that are hard to imitate because they are built, not claimed. |
| Discovery | `LEARNING.md` discovery protocol | Horizon scans are also advantage scans: every scan asks not only "what can we learn?" but "where is the unexploited gap?" Scan reports feed both the discovered-domains log and the gap candidates in §2. |

### 9.2 Re-audit of this system itself

This system is subject to the same rules it imposes. It has no
ceiling and no protected status:

- **At every horizon scan**, the scan asks whether the advantage
  system itself is still the right system: are its criteria still
  right, are its metrics still the ones that matter, has a new
  platform change made a rule obsolete? The scan may reorder,
  rewrite, or remove parts of this file. A change is recorded with
  its evidence.
- **At every learning review**, the assumption register (§5.1) is
  audited, including the assumptions *in this file* — above all the
  assumption that the factory's current method of finding advantage
  is the best one.
- **The system is never finished.** A factory that stops improving
  its ability to discover advantage has stopped discovering
  advantage. The loop in §4.1 has no final step.

---

## 10. Current status — honest, 2026-11-22

| Item | State |
|---|---|
| Advantage level | **NONE.** No advantage has been proven on any account. |
| Accounts diagnosed | **0.** No account exists yet. The diagnosis template (`factory/ACCOUNT_DIAGNOSIS.md`) is ready and empty. |
| Competitors observed | **0.** No systematic observation has been done (Scan 1, gap 5). The Revid baselines are the only comparators on record. |
| Benchmarks measured | **0.** No benchmark row exists. |
| Gaps found | **0 proven.** Candidates exist only as hypotheses (C4 comedy beat, C6 music bed + SFX, C11 curiosity-gap cover) and as modules in the learning queue (D11–D17). |
| What exists | The method (this file), the template, the experiment protocol, the learning program, the checkers, the first two videos as instruments. |
| First action when the account arrives | **Diagnose first** (§1): open the account's diagnosis file, record the facts with evidence, list the assumptions, and only then publish EXP-001/EXP-002 as the first learning instruments — with the explicit note that their strategy comes from desk research, not from this account's data. |

The factory's current work — trivia vs riddles, the safe-zone system,
the icon library, the learning program — is the *preparation* for
advantage, not advantage itself. Advantage begins when the account
exists and the first diagnosis is written.
