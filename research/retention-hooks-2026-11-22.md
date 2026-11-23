# Module 2 — Retention science + hooks

**Date:** 2026-11-22 · **Domains:** D5 (retention science), D6 (hooks, of all kinds)
**Status:** DONE as a learning module. **Level after this module: D5 LEARNING, D6 LEARNING — not TESTED.**
No account exists yet and no video of ours has retention data, so nothing here is proven
about *our* format. This module changes what the factory builds next (rules + hook library +
test designs), and its claims stay labelled until our own curves exist.

**How to read the labels:** [OFFICIAL] = TikTok's own pages or publications.
[ACADEMIC] = peer-reviewed or published research with data. [PRACTITIONER — with data] =
a practitioner analysis that shows its numbers, sample and method, and can be checked.
[PRACTITIONER — claim] = advice with no data shown. [UNPROVEN] = a number or rule with no
source the factory could verify. [INFERENCE] = the factory's own reasoning from the above,
flagged as such. A claim's label is part of the claim.

---

## 1. Retention, completion and watch time are three different numbers

[PRACTITIONER — with data] TikTok Studio shows, per video, a retention curve (share of
viewers still watching at each second), an average watch time, a "watched full video"
percentage, and a rewatch count. These are not interchangeable:

- **Retention** is the curve. It starts at 100% and mostly falls; nobody joins late.
- **Completion** is one point on it: the share who reached the last frame.
- **Average watch time** is the area under the curve, in seconds or as a share of length.
  Rewatches inflate it, because a second loop adds play time. A 12-second video with an
  average watch time of 15 seconds was watched, on average, more than once.
- **Rewatch** is a count of viewers who reached the end and kept going into a second loop
  in the same sitting — not someone scrolling back later, and not a share to a friend.

[OFFICIAL] TikTok names finishing a longer video as the strongest signal it describes
(Module 1, §1.2), and completion is therefore the factory's deciding metric (LEARNING.md
rule 1). Average watch time is a supporting metric: it can be high because many people
rewatched a short video, which is not the same as many people finishing a 90-second one.
[INFERENCE] For the factory's 90-second format, completion is the number to optimise and
to compare between EXP-001 and EXP-002. Average watch time is read second, as a check on
rewatch behaviour, never as a substitute for completion.

**No official benchmark exists.** TikTok publishes no "good completion rate" for any
length or niche. [UNPROVEN] Practitioner claims of a 50% completion threshold, or of a
single "healthy" percentage, have no verifiable source and are NOT adopted as rules.
The factory compares each video only against its own other videos at the same length,
and against the baselines it pre-registers in `EXPERIMENTS.md`.

---

## 2. The shape of a TikTok retention curve — what the evidence actually shows

### 2.1 Most videos are not finished

[ACADEMIC] Zannettou et al., CHI 2024, "Analyzing User Engagement with TikTok's Short
Format Video Recommendations using Data Donations": 347 TikTok users donated viewing
histories covering 9.2M recommended videos. **55% of recommended videos were not watched
till the end, most skipped before the halfway point.** User attention stayed stable at
around 45% over the users' lifetime. A follow-up (Coimbra Vieira et al., WebSci Companion
2026) reports the fraction of videos watched until the end "rarely exceeds 60%". Video
duration was the strongest predictor of whether a video was watched to the end — longer
videos are finished less often, which is exactly why the factory's 60-second minimum is
a cost it pays deliberately for Creator Rewards eligibility, not a retention advantage.

[INFERENCE] A 90-second quiz video should expect most viewers not to finish. The
comparison that matters is not "did most people finish" but "did this video finish more
people than the control, and where did the curve bend".

### 2.2 The first three seconds decide almost everything — and the window is shrinking

[PRACTITIONER — with data] A code-rendered short-video experiment (dev.to, Fast Data,
November 2026) posted 20+ videos from a brand-new, zero-follower account on TikTok,
YouTube Shorts and Instagram, and published the per-second Studio numbers for five
TikTok videos. **Between 44% and 62% of viewers were gone by second 3; after that the
curves flatten.** One quiz video with an AI voice (17 s, ~1,060 views) kept 68% at 1 s,
43% at 3 s, and 20.4% watched fully. This is the closest available analogue to the
factory's own production method (code-rendered, AI-voiced, new account) — and it is still
one account, five videos, uncontrolled: the short videos were also better made than the
long ones. Treat the *shape* as evidence and the *percentages* as a rough band, not a
benchmark.

