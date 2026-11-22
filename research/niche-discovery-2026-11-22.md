# Niche Discovery — Ranked Shortlist

**Date:** 2026-11-22
**Purpose:** Evaluate candidate niches/formats against the six evidence
criteria, using the three desk-research reports produced this run, and
choose what to prototype first.
**Sources (this run):**
- `research/niche-demand-2026-11-22.md` — demand evidence, primary sources
- `research/niche-formats-stack-fit-2026-11-22.md` — stack fit, 10 ideas per format
- `research/niche-commercial-2026-11-22.md` — Creator Rewards eligibility, RPM, AI/originality policy

## The six criteria (as set in STATE.md)

1. Audience demand — real, repeated interest, not a passing wave.
2. Spreadability — attracts attention, holds viewers, prompts sharing.
3. Differentiation — something different or better, not mere imitation.
4. Repeatability — dozens or hundreds of ideas without losing appeal.
5. Production feasibility — high quality with the available means, zero spend.
6. Commercial viability — a logical path to income, under TikTok policy.

## Constraint that shapes every candidate

TikTok Creator Rewards (US, Help Center, read 2026-11-22): 18+, personal
account, 10,000 followers, 100,000 views in the last 30 days; each paid
video must be **original and at least 1 minute long**, with ≥1,000 qualified
For You views. "Not original" explicitly includes looping videos, photos,
and **only text overlays**. TikTok publishes no RPM; creator-reported range
is $0.40–$1.00 per 1,000 *qualified* views (qualified views are far below
public views). **Design rule for every prototype: 60+ seconds, narration +
motion + captions — never text-only.** Short 15–30s versions can grow an
account but cannot earn under this program.

AI policy (TikTok Help Center): realistic AI content must be labelled;
labelling does not affect distribution if guidelines are followed. No
TikTok rule bans AI-made video from Rewards — **originality decides, not
production method**. Unoriginal/reused material is For You-ineligible,
which zeroes qualified views. Generic TTS narration is reported exempt
from labelling (secondary summary of Creator Academy — verify in-app).

## Ranked shortlist

### 1. Trivia / quiz — PROTOTYPE FIRST
- **Demand:** Strongest. #quiz ranked #1 and #trivia #3 in TikTok Creative
  Center's Card & Board Games category (12 Nov 2026); standing category,
  not a one-week spike. Dedicated accounts publish daily series.
