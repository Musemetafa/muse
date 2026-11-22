# Factory Learning Program — becoming a professional

**Status:** created 2026-11-22. This is the factory's FIRST responsibility.
**Honest starting point:** the factory currently has **NO proven professional
expertise** in TikTok, SEO, audience understanding, or competitive content
creation. That is Mohamed's own assessment (2026-11-22 ~15:30 UTC), and the
factory accepts it. Nothing in this file claims otherwise. The prototypes
prove the factory can *render* a 90-second narrated video; they prove
nothing about whether anyone will watch it, finish it, or come back for
another one.

**Purpose:** turn "become a professional" from a wish into a documented,
testable system. Every domain below has a level, key questions, a source
hierarchy, and a defined way its knowledge becomes a factory capability.
Learning is permanent work, not a phase: there is no level at which the
factory stops learning.

**Scope note:** Mohamed listed the domains in his 2026-11-22 message. The
list is a floor, not a ceiling. Two further domains were added by the
factory because the work revealed them (D9, D10). The factory is
responsible for discovering the rest.

---

## Knowledge levels

| Level | Meaning | Evidence required |
|---|---|---|
| **NONE** | No proven expertise. The factory must not act as if it has any. | The default. Every domain starts here. |
| **LEARNING** | Studying the domain from sources; no factory decision rests on it yet. | Sources read and cited in a module report. |
| **TESTED** | The knowledge was turned into a hypothesis and run as an experiment. | Hypothesis + experiment in `EXPERIMENT_LOG.md`. |
| **PROVEN** | Our own account data confirmed it. | Measured result against the pre-registered rule. |
| **RULE** | Written into factory law (`DESIGN_RULES.md`, `EXPERIMENTS.md`, or a module). | The rule names the evidence that earned it. |

A domain reaches RULE only through our own measured results, or through an
official platform document that states the rule directly (a policy is a
rule the moment TikTok publishes it). A practitioner claim never becomes a
rule on its own authority — it becomes a hypothesis first.

**Current level in every domain below: NONE.** Some adjacent factory
knowledge exists (the render pipeline, the safe-zone system, the
experiment protocol) but none of it is professional expertise in the
domains listed here. Do not let the existence of working code be mistaken
for the existence of professional judgement.

---

## Source hierarchy — what counts, and how much

| Tier | Source | Weight | Tag |
|---|---|---|---|
| 1 | **Official platform documentation and policy** — TikTok Help Center, TikTok Newsroom, TikTok for Developers, TikTok Safety Center, Google Search Central. | Decisive. A policy is a rule the moment it is published. | `[OFFICIAL]` |
| 2 | **Published platform data and research** — TikTok's own published statistics, Creator Academy data, peer-reviewed or large-sample published studies. | Strong, but check the sample and the date. | `[DATA]` |
| 3 | **Credible practitioner experiments with data** — a practitioner who shows their numbers, their method, and their sample size. | A hypothesis, never a rule. Test it ourselves. | `[PRACTITIONER]` |
| 4 | **Claims, opinions, marketing** — tool blogs, "guru" advice, uncited assertions, AI-video-tool marketing. | Unproven. Flag it and do not build on it. | `[UNPROVEN]` |

**Tagging rules (binding):**
- Every substantive claim in every module report carries a tag and a date
  read. A claim without a tag is an opinion, not knowledge.
- `[OFFICIAL]` vs `[PRACTITIONER]` vs `[DATA]` vs `[UNPROVEN]` is a
  statement about the *source*, not about whether the claim is true.
  An official page can be outdated; a practitioner claim can be right.
  The tag says how much the factory may lean on it before testing.
- **Knowledge expires.** When TikTok changes a policy, a formula, or a
  feature, every claim that depended on it is re-checked. The re-check
  trigger is recorded in the module report. A claim that was true in
  2026 and is still cited in 2027 without a re-check is a stale claim,
  not knowledge.
- **Never present an unproven claim as a rule.** If the factory writes a
  rule, the rule names its evidence: an official source, or our own
  measured result.
- **Never copy a famous creator's style, never follow a ready-made
  recipe.** The factory's job is to discover its own creative
  opportunities and build a distinctive identity. Studying what others
  do is research; copying what they do is the opposite of the brief.
  A module may analyse a format's mechanics; it may not prescribe
  imitating a specific creator.

---

## The learning loop

```
Learn (module) → Turn into a capability or a testable hypothesis
  → Experiment (EXPERIMENTS.md) → Measure (7 days + 1,000 views)
  → Correct the knowledge → Record in EXPERIMENT_LOG.md
  → If proven, write it into factory law; if disproven, write down
    what was wrong and what replaces it
```

Rules of the loop:
- First experiments are **learning instruments, not proof of expertise**.
  A good result on EXP-001 does not make the factory a TikTok
  professional. It makes the factory one experiment wiser.