[ACADEMIC — data-donation panels] "State of the Feed" (vantezzen.io), comparing two
donation panels measured identically, late 2024 vs 2026: **videos dismissed within 3
seconds rose from 23% to 33%; median time before a video is swiped away fell from 10 s
to 6 s.** Caveat, stated by the source itself: the two waves are different people, so
this is a panel-to-panel trend, not a within-person change. Direction is consistent
with the dev.to numbers; the exact percentages are not load-bearing.

[OFFICIAL] TikTok's Creator Academy: "The first few seconds of your videos are the most
critical in terms of hooking your audience and stopping the scroll." (Quoted via a
secondary check of the Academy page, October 2026 — re-verify directly against the
Academy page; see §8.) TikTok's Ads Help Center creative best practices (June 2025):
"Prioritize your hook in the first 6 seconds" and "Introduce your content proposition in
the first 3 seconds". Note the scope: this is ads guidance, and the data behind TikTok's
Creative Codes dates to 2020–2022. The 3-second proposition / 6-second hook window is
adopted as the factory's working window, not as a law of nature.

**The working rule the factory adopts:** the promise of the video — what it is, and
what the viewer gets by staying — must be on screen and spoken by second 3, and
something must already be moving in frame 0. The stricter 2-second reading favoured by
some practitioners ("the decision lands closer to two seconds") is [PRACTITIONER — claim]
with no data the factory could verify; it is a design aspiration (aim for 2, deadline 3),
not a rule.

### 2.3 Frame 0 is live

[PRACTITIONER — with data] In the dev.to experiment, the video whose opening showed six
identical bars growing together lost **43% of viewers in the very first second** — nothing
differed, nothing happened. The versions with camera movement from frame 0 kept 75–88%
through second 1. [PRACTITIONER — with data] In Blossom's video library, videos opening
on a mood-setting shot before any information reached 1.62× their account's usual views
(2,817 videos) against 2.41× for the typical video (48,786 videos) — about a third lower;
a first frame that looked wrong or surprising did better, 2.70× (2,183 videos). Both are
observational, single-source library numbers, not experiments — but they point the same
way as the dev.to data: a static or merely pretty opening is the most expensive frame
in the video.

**Consequence for the factory, stated plainly:** the current prototypes open with a
static title card ("TRIVIA CHALLENGE") and a spoken introduction. By the evidence in
this module, that opening is the weakest part of both videos. It is kept unchanged in
the v2 prototypes for one reason only — they are the control comparison, and changing
the opening now would mix variables (§7). The hook work applies to the next variant
round, not to the controls.

### 2.4 The curve after second 3: four shapes, four diagnoses

[PRACTITIONER — with data] Retention-curve reading guides (Blossom; Go Viral) agree on
the same four shapes, and the factory adopts this diagnostic vocabulary — as a way to
*read* its own curves in Module 7, not as proven fact:

| Shape | What it looks like | Likely cause | Fix to test |
|---|---|---|---|
| Early cliff (0–2 s) | 100% → ~55% by second 2, then flat | Dead first frame, greeting instead of a promise, cover/caption mismatch, audio starting quiet or mid-breath | Rebuild the first second only: promise in the first spoken line and on screen |
| Slow slope | No dramatic drop; leaks a few points every second to ~20% | Opening worked, nothing after it re-earns attention | Add a change every few seconds; cut lulls (§4) |
| Sudden mid dip | A step down at one timestamp | One beat broke the promise, confused, or bored — e.g. a question that vanishes, a long pause | Find the exact second; fix that beat, not the video |
| End bump / rise | Curve flattens or rises near the end | Viewers looping — a clean loop, dense detail, or a reveal that sends them back | Study it; a loop is a rewatch signal, not a completion signal (§5) |

**Steepness matters more than height.** A line that falls 20 points in one second is a
scene problem; a line that falls 20 points over 30 seconds is a pacing problem. This
distinction is what turns a curve into an edit decision.

---

## 3. The hook — what TikTok says, and what a hook is for a quiz video

### 3.1 What TikTok itself says