- **Spreadability:** Strongest mechanism in the file. An unanswered
  question forces a pause (watch time), invites an answer in the comments
  — the scarcest reaction (0.08% of views in Revid's 176K-video sample) —
  and invites rewatches to check missed answers.
- **Differentiation:** Medium. The format is crowded; the edge must come
  from question quality (the "obvious" answer is wrong), a signature
  reveal mechanic, and a consistent visual identity — writing and code,
  not footage.
- **Repeatability:** Very high. Question banks are effectively unlimited;
  10 concrete ideas in the stack-fit report.
- **Feasibility:** Strong. Pure typography + timer + reveal; fully carried
  by code motion + Kokoro TTS + faster-whisper captions. Measured stack
  cost: ~5.5 s render per 6 s of video (ffmpeg path); TTS RTF 2.67 means a
  60 s narration takes ~160 s to synthesize.
- **Commercial:** Viable if built as a multi-question round (8–10
  questions) to clear 60 s with narration — a single-question 15 s clip
  pays nothing.
- **Risks:** Accuracy (one wrong answer fills comments with corrections —
  every answer fact-checked before rendering); visual sameness; the
  "Only 1% get this" style reads as clickbait if overused.

### 2. Riddles / logic puzzles — PROTOTYPE FIRST
- **Demand:** Strong. Best account-level engagement data found: puzzle
  accounts at 5–15% engagement (IQFluence, Oct 2026) vs platform average
  ~2.6% by followers; @karenpuzzles 14.84% engagement; ~1M-follower
  accounts exist. (Note: @karenpuzzles is a physical-puzzle account, not
  a text-riddle account — do not conflate.)
- **Spreadability:** Strong. Challenge-to-intelligence hook drives comments
  (answers/scores) and shares (challenging friends).
- **Differentiation:** Medium-high. Original riddles written for the
  format + a signature "3 clues, 10 seconds" structure; classic riddles
  are public domain.
- **Repeatability:** High. Large public-domain corpus plus logic puzzles;
  10 concrete ideas in the stack-fit report.
- **Feasibility:** Strong — arguably the best fit. Suspense is built by
  pacing text reveals and TTS pauses, both code-controlled.
- **Commercial:** Same as trivia: needs a multi-riddle round or riddle +
  explanation to clear 60 s with narration.
- **Risks:** Riddle quality is everything; weak or well-known riddles get
  scrolled past. The "solve it yourself" pause must not feel like dead air.

### 3. "Did you know" facts / EduTok — PROTOTYPE SECOND WAVE
- **Demand:** Moderate-strong. Standing hashtags (#LearnOnTikTok,
  #DidYouKnow); 49% of consumers reportedly use TikTok to look up answers
  (Hootsuite via ClipCreator — secondary). But measured curiosity-hook
  performance is average among breakouts (8.5x vs 8.8x median, TryVolume
  w/c 21 Nov 2026) — solid, not a cheat code.
- **Spreadability:** Medium. Curiosity hooks open videos well; retention
  depends on the surprise landing, not the format.
- **Differentiation:** Low-medium. Facts alone are commodity content;
  the edge is verifiable, genuinely surprising facts with the source shown
  on screen, and themed series structure.
- **Repeatability:** Very high. One fact per video, endless supply; 10
  concrete ideas in the stack-fit report.
- **Feasibility:** Strong. Single-fact videos are the easiest fit: TTS +
  kinetic text + a counting/zooming graphic.
- **Commercial:** Needs 3–5 facts per video (or one fact + explanation)
  to clear 60 s with narration.
- **Risks:** Fact-checking cost — surprising facts are the most likely to
  be wrong or exaggerated; each fact needs a checkable source.

### 4. History / science explainers — PROTOTYPE SECOND WAVE
- **Demand:** Strong for reach per video. Best "small account, huge reach"
  evidence: 38.5K-follower space account reaching 8.1M plays; 13.7K
  followers → 325K plays (24x followers). Faceless tutorials median 156K
  views, ~3x on-camera tutorials (Revid).
- **Spreadability:** Medium-high. A good explainer holds viewers to the
  payoff; the format naturally clears 60 s.
- **Differentiation:** Medium. Obscure events and counterfactual hooks
  ("what if this one decision went differently") rather than the same 20
  famous topics.
- **Repeatability:** High. History and science questions are endless; 10
  concrete ideas each in the stack-fit report.
- **Feasibility:** Medium. Timelines, maps, and simple diagrams are
  code-drawable; anything needing archival photos, paintings, or
  photorealistic imagery is blocked (no image generation proven on this
  VM). Diagram complexity is the ceiling.
- **Commercial:** Viable — the standard shape (60–90 s narrated explainer)
  already clears the bar.
- **Risks:** Accuracy risk higher than quizzes; a wrong claim damages
  credibility. Visual cost per scene is the highest of the shortlist.

### 5. Word games — HOLD (test later as a quiz variant)
- **Demand:** Weak / gap. No hard demand data found either way.
- **Spreadability:** Unknown.
- **Differentiation:** Medium — speed rounds, themed sets, streak system.
- **Repeatability:** Very high; generated from word lists.
- **Feasibility:** Strong. Letters/tiles are code-drawn.
- **Commercial:** Same 60 s + narration rule applies.
- **Verdict:** Do not prioritize until a dedicated check finds
  account-level evidence. Test later as a quiz variant (e.g. an anagram
  round inside a trivia video).

### 6. Listicles / countdowns — HOLD (test later as a component)
- **Demand:** Weak. No hard numbers obtained; appears only as a component
  of other formats.
- **Feasibility:** Medium-strong for text-based lists; weak when items
  need photos.
- **Verdict:** Unproven, not disproven. Test later as a quiz/facts variant
  (e.g. a "top 5" round inside a trivia video).

### 7. "What if" scenarios — HOLD
- **Demand:** No standalone demand data gathered.
- **Feasibility:** Medium. Narrative is TTS + text, which works; the wow
  factor needs scale visuals we can only approximate with shapes.
- **Risks:** Speculation must stay clearly labelled hypothetical; sloppy
  "science" is a misinformation risk. Most script-dependent format.
- **Verdict:** Second-wave at earliest, once diagram quality and TTS
  pacing are proven.

### 8. Motivational / stoicism quotes — DO NOT PROTOTYPE
- **Demand:** Weak-moderate. No primary or large-sample data found; all
  claims come from AI-video-tool marketing blogs.
- **Feasibility:** Medium. Text + motion is easy, but the emotional punch
  usually comes from music and imagery we cannot generate; TTS reading a
  quote can sound flat.
- **Commercial:** Text-only quote slideshows are explicitly excluded from
  Creator Rewards as "not original".
- **Verdict:** Easy to make, hard to stand out, weak evidence. Skip.

### 9. Storytime / Reddit-style narration — DO NOT PROTOTYPE
- **Demand:** Large, durable audiences; serialized retention. But:
- **Feasibility:** Weak. Standard production needs gameplay/satisfying
  background footage we cannot film and should not lift from games.
  Original stories must be written, not copied from Reddit (rights and
  originality risk).
- **Verdict:** Viable only with original scripts and generated visuals —
  a writing capability to test, not a solved pipeline step. Skip until
  the visual question is solved.

## What this run did NOT decide

- No success numbers were set before studying the data, per the brief —
  and none are set here either. Baselines for comparison (from the demand
  report): Revid 0.08% comments/view and 7.1% likes/view; Socialinsider
  2.6% engagement by followers; 16–30 s median-view peak. A fair
  comparison method must be defined *before* judging prototypes — that is
  the next step's job.
- No revenue forecast: TikTok publishes no RPM. Creator-reported
  $0.40–$1.00 per 1,000 qualified views is an estimate, not a plan.
- TTS naturalness for quiz/riddle delivery is still untested (blind
  listening test pending) — the prototypes will be its first real test.

## Decision

**Prototype first: a trivia quiz round and a riddle round** — each 60+
seconds, with Kokoro narration, code-computed motion, and faster-whisper
captions, built from the proven stack. Define the comparison method
(metrics, baselines, what counts as a meaningful difference) before any
success judgement. Keep history/science explainers as the second wave;
word games and listicles as quiz variants; motivational and storytime
formats are out for now.
