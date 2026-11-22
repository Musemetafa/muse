# Discovery Scan 1 — Horizon scan outside the factory's 10 domains

**Date:** 2026-11-22
**Author:** horizon scanner (subagent)
**Scope:** capabilities, techniques, formats, tools, or opportunities relevant to the video factory that are NOT covered by its current learning program (D1–D10, queue M1–M10).
**Hard limits observed:** zero spend; no registrations, no TikTok contact, no account access, no publishing, no purchases. No edits to STATE.md, RUNLOG.md, MEMORY.md, or factory/LEARNING.md. Nothing pushed to GitHub.

## Method

Web search on 2026-11-22 (UTC), in five batches, then reading of the most relevant search-result pages (summaries as returned by search; no live-browser visits, no logins). Queries covered: TikTok LIVE / gifts / subscriptions / Series / Shop affiliate; duets / stitches / playlists / series as growth levers; curiosity-gap and retrieval-practice psychology; gamification / streaks / habit formation; parasocial attachment and why people follow and share; comedy writing (incongruity, benign violation, rule of three); free / open-source music and SFX with commercial licences; kinetic typography and procedural / code-video renderers; sound design and LUFS loudness for mobile; covers / thumbnails and manual A/B testing on TikTok; cross-posting to Shorts / Reels; TikTok AI-label / synthetic-media policy; free / open-source TikTok analytics tooling.

Source discipline follows Module 1: **[OFFICIAL]** = TikTok's own docs / newsroom / support; **[DATA]** = peer-reviewed research or a published dataset with methods; **[PRACTITIONER]** = creator / agency / vendor writing, including when it cites official pages (the citation does not make the interpretation official); **[UNPROVEN]** = a claim with no evidence attached. Unknowns are labelled unknown. No creator's style is copied and none is recommended for copying.

**What the current map already covers (not re-reported as discoveries):** D1 TikTok mechanics / policies / monetization (M1 done — including the 60-second Creator Rewards floor and the AI-label rule); D2 TikTok SEO; D3 Google SEO for video; D4 US audience; D5 retention science; D6 hooks; D7 brand; D8 craft; D9 fact-checking; D10 account operations. Queue: M2 retention + hooks, M3 US audience, M4 TikTok SEO deep, M5 performance analysis, M6 brand, M7 craft deep, M8 Google SEO, M9 fact-checking systematic, M10 account operations.

---

## C1 — Curiosity-gap and retrieval-practice science for quiz / riddle design

**What it is.** Two adjacent bodies of learning science that bear directly on the factory's two chosen formats. (a) Curiosity: Loewenstein's information-gap theory — curiosity peaks when a person knows enough to feel a specific gap but not enough to close it — and Gruber, Gelman & Ranganath (2014, *Neuron*), who showed high-curiosity trivia questions produced better memory for the answer (and even for unrelated material shown during the wait), with dopaminergic reward-circuit and hippocampal activity. (b) Retrieval practice / the testing effect: actively recalling an answer beats re-reading or re-studying for long-term retention (Roediger & Karpicke 2006; Karpicke & Roediger 2008, *Science*: ~80% recall a week later for items kept in testing vs ~33–36% for items dropped from testing; meta-analysis Adesope et al. 2017, g = 0.51 vs restudying). A 2024 *npj Science of Learning* study complicates the picture: high curiosity for a trivia question *interfered* with memory for unrelated scholastic facts presented immediately after it — curiosity focuses encoding, it does not spread it to everything nearby.

**Why it might matter.** The factory's formats *are* curiosity machines: a trivia question is an information gap with a timed reveal; a riddle is a gap with a delayed resolution. D5 (retention) covers holding attention; it does not cover *which* gaps to open, how long to hold them, or what the reveal should do. This science, if it transfers from lab to feed, would govern question difficulty (the gap must be feelable, not impossible), reveal timing (hold long enough for curiosity to build, not so long the viewer leaves), and answer design (the answer must close the gap cleanly — a confusing answer wastes the curiosity). It also reframes the product: a quiz that teaches nothing memorable is a weaker repeat-visit proposition than one viewers actually remember.

**Evidence.**
- Gruber et al. 2014, as summarised: https://scihub101.com/psychology/how-curiosity-improves-memory — [PRACTITIONER] summary of a [DATA] study; the underlying *Neuron* paper is the data source, the page is a secondary summary.
- States of epistemic curiosity interfere with memory for incidental scholastic facts, *npj Science of Learning* 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC10948872/ — [DATA] (peer-reviewed; directly contradicts the simple "curiosity helps everything nearby" reading).
- Fastrich et al. 2018, pre-answer vs post-answer interest in trivia memory (N = 1,498, 244-question database): http://escholarship.org/content/qt70m582rb/qt70m582rb.pdf?v=lg — [DATA].
- Roediger interview on retrieval practice, Digital Promise: https://digitalpromise.org/articles/ask-the-cognitive-scientist-retrieval-practice/ — [DATA] (primary researcher explaining his own studies).
- Retrieval-practice research round-up with citations: https://ahaslides.com/blog/retrieval-practice/ — [PRACTITIONER] (useful bibliography; its own 12,865-educator survey is vendor data, not peer review).

**Verdict: NEW MODULE — D11, queue position M3 (immediately after M2 retention + hooks, before M3 US audience).** It is the science underneath the factory's two formats, and M2 will otherwise build hooks without a theory of what makes a question worth waiting for. The 2024 interference finding must be carried into the module as a caution: do not assume curiosity transfers to adjacent facts or CTAs placed right after a reveal.

---

## C2 — Gamification and habit architecture: streaks, loss aversion, variable rewards

**What it is.** The engagement architecture that turns a one-off interaction into a daily ritual: streaks (consecutive-day counters), XP / levels, leaderboards segmented by activity, and variable (unpredictable) rewards. The mechanism most cited is loss aversion (Kahneman & Tversky: losses feel roughly twice as powerful as equal gains) — a long streak becomes an asset the viewer protects — plus variable-ratio reinforcement, the same schedule that makes slot machines and feed-checking compulsive. Duolingo is the documented large-scale case: monthly churn in major markets reportedly fell from 47% (2020) to 28% (early 2024) as gamification deepened, with a 2016 *Frontiers in Psychology* study linking streaks to higher engagement and retention; a 2025 meta-analysis in the *Journal of Computer Assisted Learning* is cited for game-based quiz formats improving achievement, motivation, and engagement.