- Do not wait until the factory "knows everything" before experimenting,
  and do not treat early experiments as evidence of mastery. Learn and
  test in parallel; let the results correct the knowledge.
- When a result contradicts the knowledge, the knowledge is wrong, not
  the result. Update the module, not the numbers.
- Every module ends with a "what this changes in the factory" section:
  concrete rules adopted, or hypotheses queued for testing. A module
  with no consequence for the factory is a reading list, not learning.

---

## The domains

### D1 — TikTok platform mechanics
**What the factory must be able to DO:** explain, from TikTok's own
documents, how a video gets from upload to a viewer's For You feed;
predict which of our videos are eligible for recommendation and which
are not; keep every published video inside the platform's rules.
**Current level:** NONE (Module 1, done 2026-11-22, is the first study).
**Key questions:** What are the stages of the recommendation system?
Which signals does TikTok say it uses, and which does it say it does
*not* use? What makes a video ineligible for the For You feed? What
does TikTok not disclose about ranking?
**Sources:** Tier 1 first — Newsroom "How TikTok recommends videos",
Safety Center recommendation-system page, Community Guidelines.
**Becomes a capability via:** `research/tiktok-mastery-1-2026-11-22.md`
(Module 1); rules adopted into `DESIGN_RULES.md` and the publishing
checklist in `EXPERIMENTS.md`.

### D2 — TikTok SEO
**What the factory must be able to DO:** choose, for each video, the
topic phrase real people search for; place it in the caption, on
screen, and in the spoken script so the video is findable by search;
read Creator Search Insights and find content gaps; measure search
traffic per video.
**Current level:** NONE.
**Key questions:** What does TikTok officially confirm about search
ranking, and what is practitioner inference? Do captions, on-screen
text, and spoken audio all feed search — and with what weight? How do
content gaps work, and how are they found? How much of a video's value
is search value under Creator Rewards?
**Sources:** Tier 1 — Newsroom "Creator Search Insights", Newsroom
Creator Rewards (search value as a formula metric). Tier 3 for the
three-layer (caption / on-screen / audio) practice, flagged as
practitioner until our own experiments test it.
**Becomes a capability via:** a keyword routine added to the video
build (caption + on-screen + script carry the same topic phrase);
a search-topic queue in the experiment log; Module 4 report.

### D3 — Google SEO for video
**What the factory must be able to DO:** judge whether a TikTok-hosted
video (or a page about it) can appear in Google search results; know
what indexing and appearance require; decide whether a web presence is
worth building for the factory at all.
**Current level:** NONE.
**Key questions:** Does Google index TikTok video pages, and for what
queries? What does Google require for a video to appear in video
results (structured data, thumbnails, transcripts)? Is a factory
website a discovery asset or a distraction at this stage?
**Sources:** Tier 1 — Google Search Central (video indexing, VideoObject
structured data). Tier 3 for practitioner claims about TikTok-on-Google
visibility.
**Becomes a capability via:** Module 8 report; a decision (with
reasons) on whether the factory builds any web presence. No website is
built before this module — a public site is also a precondition TikTok
may demand for API app review, which is a separate, documented fact.

### D4 — Audience study, especially the US audience
**What the factory must be able to DO:** describe the target viewer —
what they care about, how they behave on TikTok, what they expect from
a quiz or riddle video, what feels natural and what feels foreign;
write questions, jokes, and references that land with a US audience
instead of reading as translated or generic.
**Current level:** NONE. The factory's English is untested against a
real US audience; Mohamed's judgement alone is not a substitute (he
has said so himself).
**Key questions:** Who watches quiz/riddle content on TikTok, and why?
What do US viewers expect from a 90-second quiz round? Which
references, phrasings, and humour styles read as natural, and which
read as imported? What do comments on comparable videos actually say?
**Sources:** Tier 2 — published audience data (Pew, TikTok's own
published usage data, large-sample creator analytics). Tier 3 — comment
analysis on comparable videos (read, not copied). Our own account's
comments and retention data, once they exist, outrank all of it.
**Becomes a capability via:** an audience profile document (written
after Module 3, updated from our own data); writing rules in the
script templates; Module 3 report.

