# Experiment Log

One entry per experiment, in the form defined in
`factory/EXPERIMENTS.md` §6. Created in advance of the first publish so
the record is ready; the first entry is written when the first
experiment publishes (EXP-001, trivia quiz round).

No entries yet.

## EXP-001 — Trivia quiz round — 2026-11-22 (published)
Hypothesis:     A trivia quiz round earns more comments per view than a riddle round, because every question invites the viewer to answer in the comments — the question itself is the call to comment.
Variable:       format (trivia quiz round vs riddle round)
Control:        EXP-001 is the control arm; EXP-002 (riddle round) is the variant arm
Variant:        n/a for the control arm — the comparison is EXP-001 vs EXP-002
Published:      2026-11-22 19:50:09 UTC (re-published; first post 19:35:01 UTC deleted — see Correction below)
Post URL:       https://www.tiktok.com/@7711047379341231137/video/7711084680379895063
Video ID:       7711084680379895063
Video file:     prototype-1/v2/trivia-quiz-round-v2.mp4 (720x1280, 90.41 s, H.264+AAC)
Caption:        Can you answer all 5 questions before the timer runs out? 🧠 #Quiz #Trivia #BrainTeaser #GeneralKnowledge #QuizTime
Visibility:     Public (Everyone)
AI label:       **ON — verified.** Toggle verified ON before Post (ai_is_on(): chromatic descendant background rgb(32, 213, 236); screenshot 05-ai-label-on.png shows the toggle blue); public video page shows "Creator labelled as AI-generated" (v2-video-page-text.txt line 37). The first post (video 7711080785582787862, 19:35:01 UTC) was published WITHOUT the label — the publish script recorded ON from a DOM heuristic (transparent-background match) that was a false positive; screenshots 05/06 (v1) show the toggle was actually OFF (grey) at publish time, and the public video page check found no AI label. The post-publish edit view (Studio → Content → pencil) exposes caption/cover/location/visibility only — no AI toggle — so the label cannot be added after publishing via web Studio. That video was therefore DELETED (see Correction below).
Measured on:    2026-11-29 (pending — 7-day window; needs ≥1,000 views to judge)
Results:
  | Video   | Views | Completion | Likes/view | Comments/view | Shares/view | Rewatches | Follows/view |
  | Control |       |            |            |               |             |           |              |
  | Variant |       |            |            |               |             |           |              |
  (pending measurement)
Verdict:        pending
What was learned: The local-browser publish route works end-to-end (login → upload → caption → Post → profile shows the video). Two process defects found: (1) the AI-toggle check must verify a real DOM state change (class / descendant background), never a background-colour match — the publish script is fixed; (2) TikTok pre-fills the caption editor with the file name — the script now clears it first. First numbers at publish: 1 view / 1 like within minutes (own verification traffic, not audience signal).
What changes next: Correction 2026-11-22 ~19:43–19:50 UTC — the first post (video 7711080785582787862, published 19:35:01 UTC without the AI label) was DELETED (confirmed: Content row gone, profile empty, old URL "Video currently unavailable"; evidence: tiktok-session/publish-exp001/delete-evidence.json). Re-published correctly as video 7711084680379895063 at 19:50:09 UTC with the AI label ON. Publish-script defects fixed: (a) AI check now verifies a real DOM state change (aria-checked / checked|active class / chromatic descendant) — the transparent-background heuristic is gone; the redundant aria-checked == "true" gate was dropped (this DIV switch never carries aria-checked); (b) a JS bug (.rstrip is not a JS method) in the new check was found and fixed before it could post anything; (c) clicking the toggle opens a "Labelling AI-generated content" confirm modal — the script now clicks "Turn on" before verifying. AI-toggle verification is now proven on a real toggle click, so EXP-002 may proceed. Monetization status at publish: NOT ELIGIBLE — Creator Rewards Programme "Ineligible" (Studio → Monetization, read 2026-11-22 ~19:04 UTC); total rewards $0.00.
Monetization status at measurement: (pending — record at measurement)

## Queued hypotheses (Module 3, research/curiosity-science-2026-11-22.md §9e)

Ready to run once the format is stable; one variable each, same protocol
(7 days + 1,000 views minimum, win only on comments/view AND completion).
Full wording and falsifiers in the report — summaries here only.

- **H-M3-1 — Gap size (common-mistake vs straightforward).** A round built
  around common-mistake questions earns higher comments/view and higher
  completion than a difficulty-matched straightforward round.
- **H-M3-2 — Post-reveal placement (the rule-6 test).** A CTA after a reveal
  earns fewer follows per view than the same CTA at the end of the video;
  a fact after a reveal is repeated less in comments than the same fact
  before the first question. Needs comment coding; run after the format
  is stable.
- **H-M3-3 — The "why" line.** A reveal with a one-sentence "why the
  answer is true" earns higher comments/view than the bare answer only.
- **H-M3-4 — The returning question.** A video revisiting one question
  from the previous week (same fact, new wording) earns higher
  comments/view than an all-new video. Needs a second week of videos.