**Why it might matter.** The factory's commercial goal needs *returning* viewers, not just one viral video — and D5 retention is about a single video, not about return. A quiz factory has natural gamification material no generic creator has: daily rounds, score-keeping ("Day 14 — can you keep your streak?"), recurring characters / difficulty ladders, leaderboards in comments, and "you got 7/10 yesterday, beat it today" framing. All of it is code-generatable: the factory can render streak counters, score cards, and progress visuals deterministically. The risk is real and must be studied, not assumed away: gamification optimises engagement, not learning, and streak-protection can drive speed-running easy content instead of genuine engagement.

**Evidence.**
- Duolingo gamification case, with SEC-filings / churn figures: https://guul.games/blog/games-for-e-learning-apps-a-strategic-guide-2025 — [PRACTITIONER] (vendor analysis; churn figures attributed to SEC filings and StriveCloud, not independently verified here).
- Why Duolingo's gamification works (and when it doesn't): https://dev.to/pocket_linguist/why-duolingos-gamification-works-and-when-it-doesnt-1d4 — [PRACTITIONER] (good on failure modes: streak speed-running, XP optimising quantity over quality, leaderboard disengagement at the bottom).
- Duolingo streak psychology and the 2016 *Frontiers* study: https://www.historytools.org/docs/longest-duolingo-streak — [PRACTITIONER] (secondary; the 3,911-day streak figure is anecdotal, not a study result).

**Verdict: NEW MODULE — D12, queue position M4 (immediately after D11, before the current M4 TikTok SEO deep).** D11 explains why a single question holds attention; D12 explains why a viewer comes back tomorrow. Together they are the factory's "return loop" — arguably more commercially decisive than SEO depth at this stage. The module must include the failure modes (streak-protection gaming, shallow engagement) as first-class content, not a footnote.

---

## C3 — Why people follow and share: parasocial attachment, social currency, identity

**What it is.** Retention (D5) explains why someone finishes a video; this explains why they follow the account and why they send the video to someone else — two different decisions with different psychology. (a) Parasocial relationships (Horton & Wohl, 1956): repeated exposure to a consistent voice / persona creates a one-sided sense of knowing someone; familiarity, self-disclosure, and direct address ("you guys", "we") deepen it, and algorithms amplify it by re-showing familiar faces. (b) Sharing as social currency: people share content that makes *them* look good — informed, witty, in-the-know, helpful — and that signals identity and taste to their own audience; emotionally charged content is shared more than neutral content. (c) Self-presentation (Goffman): posting and sharing are performances of a "face" for a specific audience, which is why context collapse (different audiences seeing the same share) feels awkward.