### D5 — Retention science
**What the factory must be able to DO:** explain, with evidence, why a
viewer stays or leaves at each second of a video; design the pacing of
a round (question → think → reveal) so completion rises; read a
retention curve in TikTok Studio and say what to change next.
**Current level:** NONE. The factory has a 5-second think time (trivia)
and a 10-second think time (riddles) chosen by intuition, not evidence.
The H3 prediction in `EXPERIMENTS.md` (pace beats suspense) is a
guess waiting for data.
**Key questions:** What does the retention curve of a quiz video look
like, and where do viewers leave? Does a longer think time raise
completion (suspense) or lower it (boredom)? What does a rewatch mean,
and what causes one? Which is worth more: a viewer who finishes once,
or a viewer who rewatches half?
**Sources:** Tier 2 — published retention research where it exists.
Tier 3 — practitioner retention analyses with data. Tier 1 — TikTok
Studio's own retention metrics (once the account exists). Our own
retention curves are the deciding evidence.
**Becomes a capability via:** pacing rules in `DESIGN_RULES.md`
(think-time values, reveal timing, rewatch triggers); hypotheses in
the experiment queue; Module 2 report.

### D6 — Hooks, of all kinds
**What the factory must be able to DO:** open a video in a way that
stops the swipe, in several distinct ways — visual, audio, textual,
narrative — and choose the hook that fits the video instead of
repeating one template; test hooks against each other and keep the
winners.
**Current level:** NONE. The current prototypes open with a title card
("TRIVIA CHALLENGE") and a spoken introduction. No hook has been
tested against any other.
**Key questions:** What kinds of hooks exist, and what does each one
promise the viewer? Which hook fits a quiz round and which fits a
riddle round? Does the hook live in the first 1 second, the first 3,
or the whole opening beat? What is a hook that is a lie (clickbait the
video does not deliver) — and why is it banned by our own rules?
**Sources:** Tier 3 — hook taxonomies from practitioners, treated as
inventories to test, not recipes to follow. Tier 2 where a study
measures hook performance. Our own experiments decide which hooks
work for *our* format.
**Becomes a capability via:** a hook library in `factory/` (named hook
patterns, each with its promise and its falsifier); hook wording as
the first variable in the experiment queue; Module 2 report.

### D7 — Brand and identity
**What the factory must be able to DO:** build an account a viewer
remembers, searches for, and follows for its value — a name, a visual
system, a series structure, a voice, and a promise that is the same in
every video and different from every other quiz account.
**Current level:** NONE. The factory has a visual system (safe zone,
icons, accent colour, progress track) but no brand: no account name,
no series identity, no stated promise, no reason for a viewer to
follow rather than just watch.
**Key questions:** What is the account's promise in one sentence? What
makes a viewer follow a quiz account instead of watching one video and
leaving? What does "distinctive" mean when the format (quiz) is
crowded — where does the difference live? How does a series structure
(streaks, rounds, scores) turn viewers into returners?
**Sources:** Tier 2 — published brand research where applicable.
Tier 3 — analyses of distinctive accounts (mechanics, not imitation).
Our own follows/view and return-viewer data, once they exist.
**Becomes a capability via:** a brand document (name, promise, visual
and verbal identity, series structure); identity rules in
`DESIGN_RULES.md`; Module 6 report.

### D8 — Craft: storytelling, design, motion, voice, editing, performance analysis
**What the factory must be able to DO:** write a round that holds
curiosity without artificial confusion; design a frame that reads in
one glance; move elements with purpose; choose and direct a voice that
sounds natural to a US listener; cut a video so no second is dead air;
and read performance data and say what to change.
**Current level:** NONE as professional craft. The factory has proven
*technical* craft (deterministic rendering, word-timed captions, safe
zone) and an unproven voice (af_heart, listening test unanswered).
Technical craft is not creative craft.
**Key questions:** What makes a quiz round a story rather than a list
of questions? What does the current motion vocabulary lack, and which
gaps matter for retention? Does the voice sound natural to a US
listener — and who decides? What does a good edit feel like at 90
seconds?
**Sources:** Tier 1 for the tools' own documentation (Kokoro, OpenFilm).
Tier 3 for craft practice. The listening test and the audience's
retention data are the deciding evidence for voice and pacing.
**Becomes a capability via:** script templates; motion primitives in
`factory/icons.py` and the renderer; voice decision after the
listening test; Module 7 report.

### D9 — Research and fact-checking for content (factory-added)
**What the factory must be able to DO:** verify every question, answer,
fact, and riddle before rendering, from a checkable source; keep a
source record per video; never present a fabricated claim as fact.
**Current level:** NONE. The prototypes were fact-checked against
reliable sources and the sources recorded in `prototype-1/REPORT.md`
— that is manual practice on two videos, not proven professional
expertise. No systematic method exists yet.
**Key questions:** What counts as a reliable source for a trivia
answer? How is a source recorded so a later correction is traceable?
What happens when a published video is found to contain an error?
**Sources:** Tier 1 — the sources themselves (encyclopaedias,
official records). Tier 1 — TikTok's misinformation policy (a wrong
"fact" presented as fact is a policy risk, not just an embarrassment).
**Becomes a capability via:** a fact-check checklist in the build
process; a sources file per video; a correction procedure; Module 9
report.