[OFFICIAL] Creator Academy, "Understanding and engaging with your audience" (via
secondary check, October 2026): the first few seconds are the most critical for hooking
and stopping the scroll. TikTok's suggested hook moves: **open with a question, tease
the finished result, set a timer, or create FOMO.**
[OFFICIAL] Creator Academy, "Understanding the Recommendation System" (via the same
check): "Longer watch times signal compelling content. Trim any lulls and use quick cuts
to keep viewers engaged."
[OFFICIAL] TikTok Newsroom, "Scroll-stopping tips from top TikTok creators": creators'
own advice converges on the same point — a strong hook from the very first second, no
rambling, a tease or a highlight of the video; and captions are crucial for keeping
viewers engaged (over 30% watch muted, per practitioner estimates — the muted share is
[PRACTITIONER — claim], the caption advice is TikTok's own).
[OFFICIAL — ads scope] TikTok Ads Help Center: hook in the first 6 seconds, proposition
in the first 3, text overlays at 5–10 words per second; "90% of ad recall impact is
captured within the first six seconds". Adopted with the scope warning: this is recall
for ads, not retention for organic quiz videos.

[INFERENCE] A hook is not a trick and not a greeting. It is a **promise plus a reason
to believe it will be kept**, delivered before second 3, in three channels at once:
spoken line, on-screen text, and motion. The factory's current opening delivers none of
the three in the first 3 seconds: the title card names the format, not the promise.

### 3.2 A hook that lies is banned — by the factory's own rules, not just by TikTok

A hook that promises something the video does not deliver loses the viewer in the next
three seconds anyway [PRACTITIONER — claim, consistent with the mid-dip shape in §2.4],
and it is clickbait the factory will not publish: the factory's red lines (MEMORY.md)
forbid deliberate deception, and Module 1 §5 records TikTok's misleading-content rules.
**Adopted as a rule:** every hook must pass the promise test — *does the video deliver
the exact thing the hook promised, before the viewer can feel cheated?* A hook that
fails the test is rewritten, not published. This is a standing rule, not a hypothesis.

### 3.3 Hook taxonomy for this format — an inventory to test, not a recipe

[PRACTITIONER — claim] Hook taxonomies from practitioners (question, surprise, mistake,
bold claim, timer, result-first, story, dare) are inventories, not evidence: no study
the factory found measures one hook type against another for quiz content. The factory
therefore builds its own library from them — `factory/HOOKS.md` — with eight named
patterns adapted to trivia and riddles, each with its promise, its opening line, what
it must deliver, and its falsifier. The library is the capability this module creates;
which pattern wins is decided by EXP-003 onwards, one variable at a time.

The eight patterns, in brief (full text in `factory/HOOKS.md`): the Direct Question;
the Stakes (timer/score); the Teased Answer; the Impossible Claim; the Common Mistake;
the Streak Challenge; the Reveal Rewind; the Personal Dare. Two design notes that apply
to all eight:

- **The hook lives in the first 1–3 seconds, not in a title card.** The title card is
  not a hook: it tells the viewer the format, and the viewer already knows they are
  watching a quiz from the cover and caption.
- **The hook must survive muted viewing.** The promise is on screen as text as well as
  spoken, because the caption system the factory already built is the hook's second
  channel, not decoration.

---

## 4. The middle — pacing, lulls, and the think-time question

### 4.1 Trim lulls; a designed pause is not a lull

[OFFICIAL] "Trim any lulls and use quick cuts" (Creator Academy). [PRACTITIONER — with
data] The dev.to experiment's sharpest operational finding: in one video the question
on screen disappeared after ~1.5 s, so anyone who looked up at second 2 saw a number
without context — the most common exit point was second 2. Their rule, adopted here as
a testable practice: **the question stays visible for at least 3 seconds, and the first
change (an elimination, a tick, a movement) happens before second 3.**
[INFERENCE] For the factory, "trim lulls" does not mean "cut the think time". The think
time is the product: the viewer is playing, not waiting. A lull is a second in which
nothing changes — no ticking, no progress, no new information, no movement. The design
requirement is therefore: **every second of think time must show change** (countdown,
progress track filling, options eliminating, icon animating). The factory's motion
library (`factory/icons.py`) and progress track already exist for this; whether they are
enough is an empirical question for the first curves.

### 4.2 Think time: 5 s vs 10 s — the H3 prediction, now with a test design

D5's key question, and EXPERIMENTS.md H3: does a longer think time raise completion
(suspense — the viewer stays to see if they were right) or lower it (boredom — the
viewer leaves before the reveal)? No published study the factory found answers this
for quiz video; it is [UNPROVEN] until our own data speaks. The test design, to run
after EXP-001/EXP-002 close:

- One format only (trivia), one variable (think time 5 s vs 10 s), same questions
  difficulty-matched, same hook, same voice.
- Primary metric: completion. Supporting: comments/view during think time (are viewers
  answering in comments instead of leaving?), and the retention curve at the think-time
  seconds (does the dip sit inside the pause?).
- Falsifier, pre-registered: if the 10 s variant's completion is ≥5 points *lower* than
  the 5 s control, pace wins and think time is capped at 5 s for trivia; if ≥5 points
  higher, suspense wins and the next test is 10 s vs 15 s.

**A related mechanism, flagged for M3, not decided here:** the open loop. An unanswered
question holds attention (the Zeigarnik effect is the usual name; the curiosity-gap
science is M3, D11). What M2 already constrains, from Scan 1's finding: **curiosity can
harm near-term memory — what is placed immediately after a reveal may fall in a dead
zone.** So the beat after a reveal must be the next question's hook, not a fact, a CTA,
or a piece of branding. M3 will give this its full treatment; M2 records it as a
provisional pacing rule, labelled [INFERENCE from Scan 1].

---

## 5. The end — completion, loops, and what a rewatch is worth

[PRACTITIONER — with data] In Blossom's library, videos whose last frame flows back
into the first reached **4.22× their account's usual views (3,435 videos)** against
2.24× for the typical video (51,100 videos) — about 88% higher. The same source warns:
a rewatch the viewer did not choose can lift watch time without lifting shares or
follows. Observational, one library, not an experiment — but the mechanism is real:
TikTok loops by default, and a seamless loop can pull a viewer into a second pass
before they decide anything.
[PRACTITIONER — claim] Rewatch rate is read from average watch time vs video length
(§1); TikTok shows no number called "rewatch rate".

[INFERENCE — the factory's position] For a 90-second Creator Rewards video, a loop is
a weak lever and a dangerous temptation. A 90-second loop that a viewer did not choose
is 90 more seconds before they can leave; a loop that works would show up as average
watch time above 100% of length, which for videos above ~15 seconds is rare. The
factory will **not** engineer loop endings for the 90-second format until a completion
baseline exists. The end of a round should instead do two things: deliver the payoff
the hook promised (the score, the answer, the ranking), and open the next loop
*between* videos — the next question, the streak, the follow — which is M4's territory
(gamification and habit), not a trick inside the last frame. If a future short-form
variant (under 30 s) is ever tested, the loop becomes a live variable there.

---

## 6. What TikTok does NOT disclose — labelled unknowns (carried from M1, extended)

1. **No ranking weights.** The relative weight of completion vs likes vs shares vs
   rewatches is undisclosed. Any claim to know it is [UNPROVEN].
2. **No completion benchmark.** No official "good" completion or 3-second retention
   figure for any length or niche. Practitioner thresholds (e.g. "50% completion") are
   [UNPROVEN] and not adopted.
3. **How Studio treats replays in the curve.** TikTok does not publish whether the
   retention chart counts replays; the curve's shape is the usable part, the exact
   treatment is unknown.
4. **Whether the 2-second or 3-second window is the real decision point.** TikTok says
   "first few seconds" and "first 3 seconds" (proposition) / "first 6 seconds" (hook,
   ads). Practitioners argue 2 seconds. The factory designs to 2, deadlines to 3, and
   lets its own 1-second Studio data settle it.
5. **Hook-type effectiveness for quiz content.** No study found. Our own experiments
   decide.

---

## 7. What this changes in the factory

### Rules adopted now (official evidence, or labelled inference)

1. **Promise by second 3.** The video's promise — what it is, what the viewer gets —
   is spoken and on screen by second 3. Design to 2, deadline 3. (Creator Academy;
   Ads Help Center 3 s proposition / 6 s hook.)
2. **Frame 0 is live.** Something moves or changes in the first frame. No static title
   card as the opening, no greeting, no logo-first frame. (Dev.to frame-0 data;
   Blossom library.)
3. **The question stays visible ≥3 seconds, and the first change lands before second 3.**
   (Dev.to operational finding.)
4. **No dead seconds.** Every second of think time shows change — countdown, progress,
   elimination, motion. A pause with nothing changing is a lull and is cut.
   (Creator Academy "trim lulls"; [INFERENCE] for the think-time application.)
5. **The promise test.** Every hook must deliver the exact thing it promised, before
   the viewer can feel cheated. A hook that fails is rewritten, not published.
   (Factory red lines; TikTok misleading-content rules, M1 §5.)
6. **Nothing valuable immediately after a reveal.** The beat after a reveal is the next
   question's hook — not a fact, CTA, or branding. Provisional, [INFERENCE from Scan 1];
   M3 to deepen or overturn.
7. **Completion is the deciding metric; average watch time is supporting.** Rewatch is
   read from average watch time vs length, never as a substitute for completion. No
   invented benchmark: compare only against our own videos at the same length.
8. **No loop engineering for the 90-second format** until a completion baseline exists.
   The end delivers the payoff and opens the between-video loop (M4).

### Hypotheses queued for testing (practitioner evidence — not rules)

- **H-M2-1 — Hook type.** Question vs teased-answer vs timer vs stakes: one hook type
  per video, primary metric 3-second retention, then completion. First variable in the
  experiment queue after EXP-001/002 close.
- **H-M2-2 — Think time.** 5 s vs 10 s inside trivia only (test design in §4.2).
  Pre-registered falsifier: ≥5 points completion difference decides.
- **H-M2-3 — Frame-0 motion.** Static title-card opening vs motion-from-frame-0
  opening, same hook wording: primary metric 1-second and 3-second retention.
- **H-M2-4 — Dead-zone placement.** Fact/CTA after reveal vs next-question hook after
  reveal: primary metric retention in the 5 seconds after each reveal.
- **H-M2-5 — Loop ending (deferred).** Only for a future sub-30 s variant: seamless
  loop vs clean ending, primary metric average watch time as % of length. Not run on
  the 90-second format.

### Changes to EXP-001 / EXP-002 (the first experiments)

- **None.** The v2 prototypes are unchanged: same openings, same think times. Changing
  them now would mix the hook variable into the trivia-vs-riddles comparison and destroy
  the control. Their openings are now *known* to be weak by this module's rules — that
  is information about the baseline, not a reason to rebuild the baseline mid-test.
- The comparison's interpretation changes: if completion is low, the first suspect is
  the opening (title card + intro), not the format. The hook-variant round (H-M2-1,
  H-M2-3) is the next experiment after the verdict, using the winner format.
- H3 (pace vs suspense) is now a designed test (§4.2), not just a prediction.

### Capabilities created

- **`factory/HOOKS.md`** — the hook library: 8 named patterns, each with promise,
  opening line, delivery requirement, and falsifier. D6's "becomes a capability" is met.
- **Retention-curve reading vocabulary** (§2.4) — the diagnostic language M7
  (performance analysis) will use on real Studio curves.
- **Pacing rules** added to `factory/DESIGN_RULES.md` from rules 1–4 and 6 above
  (applied by the loop when it next edits the file; recorded here as the module's
  requirement).

### Re-check triggers

- When the first Studio retention curves arrive (after EXP-001/002 publish + 7 days):
  re-read this module against real curves; any rule our data contradicts is revised in
  writing, with the curve cited.
- If TikTok's Creator Academy changes its hook/retention guidance, or the Ads Help
  Center revises the 3 s / 6 s windows: update rules 1–2 and the queue.
- When M3 (curiosity-gap science) lands: re-check rule 6 and H-M2-4 against it.
- When M7 (performance analysis) lands: the §2.4 diagnostic table becomes a Studio
  reading procedure with real thresholds from our own data.

---

## Sources

**Official (TikTok)**
- TikTok Creator Academy, "Understanding and engaging with your audience" — hook in the
  first few seconds is "the most critical… stopping the scroll"; suggested moves: open
  with a question, tease the finished result, set a timer, create FOMO. Quoted via
  secondary verification (outfeed.ai, checked 7 Oct 2026); re-verify directly against
  the Academy page. https://outfeed.ai/blog/tiktok-strategy/
- TikTok Creator Academy, "Understanding the Recommendation System" — "Longer watch
  times signal compelling content. Trim any lulls and use quick cuts." Via the same
  secondary check.
- TikTok Ads Help Center, "Creative best practices for performance ads" (June 2025) —
  hook in first 6 s; proposition in first 3 s; 5–10 words of text per second; 90% of ad
  recall impact within the first 6 s. Ads scope; underlying Creative Codes data
  2020–2022. https://ads.tiktok.com/resources/help/article/creative-best-practices?la
- TikTok Newsroom, "Scroll-stopping tips from top TikTok creators" — hook from the very
  first second, no rambling; captions crucial.
  https://newsroom.tiktok.com/scroll-stopping-tips-from-top-tiktok-creators?lang=en-GB
- TikTok for Business Blog, "Short Form Video Best Practices" — strong hook, opening
  line (question / relatable statement / bold claim), then benefits, then CTA.
  https://ads.tiktok.com/business/en-AU/blog/tiktok-short-video-best-practice

**Academic / published research**
- Zannettou, S., Nemeth, O.-N., Ayalon, O., Goetzen, A., Gummadi, K., Redmiles, E. M.,
  et al. (2024). Analyzing User Engagement with TikTok's Short Format Video
  Recommendations using Data Donations. CHI '24. 347 users, 9.2M views; 55% of
  recommended videos not watched till the end, most skipped before halfway; attention
  ~45%. DOI: 10.1145/3613904.3642433. https://arxiv.org/html/2301.04945v2
- Coimbra Vieira, C., et al. (2026). Exploring the Limits of Predicting User Watching
  Behavior with Short-Form Videos on TikTok. WebSci Companion '26 — fraction watched
  till the end rarely exceeds 60%; video duration the strongest predictor.
- "State of the Feed" (vantezzen.io) — two donation panels, late 2024 vs 2026: dismissed
  within 3 s 23% → 33%; median time before swipe 10 s → 6 s. Different panels;
  trend, not within-person change. https://wrapped.vantezzen.io/state-of-the-feed

**Practitioner — with data (checked, not trusted blindly)**
- Fast Data (dev.to, Nov 2026) — 20+ code-rendered short videos from a new account;
  per-second TikTok Studio numbers for 5 videos: 44–62% gone by second 3; 43% lost in
  second 1 on a static opening; quiz with AI voice 17 s: 68% at 1 s, 43% at 3 s, 20.4%
  full watch. One account, five videos, uncontrolled.
  https://dev.to/fast_data_asap/i-posted-20-short-data-videos-rendered-from-code-every-video-over-25-seconds-died-and-half-the-4f84
- Blossom, "How to Read Your Retention Graph" — four curve shapes; mood-setting opener
  1.62× usual views (n=2,817) vs 2.41× typical (n=48,786); surprising first frame
  2.70× (n=2,183). Observational, one library.
  https://www.blossai.com/blog/read-your-retention-graph
- Blossom, "What Is a Good Rewatch Rate" — loop videos 4.22× usual views (n=3,435) vs
  2.24× typical (n=51,100); rewatch read from average watch time vs length.
  https://www.blossai.com/blog/rewatch-rate-what-is-good
- Go Viral / Monadly, "TikTok Retention" — retention vs completion vs average watch
  time; curve shape as the usable signal; TikTok does not publish how replays are
  treated. https://trygoviral.com/tiktok-video-retention
- Lilach Bullock, "What Does Rewatched Mean on TikTok Analytics?" — rewatch as
  in-session looping after the end; data appears only after a few hundred views.
  https://www.lilachbullock.com/what-does-rewatched-mean-on-tiktok-analytics/

**Practitioner — claim (not adopted as rules)**
- Hook-rate ~30% band; "2-second hook" as a hard window; 50% completion threshold;
  "80% retention through 3 seconds" Shorts benchmarks; MIT 13 ms image identification
  as applied to hooks. Listed here so the next reader knows they were seen and not
  adopted — not as evidence.

**Internal (factory's own records)**
- `research/discovery-scan-1-2026-11-22.md` — Scan 1: curiosity may harm near-term
  memory (dead zone after a reveal); factory has no audio layer; Series videos do not
  earn Creator Rewards.
- `research/tiktok-mastery-1-2026-11-22.md` (Module 1) — completion as the strongest
  signal TikTok names; 60-second minimum; AI label mandatory.
- `factory/EXPERIMENTS.md` — H3 (pace vs suspense); EXP-001/EXP-002 as the control
  comparison; 7-day / 1,000-view minimum windows.
- `factory/LEARNING.md` — D5/D6 definitions, key questions, queue position (M2).