**Why it might matter.** The factory currently has no face, no persona, and no host — a synthetic voice reading questions. That is a design choice with a cost this domain would make explicit: a faceless quiz channel may earn views without ever earning follows, because there is nobody to feel attached to. The question is not "add a face" (that would contradict the factory's code-drawn identity) but what a *non-human* persona can do instead: a consistent voice, a consistent character or mascot system, recurring rituals, direct address, and content designed to be *shareable as identity* ("I got 9/10 — can you beat me?") rather than merely watchable. The experiment protocol's win condition (comments/view AND completion together) already gestures at this; this domain would give it a theory.

**Evidence.**
- Parasocial relationships explained (Horton & Wohl 1956; mere exposure; self-disclosure): https://datafield.dev/blog/parasocial-relationships-explained.html — [PRACTITIONER] (secondary summary of a real 1956 paper; the neuroscience claims are stated without primary citations — treat as [UNPROVEN] where uncited).
- Psychology of why people share video (social currency, informational advantage, humour as currency): https://vvideo.co/blog/the-psychology-of-why-people-share-video-ads — [PRACTITIONER] (marketing writing; the "emotionally charged content is shared more" claim is consistent with published work but is not itself a study here).
- Presentation, competition, and coalition-building on social media (Goffman): https://www.optimallyirrational.com/p/what-are-we-really-doing-on-social — [PRACTITIONER] (essay by an academic; Goffman 1956 is real, the extension to social media is argument, not data).

**Verdict: NEW MODULE — D13, queue position after M6 brand (i.e. M7 in the revised queue).** It belongs immediately after brand/identity because it answers what a brand *does* psychologically — creates attachment and shareability — rather than what it looks like. Do not build it before D11/D12: the return loop comes first; attachment theory without a return loop is decoration.

---

## C4 — Comedy craft: incongruity, benign violation, rule of three, callback

**What it is.** A teachable craft, not a talent: humour works (incongruity theory) when a pattern is set up and broken, and (benign-violation theory, McGraw) when something is simultaneously *wrong* and *safe*. The portable structures are setup–punchline, the rule of three (two beats establish a line, the third cuts across it — e.g. "brain tumour, heart disease, and a really ugly tie"), callbacks (a line from the start returning later in a new context), and the inappropriate response. Short-form constraints sharpen them: setups of 1–5 seconds, punchlines that are both heard *and* seen (many viewers watch muted), and visual gags built for a vertical frame.

**Why it might matter.** The factory's current formats are earnest: questions, answers, explanations. Earnestness is forgettable on a feed where the adjacent video is funny. Comedy is also a *retention* tool (a punchline is a reason to stay to the end) and a *share* tool (humour is social currency — see C3). The factory does not need to become a comedy channel; it needs to know whether a light comic layer — a wrong answer that is absurd rather than merely wrong, a recurring gag, a callback to an earlier round — lifts completion and comments without damaging the "real knowledge" credibility the fact-checking domain (D9) protects. That is testable, and the factory's code-rendered format makes comic timing (a beat held, a text slam) cheap to vary.

**Evidence.**
- Comedy and humour: incongruity, benign violation, structures for 15–60 s formats: https://datafield.dev/why-they-watch/part-05/chapter-25/ — [PRACTITIONER] (textbook-style chapter; theories are real, the short-form applications are the author's).
- John Vorhaus on the rule of three (two points make a line, the third cuts across it): https://filmcourage.com/2026/09/05/the-one-comedy-tool-that-every-writer-should-know-john-vorhaus/ — [PRACTITIONER] (interview with a working comedy writer; craft testimony, not data).

**Verdict: HYPOTHESIS TO TEST.** *Hypothesis: adding one scripted comic beat per round — an absurd wrong answer option, delivered as both voice and on-screen text — raises completion rate and comments/view versus the same round without it, with no drop in the share of viewers who later answer a follow-up question correctly.* Test under the existing experiment protocol (one variable, 7 days + 1,000 views minimum, win only on comments/view AND completion together). If it wins, promote to a module (proposed D14, late queue); if it loses or is neutral, record the failure and do not re-test the same beat. Do not import a creator's comic persona — the test is of a structural device, not a style.

---

## C5 — Sound design and loudness: the audio layer the factory does not yet have

**What it is.** A complete audio discipline the factory currently lacks: it has a voice and (presumably) silence. Sound design has three layers mixed in order — dialogue first, sound effects second, music last — with level targets (dialogue −6 to −12 dB peak; SFX −10 to −20 dB; background music −20 to −30 dB under speech, −12 to −18 dB when no one is speaking), ducking (music drops 6–12 dB, up to 22 dB for complex educational content, while narration is active), voice EQ for small speakers (high-pass ~80 Hz, presence boost 2–5 kHz, cut 6–8 kHz), and a delivery loudness target of about −14 LUFS integrated with true peak under −1 dBTP. TikTok and Instagram do not publish a loudness target; −14 LUFS is the practitioner consensus for them, matching YouTube's published normalisation level. FFmpeg's free `ebur128` filter can measure it — no paid tool is needed.

**Why it might matter.** The factory's videos are 60–90+ seconds of continuous narration. On a phone speaker, in a noisy room, an unmixed voice-plus-silence track is fatiguing in a way a viewer cannot articulate but can feel as "boring" — and then swipes. Sound design is also the cheapest retention lever the factory has not tried: a whoosh 10–20 ms before a visual transition, a pop when an answer lands, a riser before a reveal, a music bed that lifts in gaps and ducks under speech. All of it is code-schedulable from the same word-timing data the caption system already uses. The risk of skipping it is that the factory optimises visuals and scripts while losing viewers to audio fatigue it never measures.

**Evidence.**
- Sound design levels, ducking, three-layer mixing: https://mytasker.com/blog/the-complete-guide-to-sound-design-for-video-creators — [PRACTITIONER] (level numbers are practitioner consensus; not a standard).
- Best LUFS for TikTok / Reels / Shorts (−14 LUFS, true peak under −1 dBTP; TikTok target not published): https://www.storycut.com/blog/best-lufs-for-tiktok-youtube-shorts — [PRACTITIONER] (vendor guide; its disclosure notes it sells the tool it describes — discount its product claims, keep the LUFS method, which is independently checkable with FFmpeg `ebur128`).
- Video sound design quick-reference (dialogue −16 to −14 LUFS, ducking, EQ, SFX timing): https://www.skillsdirectory.com/skills/aicodedecode-video-sound-design — [PRACTITIONER] (skill directory entry; numbers agree with the other two sources, which is weak corroboration, not confirmation).

**Verdict: NEW MODULE — D14, queue position M7 (between brand M6 and craft-deep M7 in the current queue, i.e. immediately before the craft module it feeds).** It is production-blocking in the sense that every video shipped without it carries an unmeasured audio handicap. The module's first deliverable should be a measurable audio spec (LUFS target, ducking rules, SFX timing rules) enforced by an automated FFmpeg check, in the same spirit as the existing safe-zone checker.

---

## C6 — Free, commercially licensed music and SFX sourcing (the supply side of C5)

**What it is.** The sourcing problem behind C5: where does a zero-spend factory get music and effects it may legally use in monetised US content? Three routes surfaced: (a) openly licensed libraries — Openverse, a search engine over ~5.2M openly licensed audio files (Freesound, Jamendo, Wikimedia Commons) with a no-key API and a commercial-use filter (CC0 needs nothing; CC-BY needs attribution logged per file); SFX Kit, 320 CC0 effects; SFXMint, 11,500+ CC0 effects. (b) Open-weight local models — Stable Audio 3 Small SFX (Stability AI), free for commercial use under $1M yearly revenue, runs on a CPU/laptop; HunyuanVideo-Foley (Tencent) for video-matched Foley, commercial outside EU/UK/South Korea under its licence terms. (c) Hosted free tiers with traps — ElevenLabs Sound Effects (10k credits/month free, but paid plans for commercial use), Adobe Firefly Generate Sound Effects (commercially safe per Adobe, but credit-gated), Stable Audio web app (free plan includes a commercial licence but only ~50 credits/month). MMAudio and Meta AudioGen are non-commercial (CC BY-NC / research-only) and must be excluded.

**Why it might matter.** Music and SFX are the factory's largest unfilled production gap, and the wrong source is a legal and account-standing risk, not just a quality gap: a non-commercial licence on a monetised video, or an unattributed CC-BY track, is exactly the kind of violation D10 (account standing) exists to prevent. The distinction the factory already draws — free source vs free operation — applies here with force: a "free" hosted tier that requires a paid plan for commercial use is not free for this factory. Openverse + CC0 kits are the only routes that are free *and* commercially usable *and* CPU-friendly today; Stable Audio 3 Small SFX is the one local model worth a licence-and-CPU verification pass.

**Evidence.**
- AI SFX generator comparison, Oct 2026 (licence table; Stable Audio 3 Small SFX commercial under $1M; MMAudio non-commercial): https://www.cinemadrop.com/blog/ai-sound-effects-generator — [PRACTITIONER] (comparison site; licence claims must be verified against each project's own licence before use).
- Openverse (5,223,435 files, no-key API, commercial filter) and SFX Kit (320 CC0): https://fadeadeniyi.com/static/guides/3-free-ai-audio-tools-editors-hate.pdf?v=1 — [PRACTITIONER] (PDF guide; the Openverse counts are checkable against the live API).
- Openverse-SFX skill (licence filter `cc0,by,pdm`, `credits.txt` mandatory, librosa beat grid, FFmpeg `ebur128` verification): https://sourceweft.com/skills/gh-varnan-tech-opendirectory-openverse-sfx-skills-openverse-sfx-df5c2cedc4899824 — [PRACTITIONER] (a reusable workflow, not a source of fact; its licence-filter rule is the part to adopt).

**Verdict: HYPOTHESIS TO TEST.** *Hypothesis: adding a ducked, beat-matched CC0 music bed (sourced via Openverse with attribution logged) plus three timed SFX (pop on answer reveal, whoosh on transition, riser before the final question) raises completion rate versus the same video with voice only, with no drop in comments/view.* One variable is the audio package as a whole (not each sound separately — that would take months). Before the test, verify the licence of every file used and log attribution; if any file's licence is unclear, drop it. If the hypothesis wins, fold sourcing + mixing into D14 as its supply chapter; if it loses, the factory has evidence that its audience does not want a bed, which is itself a useful finding.

---

## C7 — Comments-as-content and the community loop (reply-to-comment video, Q&A, comment bank)

**What it is.** A TikTok-native mechanic the factory's current plan does not use: replying to a comment with a full video, which pins the original comment at the top of the reply, so the reply's premise is visible before anyone watches. Practitioners describe a loop, not a one-off: publish a seed video → harvest questions / disputes / requests from comments → select one as the premise for the next video → reply by video → harvest the new comments for the next premise. Adjacent mechanics: profile Q&A (questions become content prompts), pinned videos (welcome / FAQ / invitation to participate), duet/stitch prompts ("stitch this with your score — I'll duet the best"), and a weekly ritual (same format, same day) that gives followers a reason to return. The discipline is a cap (e.g. a fixed number of comment-reply videos per week, reserved for questions that make genuinely useful standalone content) so reply culture does not become unsustainable.

**Why it might matter.** This is the factory's cheapest source of *proven* demand: a question asked in comments is evidence of curiosity (C1) from a real viewer, not a guess from a brainstorm. It also directly feeds the experiment protocol's win metric — comment-reply videos publicly reward commenting, which should raise comments/view on every other post, and they create continuity (returning viewers recognise the next instalment). For a quiz factory the loop is unusually natural: "You asked for a harder round — here it is", "You said Q3 was wrong — here's the proof", "Top scorer this week gets the next round named after them". The factory cannot do any of this until the account exists, but the *system* — a comment bank with columns for question, category, topic, urgency, monetisation relevance, publication status — can be designed now.

**Evidence.**
- TikTok community building (reply-to-comment as a recurring habit; reply routine to avoid burnout): https://contentmation.com/marketing/tiktok/tiktok-community-building — [PRACTITIONER].
- The comment-to-content loop framework (five steps; comment bank schema): https://insighttokai.com/blog/the-comment-to-content-loop-framework-2026-turn-viewer-questions-into-your-next-viral-video — [PRACTITIONER] (2026 framework post; the "loop" is a proposed method, not a measured result — [UNPROVEN] as a growth claim, useful as a workflow design).
- TikTok strategy for community building (7 community-first formats; hook/CTA formulas; 90-day plan): https://www.copycut.app/guides/tiktok-strategy-for-community-building — [PRACTITIONER].

**Verdict: NEW MODULE — D15, queue position M11 (after M10 account operations).** It requires a live account with comments to exist, so it cannot be built before D10. But its *design* (comment bank schema, reply-selection rules, weekly ritual template) should be sketched during M10, so the first week of the live account is not spent inventing a workflow. Do not treat practitioner "community" language as evidence that reply videos grow accounts — no controlled data was found in this scan; the claim rests on the mechanic being native to TikTok and on the logic that rewarded commenting begets commenting.

---

## C8 — Monetisation beyond Creator Rewards: LIVE, Series, Subscriptions (the ladder)

**What it is.** Creator Rewards is one rung, not the ladder. The other rungs, with their thresholds (all requiring 18+, good standing, eligible country): going LIVE at 1,000 followers (may vary by region) with LIVE Gifts (viewers buy Coins, send Gifts, creators collect Diamonds — reported at $0.005 per Diamond after TikTok's cut, with a typical $100 withdrawal threshold); TikTok Subscriptions at 10,000 followers + 100,000 views in the last 30 days (fans pay ~$5.99/month for badges, emojis, subscriber-only chat/videos; TikTok's share reported at 50–70%); Video Gifts at 10,000 followers + 30-day-old account + a public video in the last 30 days; and TikTok Series — a paid collection of up to 80 videos, each 30 seconds to 20 minutes, priced once at $0.99–$189.99 (price cannot be changed after posting; payout on the 15th once the balance reaches $50, via PayPal; buyers can refund within 14 days if they have watched under 25%). Critically for this factory, a rule surfaced in practitioner checking of TikTok's own pages: **videos linked to a Series do not earn Creator Rewards** — the rungs interact and can conflict.

**Why it might matter.** The factory's commercial goal is a sustainable income, and D1 covers Creator Rewards. But the ladder changes *what to build*: a quiz factory that only ever makes free 60–90 s videos has one income stream gated at 10,000 followers; a factory that also designs a premium Series (e.g. a 20-episode "masterclass" or a hard-mode season) and a LIVE quiz format has income that starts earlier (LIVE at 1,000) and recurs (subscriptions). LIVE is also the only format in this scan that is *inherently* interactive — a live quiz round is a different product from a recorded one, and it is the natural home for C2's streaks and C7's community loop. The Series conflict rule is the kind of fact that must be in the factory's permanent rules, not discovered by losing Rewards income on a linked video.

**Evidence.**
- Monetisation requirements by follower count (Rewards 10k; Subscriptions 10k + 100k views; Video Gifts 10k; LIVE 1k): https://blog.hootsuite.com/how-many-followers-on-tiktok-to-get-paid/ — [PRACTITIONER] (Hootsuite guide citing TikTok pages; thresholds match the official pages cited in the next source).
- Monetisation requirements checked against TikTok Creator Academy / Help Center, Oct 2026: https://www.ranktracker.com/blog/tiktok-monetization-checker/ — [PRACTITIONER] (secondary; explicitly defers to the official page as final word — correct discipline, and the right posture for the factory too).
- TikTok Series rules, pricing, payouts (80 videos, 30 s–20 min, $0.99–$189.99, price unchangeable, refund rule): https://www.sirency.com/blog/tiktok-series-for-creators — [PRACTITIONER] (checked against TikTok help pages 1 Oct 2026).
- TikTok Series rules re-checked 5 Oct 2026: https://tokconnect.com/guides/tiktok-series/ — [PRACTITIONER].
- Series videos do not earn Creator Rewards; Duets/Stitches are not original under the programme: https://www.hookstudio.ai/guides/frutinovelas-en-tiktok — [PRACTITIONER] (checked a real episode against TikTok's Creator Rewards page, programme terms, and Creator Academy pages, 18 Nov 2026 — a useful *method* example, not an official ruling).

**Verdict: NEW MODULE — D16, queue position M12 (after M11 / D15).** It extends D1 rather than replacing it: D1 is the platform and its first monetisation rung; D16 is the full ladder, the interactions between rungs (especially the Series/Rewards conflict), and the product design each rung implies (LIVE quiz format, premium Series design). Nothing in it can be acted on before the account exists and approaches 1,000 followers, which is why it sits last — but the Series/Rewards conflict rule should be copied into the factory's permanent rules now, because it constrains future product decisions.

---

## C9 — TikTok Shop affiliate (commission income at a lower threshold — and a trust risk)

**What it is.** A separate, commission-based programme: creators promote products listed in TikTok Shop through shoppable videos and LIVEs and earn a percentage per sale (reported bands: 5–10% electronics, 10–20% fashion/home, 15–30% beauty/skincare; overall US average reported at 13.02% in 2026). Entry is lower than Creator Rewards: 1,000 followers via a 30-day Pilot Programme (capped at 3 shoppable videos/day and 3 shoppable LIVEs/week), 5,000 followers for the full US Open Plan; 18+, 30-day-old account, good standing, ID verification, a public video in the last 28 days. Payouts are rolling weekly after a ~16-day return window, minimum withdrawal ~$10. Practitioner reporting is consistent that most creators earn $0 in their first 60 days and only a small fraction break through to $1,000+/month.

**Why it might matter — and why it might not.** On paper this is the earliest income the factory could reach (1,000 followers vs 10,000), and it pays per sale rather than per view, which diversifies income away from RPM. In practice it is a poor fit for a quiz factory and a risk to it: shoppable videos are product demonstrations, not trivia rounds; inserting product pitches into a knowledge format trades the trust D9 (fact-checking) and the factory's red lines (no deception, no misleading claims) build, for commission; and the account would need ID verification and tax handling the factory has not planned for. The honest question is whether a quiz audience buys anything a quiz channel can credibly recommend (books? puzzle sets? — unknown) — and that question has no evidence behind it in this scan.

**Evidence.**
- TikTok Shop Creator Program (Pilot at 1,000; commission 10–30%; $5K–$50K/month top-earner claim): https://www.shortformnation.com/blog/tiktok-shop-creator-program-how-it-works-requirements-and-how-to-earn-2026-guide — [PRACTITIONER] (top-earner figures are marketing-style claims — [UNPROVEN] as stated; thresholds are consistent across sources).
- TikTok Shop Creator in 2026 (Pilot caps, ID verification, commission bands, $0-in-60-days reporting): https://projectcasting.com/blog/casting-calls-acting-auditions/how-to-become-a-tiktok-shop-creator-in-2026-requirements-commissions-earnings — [PRACTITIONER].

**Verdict: WATCH ITEM.** Do not build a module, do not plan product content, do not apply. Revisit only when (a) the account passes 1,000 followers, (b) the factory has a product category a quiz audience could credibly want, and (c) the trust cost has been explicitly weighed against the commission. The trigger for revisiting is evidence, not the threshold alone: a comparable knowledge/quiz account earning affiliate income without damaging its standing. Until then, the Shop is a distraction from the core loop (views → follows → Rewards → Series/LIVE).

---

## C10 — Cross-platform distribution: Shorts and Reels are not TikTok with a different logo

**What it is.** The same vertical video performs differently on the three short-form platforms, and the differences are structural, not cosmetic. Metricool's Short Video Report 2026 (6M+ videos, 375k+ accounts, [DATA] as a published dataset — vendor-collected, not peer-reviewed): TikTok averages ~33,000 views per video (42.6% more than the average Reel, 6× the average Short); Instagram leads on shares and comments at almost every account size; YouTube Shorts trails on every metric in that dataset. The signals differ: TikTok rewards completion and re-watches; Reels rewards *sends* (DM forwards — stated by Instagram's Adam Mosseri as the strongest single Reels signal) and profile visits; Shorts rewards subscriber conversion and watch-time on subsequent (long-form) videos, with likes-per-impression carrying more weight. The mechanical rules are consistent across sources: never cross-post a watermarked download (Instagram actively suppresses Reels with TikTok watermarks; TikTok deprioritises other platforms' watermarks); export one clean master, then adapt hook, caption placement, and safe zones per platform; upload natively in each app.

**Why it might matter.** The factory's render pipeline already produces a clean master (no platform watermark) — it is accidentally cross-platform-ready. That is an unexploited option: the same 60–90 s quiz round could, with per-platform caption/safe-zone adaptation, reach a Reels audience that shares more and a Shorts audience that compounds into long-form discovery, diversifying the factory away from single-platform dependence. The cost is real: three safe-zone layouts instead of one, three caption styles, three posting workflows, and three analytics streams — and the factory's current safe-zone system is TikTok-specific. The decision is not "post everywhere" but whether the marginal audience is worth the marginal system complexity, and which platform's signal (shares on Reels) the factory's content is actually built to earn.

**Evidence.**
- Video repurposing: same short, three results (Metricool Short Video Report 2026, 6M videos): https://metricool.com/how-to-repurpose-video-content/ — [DATA] (vendor dataset with stated sample; not peer-reviewed; the platform-leadership pattern is the finding, the exact averages are sample-dependent).
- TikTok vs Shorts vs Reels 2026 (signals per platform; Mosseri on sends; never post the same file): https://www.markstudios.com/blog/tiktok-reels-shorts-cross-platform-strategy-2026 — [PRACTITIONER].
- Cross-posting rules (watermark suppression; adapt captions/hashtags/hooks): https://syncstudio.ai/blog/cross-post-videos-tiktok-reels-shorts — [PRACTITIONER] (the claim that TikTok caps posting after 5+ non-interactive videos in 7 days is stated without an official citation — [UNPROVEN] here).

**Verdict: NEW MODULE — D17, queue position M9 (after M8 Google SEO, before M9 fact-checking systematic — i.e. once the factory understands search on TikTok and on Google, it is ready to understand distribution across platforms).** The module's first task is not posting anywhere: it is a per-platform adaptation spec (safe zones, caption placement, hook timing, signal to optimise) and a costed decision on whether the factory's clean master is worth adapting at all. No cross-posting before that spec exists — a watermarked or mis-zoned re-upload would actively harm the accounts it is meant to grow.

---

## C11 — Covers / thumbnails and pre-click testing (the factory has no front door)

**What it is.** TikTok surfaces covers (thumbnails) on the profile grid, in search results, and in parts of the feed — and the factory currently has no cover system at all: its videos begin at frame zero. Practitioner guidance (no official TikTok CTR data exists — TikTok does not publish a cover CTR metric) converges on: 3–5 word bold text answering "why should I care?", high-contrast subject, one focal action, text placed inside the safe zone (the factory's existing safe-zone system already constrains this), and a consistent template that becomes part of visual brand. TikTok has **no native A/B testing tool for organic content** (unlike Meta Ads or YouTube thumbnails), so testing is manual: publish variants differing by exactly one variable (cover text vs no text; face close-up vs wide; bright vs muted; custom cover vs auto frame), control everything else, and compare — with the success metric proxied, since profile-to-video CTR is not surfaced (compare total views on videos with different cover styles posted in similar periods). Claimed lifts (15–40% views; faces 20–35% higher CTR; thumbnails "up to 2× more clicks") are agency / vendor claims without published methodology — treat as [UNPROVEN], not as expected results.

**Why it might matter.** The factory's experiment protocol is built for *in-video* variables (hook, pacing, difficulty). Covers are a *pre-click* variable: they decide whether a profile visitor or a searcher ever presses play, which matters most exactly when the factory starts earning profile traffic from a series or from search (D2). A code-rendered cover is also nearly free for this factory: the same Pillow system that draws icons can render a deterministic cover frame with the round's question or score as text. The risk is spending effort on a variable whose effect the factory cannot measure cleanly (no CTR metric) — hence the verdict below is a test, not a module.

**Evidence.**
- TikTok thumbnail tricks 2026 (3–5 words; safe zones; 15–40% lift claim): https://postigniter.com/blog/10-tiktok-thumbnail-design-tricks-to-boost-ctr-in-2026 — [PRACTITIONER] (the lift figure is an agency claim with no methodology — [UNPROVEN]).
- TikTok A/B testing (no native tool; one variable; cover variables; CTR must be proxied): https://ttcalculator.net/learn/tiktok-ab-testing-content/ — [PRACTITIONER] (methodologically the soundest source found; its face/CTR percentages are stated without a source — [UNPROVEN]).

**Verdict: HYPOTHESIS TO TEST.** *Hypothesis: a code-rendered cover frame with a 3–5 word curiosity-gap title (e.g. the round's hardest question, not "Episode 17") earns more profile-grid taps — proxied by views on videos posted in matched pairs in similar periods — than the auto-selected first frame, with no change to completion rate.* This test can only run once the account exists and has profile traffic; until then, build the cover *renderer* (a deterministic first-frame export from the existing Pillow system) so the test is ready. If the proxy shows no difference, drop covers as a variable and keep the auto frame.

---

## C12 — Code-video renderers beyond the current stack: HyperFrames, Motion Canvas / Revideo, Manim, oxframe

**What it is.** A fast-moving family of free, code-first video frameworks that did not exist (or were not mature) when the factory chose Python + Pillow + FFmpeg, with OpenFilm as a conditional layer. The November 2026 landscape, as ranked by agent-workflow fit: **HyperFrames** (Apache-2.0, largest in the comparison; HTML/CSS/GSAP scenes rendered locally with FFmpeg; word-level timing from transcription; free local renders, no watermark; a Studio app with a free plan that includes AI voiceovers/music/SFX and 3 AI video clips + 5 cloud exports/month, Pro $25/month); **Motion Canvas** (MIT) and its heir **Revideo** (MIT, headless-browser parallel rendering, templated TypeScript video); **Manim** (MIT, 42k+ stars, the 3Blue1Brown engine — unmatched for precise equations, graphs, geometric transforms, Cairo/OpenGL rendering); **oxframe** (MIT/Apache-2.0, Rust, its own CPU renderer with no browser, deterministic frames, `oxframe check` reporting frame problems — median 0.51 s vs Remotion 2.97 s in the vendor's own benchmark); **fframes** (MIT, Rust + Skia, GPU or CPU backend). Remotion itself is *not* MIT — free only for individuals and companies up to 3 people — and is therefore a licensing trap for a growing factory, not a candidate.

**Why it might matter.** The factory's current renderer works (OpenFilm render proven: 720×1280, 6 s, 180 frames, ~29–34 s) — this is not a rescue. It is an option-value question: HyperFrames' kinetic-typography-from-transcription and oxframe's browser-free CPU rendering with a built-in frame checker are capabilities the Pillow stack would have to be hand-built to match, and Manim would unlock a whole format class (animated diagrams, charts, maths visuals) the factory cannot currently produce. The counterweight is switching cost: every renderer change re-opens determinism, safe-zone, and caption-timing verification, and the November 2026 rankings come from vendor / comparison sites with obvious incentives (the oxframe benchmark is the vendor's own; the HyperFrames page is HeyGen's).

**Evidence.**
- Top 10 GitHub repos turning code into motion videos, 13 Nov 2026 (star counts from GitHub API; HyperFrames 1st on agent loop, OpenFilm 3rd, Manim 5th): https://promptstaging.site/article-top-10-github-repos-code-into-motion-videos.html — [PRACTITIONER] (comparison site; star counts are verifiable, the ranking is editorial).
- Remotion alternatives 2026, licences and renderers (oxframe MIT/Apache, HyperFrames Apache-2.0, Revideo/Motion Canvas/fframes/Manim MIT): https://www.oxframe.dev/alternatives/remotion — [PRACTITIONER] (written by the oxframe team — discount its benchmark and its ranking; the licence table is checkable against each project's repo).
- HyperFrames kinetic typography (free, open source, no watermark; word timing from voiceover): https://hyperframes.heygen.com/tools/kinetic-typography — [PRACTITIONER] (vendor page; "free" refers to local rendering — the Studio free plan's AI features are credit-gated, and Studio needs a free HeyGen account, i.e. a registration, which the factory's limits currently forbid).
- Video assembly comparison (HyperFrames, MoneyPrinterTurbo, OpenMontage, Remotion, Manim, OpenFilm): https://agentgid.com/assets/video-assembly/ — [PRACTITIONER] (aggregator; scores are its own).

**Verdict: WATCH ITEM.** Do not switch renderers, do not register for any Studio account, do not install anything on the strength of this scan. The trigger for a real evaluation is a concrete capability gap the Pillow stack cannot close (e.g. a format that needs animated diagrams, or kinetic typography that outperforms the current caption system in a test) — at which point the evaluation must be: licence check against the repo, CPU-only render benchmark on this VM, determinism check (byte-identical re-render), and safe-zone/caption-timing verification, in that order. Until then, note HyperFrames and oxframe as the two names to re-check in the next scan.

---

## C13 — Analytics and research tooling without spend (and where the line is)

**What it is.** The tooling layer D5 (performance analysis, M5) will need, and the ways to get TikTok data for free — with very different legitimacy. (a) Official: TikTok's Display API (reads only users who log in to your app) and Research API (richer, but limited to approved non-commercial researchers; new videos can take up to 48 hours to become searchable, statistics up to 10 days to update — built for studies, not live dashboards). TikTok's own Studio analytics remain the canonical source for the factory's own account. (b) Open-source self-hosted: **4CAT** (MPL-2.0, social-listening datasets, TikTok from a list of post URLs) with the **Zeeschuimer** browser extension (collects posts you see on TikTok/Instagram/X/Threads); **Postiz** (AGPL-3.0, per-post analytics, self-hostable); **tiktok-organic-mcp** (MIT, MCP server for organic analytics via the TikTok Developer API — video performance, engagement, profile insights). (c) Grey-area: **yt-dlp** (TikTok extractor listed as working, Nov 2026) and **TikTok-Api** (MIT, needs a Playwright browser and an `ms_token` taken from your own tiktok.com cookies; its README says bot detection blocks it) — both break when TikTok changes its pages, run from your own IP, and sit in tension with TikTok's terms; hosted scraper APIs are paid and therefore excluded by the zero-spend rule.

**Why it might matter.** M5 (performance analysis) will otherwise be built on manual Studio exports and spreadsheets — workable, but slow, and it cannot answer "what is the niche doing?" without a research feed. 4CAT/Zeeschuimer and the official APIs are the legitimate research route; the scraper route is a standing and legal risk the factory has explicitly decided not to take (no TikTok contact, no account access, no workarounds). The distinction matters enough to record now, before M5 starts: the factory should design its analytics around (i) Studio exports for its own account, (ii) the official APIs where eligible, and (iii) 4CAT-style public-post research — and should explicitly *exclude* cookie-based scraping and bot-detection evasion from its tooling, as a standing rule in the D10 / account-standing sense.

**Evidence.**
- How to scrape TikTok data (official APIs vs yt-dlp vs TikTok-Api vs hosted APIs; Research API delays): https://scrapeio.com/blog/how-to-scrape-tiktok-data — [PRACTITIONER] (a scraping vendor's guide — its description of the official APIs' limits is consistent with TikTok's own docs; its encouragement of scraping is not endorsed here).
- Open-source social media analytics tools, checked 3 Nov 2026 (4CAT, Zeeschuimer, Postiz, Matomo, Superset/Metabase): https://www.femaleswitch.com/directories/tpost/open-source-social-media-analytics-tools?amp=true — [PRACTITIONER] (directory; licence and release claims are checkable against each repo).
- tiktok-organic-mcp (MIT, organic analytics via TikTok Developer API): https://glama.ai/mcp/servers/lanternrow/tiktok-organic-mcp — [PRACTITIONER] (MCP directory listing; the "free and open source" claim needs a repo check before use).

**Verdict: WATCH ITEM.** No module, no installation, no API application in this scan. Feed the conclusion into M5 when it starts: own-account analytics from Studio exports first; official APIs second (eligibility to be checked then); 4CAT/Zeeschuimer as the research route; cookie-based scrapers and evasion techniques explicitly out of scope. Revisit if TikTok opens a free creator analytics API tier or if 4CAT's TikTok source changes.

---

## How the module queue changes

Current queue (M1 done): M2 retention + hooks, M3 US audience, M4 TikTok SEO deep, M5 performance analysis, M6 brand, M7 craft deep, M8 Google SEO, M9 fact-checking systematic, M10 account operations.

Proposed revised queue — new modules inserted where they feed the work that follows them, not appended at the end:

| Revised position | Module | Domain | Reason for the position |
|---|---|---|---|
| M2 (unchanged) | Retention + hooks | D5 + D6 | Unchanged — the immediate next step. |
| **M3 (new)** | **Curiosity-gap & retrieval-practice science** | **D11** | Governs question design; M2's hooks need it. |
| **M4 (new)** | **Gamification & habit architecture** | **D12** | The return loop; pairs with D11. |
| M5 | US audience | D4 | Was M3; now follows the return-loop pair, since audience study should test whether *these* mechanics land with *this* audience. |
| M6 | TikTok SEO deep | D2 | Was M4. |
| M7 | Performance analysis | D5 (analysis) | Was M5; now absorbs the C13 conclusion (Studio exports first, official APIs second, no scrapers). |
| M8 | Brand | D7 | Was M6. |
| **M9 (new)** | **Why people follow & share: parasocial, social currency, identity** | **D13** | Immediately after brand — it is what a brand does psychologically. |
| **M10 (new)** | **Sound design & loudness** | **D14** | Immediately before craft-deep; it is the audio spec craft needs. C6 (sourcing) is folded in as its supply chapter once the C6 hypothesis is tested. |
| M11 | Craft deep | D8 | Was M7; now includes the C4 comedy test result if it wins. |
| M12 | Google SEO | D3 | Was M8. |
| **M13 (new)** | **Cross-platform distribution (Shorts / Reels)** | **D17** | After Google SEO — once search is understood on TikTok and Google, distribution across platforms is the next question. |
| M14 | Fact-checking systematic | D9 | Was M9. |
| M15 | Account operations | D10 | Was M10; C7's comment-bank design is sketched here. |
| **M16 (new)** | **Community & participation mechanics** | **D15** | After account ops — it needs a live account with comments. |
| **M17 (new)** | **Monetisation ladder beyond Creator Rewards (LIVE / Series / Subscriptions)** | **D16** | Last — it needs followers (1,000 for LIVE, 10,000 for the rest). One rule from it is adopted immediately: Series-linked videos do not earn Creator Rewards. |

Net effect: 10 domains become 17; 10 modules become 17 (M1 done + 16 to go). The queue grows by 7 modules, but the *order* matters more than the count: the two highest-leverage insertions are D11/D12 early (they change what the factory builds) and D14 before craft-deep (it changes the audio spec every video ships with). Nothing already queued is removed or demoted in substance — US audience, SEO, and fact-checking only shift by two positions.

Hypotheses to test (not modules yet — run under the existing experiment protocol when the account exists): C4 comedy beat; C6 music-bed + SFX package; C11 curiosity-gap cover. Watch items (no action until their trigger): C9 Shop affiliate; C12 code-video renderers; C13 analytics tooling beyond Studio.

## What this scan did NOT cover (honest gaps)

1. **Accessibility.** Captions for deaf / hard-of-hearing viewers, colour-contrast and font-size minima, flashing-content safety, and TikTok's own accessibility features were not searched. The factory's word-timed captions are an accessibility asset, but no standard was checked against them. This deserves a focused pass before the first public video.
2. **US law beyond TikTok's policies.** FTC endorsement / advertising disclosure rules, COPPA-adjacent questions (the factory's content must not target children), state privacy law, and music-licence enforcement practice in the US were not researched. C6's licence notes are a starting point, not legal advice.
3. **Voice / TTS frontier.** No systematic check of free TTS voices beyond Kokoro (e.g. newer open-weight voices, voice-cloning legality, or multi-voice dialogue) was done; the voice decision is still provisional (af_heart) and this scan does not resolve it.
4. **TikTok's own 2026 product changes after M1.** The scan relied on secondary sources for Series / LIVE / Shop thresholds; every threshold must be re-verified against TikTok's own Help Center / Creator Academy at the moment of use, because TikTok changes them. No threshold in this report should be treated as stable.
5. **Competitor / niche-format intelligence.** No systematic viewing or measurement of what quiz / riddle accounts actually do on TikTok today (formats, lengths, hooks, posting cadence) was possible without TikTok contact, which the limits forbid. The niche-discovery reports remain the evidence base for formats; this scan adds psychology and mechanics, not market observation.
6. **Posting cadence, timing, and volume strategy.** Deliberately not covered: M1 already adopted "no volume strategy" as a rule, and no credible data was found in this scan that would overturn it. It remains an open question for M5 (performance analysis) to answer from the factory's own data.
7. **Non-English / non-US expansion.** Out of scope by decision (English-only, US audience); no assessment was made of whether the formats would transfer.
8. **Depth of the practitioner sources.** Most practitioner claims in this scan (thumbnail lift percentages, Shop earnings, Duolingo churn) are stated without published methodology. They are recorded as [PRACTITIONER] or [UNPROVEN] for that reason, and none of them is used as a rule anywhere in this report.

## Source list (all URLs as found)

- https://scihub101.com/psychology/how-curiosity-improves-memory
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10948872/
- http://escholarship.org/content/qt70m582rb/qt70m582rb.pdf?v=lg
- https://digitalpromise.org/articles/ask-the-cognitive-scientist-retrieval-practice/
- https://ahaslides.com/blog/retrieval-practice/
- https://guul.games/blog/games-for-e-learning-apps-a-strategic-guide-2025
- https://dev.to/pocket_linguist/why-duolingos-gamification-works-and-when-it-doesnt-1d4
- https://www.historytools.org/docs/longest-duolingo-streak
- https://datafield.dev/blog/parasocial-relationships-explained.html
- https://vvideo.co/blog/the-psychology-of-why-people-share-video-ads
- https://www.optimallyirrational.com/p/what-are-we-really-doing-on-social
- https://datafield.dev/why-they-watch/part-05/chapter-25/
- https://filmcourage.com/2026/09/05/the-one-comedy-tool-that-every-writer-should-know-john-vorhaus/
- https://mytasker.com/blog/the-complete-guide-to-sound-design-for-video-creators
- https://www.storycut.com/blog/best-lufs-for-tiktok-youtube-shorts
- https://www.skillsdirectory.com/skills/aicodedecode-video-sound-design
- https://www.cinemadrop.com/blog/ai-sound-effects-generator
- https://fadeadeniyi.com/static/guides/3-free-ai-audio-tools-editors-hate.pdf?v=1
- https://sourceweft.com/skills/gh-varnan-tech-opendirectory-openverse-sfx-skills-openverse-sfx-df5c2cedc4899824
- https://contentmation.com/marketing/tiktok/tiktok-community-building
- https://insighttokai.com/blog/the-comment-to-content-loop-framework-2026-turn-viewer-questions-into-your-next-viral-video
- https://www.copycut.app/guides/tiktok-strategy-for-community-building
- https://blog.hootsuite.com/how-many-followers-on-tiktok-to-get-paid/
- https://www.ranktracker.com/blog/tiktok-monetization-checker/
- https://www.sirency.com/blog/tiktok-series-for-creators
- https://tokconnect.com/guides/tiktok-series/
- https://www.hookstudio.ai/guides/frutinovelas-en-tiktok
- https://www.shortformnation.com/blog/tiktok-shop-creator-program-how-it-works-requirements-and-how-to-earn-2026-guide
- https://projectcasting.com/blog/casting-calls-acting-auditions/how-to-become-a-tiktok-shop-creator-in-2026-requirements-commissions-earnings
- https://metricool.com/how-to-repurpose-video-content/
- https://www.markstudios.com/blog/tiktok-reels-shorts-cross-platform-strategy-2026
- https://syncstudio.ai/blog/cross-post-videos-tiktok-reels-shorts
- https://postigniter.com/blog/10-tiktok-thumbnail-design-tricks-to-boost-ctr-in-2026
- https://ttcalculator.net/learn/tiktok-ab-testing-content/
- https://promptstaging.site/article-top-10-github-repos-code-into-motion-videos.html
- https://www.oxframe.dev/alternatives/remotion
- https://hyperframes.heygen.com/tools/kinetic-typography
- https://agentgid.com/assets/video-assembly/
- https://scrapeio.com/blog/how-to-scrape-tiktok-data
- https://www.femaleswitch.com/directories/tpost/open-source-social-media-analytics-tools?amp=true
- https://glama.ai/mcp/servers/lanternrow/tiktok-organic-mcp