### D10 — Account operations and standing (factory-added)
**What the factory must be able to DO:** keep the account in good
standing; read TikTok Studio (retention, traffic, search, monetization
status) and record numbers verbatim; respond correctly to a strike,
a removal, or a review; never do anything that risks the account.
**Current level:** NONE. The legitimate connection paths, the Studio
metrics, and the prohibited automation are documented in
`research/tiktok-connection-2026-11-22.md` — that is desk research,
not proven professional expertise. No account exists yet, so no part
of it has been practised.
**Key questions:** What does each TikTok Studio screen actually show,
and which number answers which question? What is the appeal process,
and when is it used? What account behaviours put standing at risk?
**Sources:** Tier 1 — TikTok Help Center, TikTok Studio itself,
Community Guidelines (enforcement). Tier 1 — the Creator Rewards
review/appeal rules.
**Becomes a capability via:** a Studio reading routine in
`EXPERIMENTS.md` §4; an operations checklist; Module 10 report.
Pulled forward immediately if any strike, removal, or review occurs.

---

## Module queue

| # | Module | Domains | Why here | Output |
|---|---|---|---|---|
| **1** | **TikTok mastery** — platform mechanics, discovery, TikTok SEO, policies, monetization | D1, D2 (intro), D10 (intro) | The ground rules. Without it the factory could publish something ineligible, unlabelled, or unfindable. Done first, done now. | `research/tiktok-mastery-1-2026-11-22.md` |
| **2** | **Retention science + hooks** | D5, D6 | The first creative variables the factory will test (hook wording is first in the experiment variable queue; think time is the H3 prediction). Highest leverage on completion, the deciding metric. | `research/retention-hooks-YYYY-MM-DD.md` |
| **3** | **US audience study** | D4 | Needed before writing the next round of questions and riddles. The current prototypes were written with no audience knowledge. | `research/us-audience-YYYY-MM-DD.md` |
| **4** | **TikTok SEO, deep** — keyword practice, Creator Search Insights routine, search-value measurement | D2 | Needed to pick the next topics from real search demand (content gaps) instead of guessing. Feeds the idea queue. | `research/tiktok-seo-YYYY-MM-DD.md` |
| **5** | **Performance analysis** — reading TikTok Studio, retention curves, turning numbers into decisions | D8 (analysis), D10 | Needed when the first experiment windows close (7 days after publish). Without it the numbers sit unread. | `research/performance-analysis-YYYY-MM-DD.md` |
| **6** | **Brand and identity** | D7 | Once the first comparison reports, the factory needs a distinctive identity, not a generic quiz format. Also sets the account name, bio, and series structure. | `research/brand-identity-YYYY-MM-DD.md` |
| **7** | **Craft, deep** — storytelling, editing, voice, motion beyond the current vocabulary | D8 | Informed by what Modules 2 and 5 showed. Decides whether the factory needs OpenFilm motion, a different voice, or a new edit rhythm. | `research/craft-YYYY-MM-DD.md` |
| **8** | **Google SEO for video** | D3 | A second discovery surface. Lower priority: TikTok is the primary surface, and Google visibility for TikTok-hosted video is indirect without a web presence the factory does not have. | `research/google-video-seo-YYYY-MM-DD.md` |
| **9** | **Research and fact-checking, systematic** | D9 | The current manual checking works at 1 video/day. This module systematizes it before volume or topic breadth grows. | `research/fact-checking-YYYY-MM-DD.md` |
| **10** | **Account operations and standing** | D10 | Mostly covered by the connection research and the experiment protocol. Formalizes the routine. Pulled forward immediately on any strike, removal, or review. | `research/account-operations-YYYY-MM-DD.md` |

**Queue rules:**
- The queue is a priority order, not a prison. A module is pulled
  forward when the factory's next decision needs it, or when the
  platform changes underneath it.
- A module is not "done" when its report is written. It is done when
  its knowledge has changed something in the factory — a rule, a
  template, a hypothesis — and that change names the module as its
  evidence.
- New domains discovered later get a D-number, a queue position, and
  a level of NONE. Discovering a gap is progress, not failure.

---

## What "professional" means here

Not a certificate and not a feeling. A professional factory is one that:
1. Knows what it does not know, and says so (every domain above starts
   at NONE, in writing).
2. Can state, for any decision, whether the evidence is an official
   document, published data, a practitioner claim, or our own measured
   result — and acts accordingly.
3. Learns from its own market, not from imitation: the account's data
   outranks every guru.
4. Turns learning into durable capability: a rule, a template, a
   module, a check — not a memory in a chat.
5. Keeps learning after every win. No successful style is final; no
   module is the last one.

The loop (OPERATIONS.md) runs this file: each run reads the module
queue, does the next learning step, and records what changed.
