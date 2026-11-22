# TikTok connection research — how a TikTok account can legitimately be used by an agent

**Date:** 2026-11-22
**Status:** research only. **There is no TikTok account yet.** Nothing was registered, no developer app was created, no TikTok contact was made, nothing was published, no account was accessed. This file records what the legitimate paths are, what they cost, what Mohamed would need to do, and what is still unknown.

**Sources:** TikTok's own developer documentation and TikTok's own site wherever possible. Where a claim comes from a secondary source (a guide quoting TikTok), it is marked **[secondary]**. Every substantive claim carries its source at the end of its bullet or paragraph.

---

## 1. The short answer

| Path | What it does | Needs | Cost | Verdict |
|---|---|---|---|---|
| **A. Manual publishing** — TikTok app / TikTok Studio web | Mohamed posts the factory's videos by hand; reads analytics in TikTok Studio | Nothing but the account | $0 | **Recommended first path — works from day one** |
| **B. Content Posting API — Upload (draft) mode** | Factory uploads a video to the creator's TikTok inbox as a draft; Mohamed finishes it in the app | Developer app, `video.upload` scope, app review | $0 (no fee found in any TikTok doc) | Pursue in parallel with A |
| **C. Content Posting API — Direct Post** | Factory publishes straight to the profile with no human tap | Developer app, `video.publish` scope, app review **and a separate audit** | $0 (no fee found) | Long-term option only — **likely to fail the audit for a single-account internal tool** (see §3) |
| **D. Display API** (`video.list` / `video.query`) | Reads per-video view/like/comment/share counts | Login Kit, `video.list` scope, app review | $0 | Use for counts; it cannot read retention |
| **E. TikTok Studio** | The only source of retention, average watch time, watched-full-video rate, traffic sources, search queries, demographics, and the monetization (Creator Rewards) status | The account itself | $0 | **Required for the experiment metrics** — a human reads it |

**What does not exist:** there is no official API that gives an agent full account control, no API for retention/watch-time, and no API for reading the Creator Rewards status. Retention and monetization status are only visible in TikTok Studio, read by the person holding the account.

---

## 2. Option A — Manual publishing via the TikTok app / TikTok Studio web (recommended first)

**What it is:** the factory renders the video, writes the caption, hashtags, cover choice and a publishing checklist; Mohamed (or whoever holds the account) posts it in the TikTok app or on the TikTok Studio website, and reads the analytics in TikTok Studio.

**Why it is legitimate:** it uses TikTok's own interfaces exactly as TikTok designed them. No third-party tool, no automation, no Terms-of-Service risk.

**What TikTok Studio is:** TikTok's creator hub, available in the app (Profile → Menu → TikTok Studio) and on the web at tiktok.com/tiktokstudio. It has tabs for Overview (post views, profile views, likes, comments, shares, estimated rewards, traffic source, search queries), Content (top posts), and Viewers/Followers (demographics, activity), and per-video detail including retention rate, average watch time, watched-full-video rate, and traffic sources. Date ranges 7/28/60/365 days; data downloadable up to 365 days. Analytics cover only the account holder's own account. **[secondary: personaxpand.com — "How to Use TikTok Studio"; sociality.io — "TikTok Studio: The Complete Guide for 2025"; trackmedia.co — "TikTok Studio Review"]**

**Publishing on the web:** TikTok Studio on the web offers video upload and scheduling **[secondary: tokconnect — "Top 8 TikTok API Posting Tools"; instantdm — "The Only Legitimate Ways to Post to TikTok"]**. The web uploader accepts files up to 10 GB and up to 30 minutes **[secondary: schedulenchill.com — "How to Upload Videos to TikTok from Your PC"]**.

**What Mohamed would need to do:** create the dedicated account (when it exists), open the TikTok app or tiktok.com/tiktokstudio, upload the factory's video file, paste the factory's caption, set the AI-generated label toggle, set privacy to Public, and publish. Then, once a week, read the per-video numbers from TikTok Studio and pass them to the factory for the experiment log.

**What it costs:** $0. TikTok Studio is free; no paid tier was found for it.

**What remains unknown:** nothing about the path itself — it is certain to work. The open questions are about the account (Section 8).

---

## 3. Option C — Content Posting API, Direct Post (the long-term, uncertain path)

Read this one before B, because the audit gate decides the whole API strategy.

**What it is:** the factory calls TikTok's official API and the video appears on the profile with no human tap.

- Endpoint: `POST /v2/post/publish/video/init/`, scope `video.publish`.
- The video is uploaded either by chunked upload (`FILE_UPLOAD`, chunks 5–64 MB, final chunk up to 128 MB, upload URL valid 1 hour) or pulled from a verified domain (`PULL_FROM_URL`).
- The request must carry `post_info` (title/caption up to 2,200 UTF-16 code units, `privacy_level`, `disable_duet`, `disable_comment`, `disable_stitch`, `video_cover_timestamp_ms`) and `source_info` (file or URL).
- Status is checked with `POST /v2/post/publish/status/fetch/`.
- **Source: TikTok for Developers, "Content Posting API reference — Upload video" and "Content Posting API — Get started", read 2026-11-22.**

**Prerequisites** (from the same get-started guide):
1. A registered app on TikTok for Developers.
2. The Content Posting API product added to the app.
3. Direct Post enabled in the app settings.
4. The app approved for the `video.publish` scope.
5. The user authorizing the app for that scope.

**The audit gate — decisive.** The get-started guide states, verbatim: *"All content posted by unaudited clients will be restricted to private viewing mode."* Unaudited clients can only post `SELF_ONLY`, at most 5 users in 24 hours, and each account must be set to private at posting time. The audit lifts the restriction. **Source: TikTok for Developers, "Content Posting API — Get started", read 2026-11-22.**

**The intended-use test — the factory may fail it.** TikTok's Content Sharing Guidelines state that clients must (1) *"facilitate authentic creators posting original content"* and (2) *"must not be limited to test applications and should be intended for a wide audience, not limited to internal groups/private use."* The same page lists as explicitly not acceptable: *"A utility tool to help upload contents to the account(s) you or your team manages."* **Source: TikTok for Developers, "Content Sharing Guidelines", read 2026-11-22.** The factory is, by design, a tool that uploads content to one account its team manages. That is the exact shape TikTok says is not acceptable. Approval is therefore not something to plan on.

**Other rules from the same guidelines (read 2026-11-22):**
- Query creator info first (`POST /v2/post/publish/creator_info/query/`) to get the account's privacy options and maximum video duration, and respect them.
- The user must manually select the privacy setting — no default. The user must manually toggle comment/duet/stitch — none checked by default.
- Show the user a preview and get consent before uploading.
- No watermarks or logos on posted content. Videos must be the creator's own original content.
- Rate limit: 6 requests per minute per user access token **[secondary: skedcast.com — "TikTok Content Posting API"]**.
- Posting cap: about 15 posts per day per creator account, shared across all API clients **[secondary: vorp-labs.com — "TikTok Content Posting API"; blog.lots.social — "TikTok Content Posting API"]**. The factory's proposed cadence (1/day) is far below this.
- The request accepts an `is_aigc` flag to label AI-generated content **[secondary: vorp-labs.com]** — consistent with TikTok's Help Center requirement that realistic AI-generated content be labelled (see the experiment protocol).

**Video restrictions** (TikTok for Developers, "Media Transfer Guide", read 2026-11-22): MP4 (recommended), WebM, or MOV; H.264 (recommended), H.265, VP8, or VP9; 23–60 fps; 360–4096 px per side; max 4 GB; up to 10 minutes via the API, but the creator's own limit applies (every creator can post 3 minutes; some can post 5 or 10). The factory's videos (720×1280, 30 fps, H.264, MP4, ~90 s) fit comfortably inside every limit.

**App review:** scopes require review. The review asks for 1–5 demo videos (up to 50 MB each) showing the complete end-to-end flow with every requested scope demonstrated, plus a description of how each product and scope is used; unneeded scopes must be removed. TikTok publishes no firm review time; secondary guides report several days to two weeks. **[secondary: scrapeio.com — "How to Get a TikTok API Key"; easycoexistence.com — "TikTok App Review Rejected?"; tryadeli.com — "How to Get TikTok API Access"]** A sandbox exists for testing before review (up to 5 sandboxes, 10 target users, accounts the developer owns) **[secondary: scrapeio.com]**.

**What Mohamed would need to do:** create a TikTok developer account, register an app, add the Content Posting API, enable Direct Post, record the demo video, submit for review, then submit for the separate audit — and authorize the app on the TikTok account. The factory can prepare the app description, the scope justifications, and the demo script, but the registration and the authorization are human actions on TikTok's site.

**What it costs:** $0 as documented. No fee for a developer account, app registration, app review, or the audit appears in any TikTok documentation read for this research; no payment step exists in any documented flow. (That is absence of a fee in the docs, not a pricing page — if TikTok introduces a fee, it would appear at registration.)

**What remains unknown:** whether TikTok approves a single-account internal tool at all (the intended-use test says no); how long the audit takes (unpublished); whether the account's maximum video duration is 3 minutes (sufficient — videos are ~90 s).

---

## 4. Option B — Content Posting API, Upload (draft) mode

**What it is:** the factory uploads the video to the creator's TikTok inbox as a draft; the user finishes it in the TikTok app (adds the caption, sets privacy, taps post).

- Endpoint: `POST /v2/post/publish/inbox/video/init/`, scope `video.upload`.
- **Source: TikTok for Developers, "Content Posting API reference — Upload video", read 2026-11-22.**

**Why it matters:** it is the same API as Direct Post but without the audit gate's public-posting restriction — the video never goes public until a human finishes it in the app. The human tap is the safeguard TikTok wants, and it matches the factory's working model (Mohamed stays the publisher of record; the factory prepares everything).

**Limits:** at most 5 pending shares in any 24 hours; the user must tap the inbox notification to finish the post in TikTok. **[secondary: tokconnect — "Top 8 TikTok API Posting Tools"]** The factory's 1/day cadence is far below this.

**Prerequisites:** the same as Direct Post except the Direct Post setting and the audit: registered app, Content Posting API product, app approved for the `video.upload` scope, user authorization. **Source: TikTok for Developers, "Content Posting API — Get started", read 2026-11-22.**

**What Mohamed would need to do:** the same developer-account and app-registration steps as Option C (minus the audit), plus one tap in the TikTok app per video to finish the draft.

**What it costs:** $0 as documented (same basis as Option C).

**What remains unknown:** whether TikTok approves the `video.upload` scope for a single-account tool at review — the intended-use test applies to the app as a whole, so this is not certain either, but the draft mode is the less demanding ask and the one the factory should try first.

---

## 5. Login Kit / OAuth — what account access it grants and what it does not

**What it is:** TikTok's OAuth 2.0 login. A developer app gets a client key and secret; the user authorizes the app on TikTok; the app exchanges the authorization code server-side for an access token and a refresh token.

- Token endpoint: `POST https://open.tiktokapis.com/v2/oauth/token/`.
- **Access token lifetime: 2 hours. Refresh token lifetime: 180 days, and it rotates** — each refresh returns a different refresh token, and the stored one must be replaced every time; reusing a replaced refresh token fails and forces the user to authorize again.
- Token endpoints must be called server-side (the client secret must never be exposed); the app stores access token, refresh token, open_id, scope, and expiry times.
- **Source: TikTok for Developers, "Manage OAuth Access Tokens", last updated November 5, 2026, read 2026-11-22.**

**Scopes** (TikTok for Developers, "TikTok API scopes", read 2026-11-22):
- `user.info.basic` — open_id, avatar, display name (added by default).
- `user.info.profile` — bio, links, verified status.
- `user.info.stats` — follower, following, like, and video counts.
- `video.list` — the user's public videos.
- `video.upload` — send content to the user's drafts.
- `video.publish` — post directly to the user's profile.
- `video.manage` — view, edit, and delete published posts; `video.collab` — collaboration.

**Redirect URIs** (TikTok for Developers, "Login Kit — Web", read 2026-11-22): web redirect URIs must be HTTPS, absolute, static, with no query parameters, at most 10 URIs, each under 512 characters. For desktop apps the redirect URI may be a localhost URL, and PKCE is required. **This matters for the factory:** the VM has no public HTTPS endpoint, so the realistic OAuth route is a **desktop app type with a localhost redirect**, performed once with Mohamed's help (he authorizes in his own browser; the factory receives the code and stores the tokens). Login Kit is not a way for an agent to sign in as the user.

**What Login Kit does NOT grant:** it does not give the account password, does not allow reading direct messages, comments, or watch history, does not allow posting without the posting scopes, and does not give any analytics beyond the scopes listed above. It is a permissioned API key, not account control. The factory can never act as the user — it can only call the APIs the user authorized, within the scopes granted.

**Operational consequence of the 2-hour access token:** the factory's loop wakes every 6 hours, so the access token will usually be expired at wake time. That is fine: the loop refreshes it with the stored 180-day refresh token at the start of each run, then calls the API. No always-on server is needed — but the refresh token must be stored securely on the VM, rotated on every refresh, and never committed to the repo.

---

## 6. Display API — reading analytics (counts only)

**What it gives:** `POST /v2/video/query/` (scope `video.list`, up to 20 video IDs per call) returns, per video: id, create_time, cover_image_url, share_url, video_description, duration, height, width, title, embed_html, embed_link, **like_count, comment_count, share_count, view_count**. `user.info.stats` gives follower/following/like/video totals. **Source: TikTok for Developers, "Video Query", read 2026-11-22.**

**What it does NOT give:** average watch time, retention/completion curve, watched-full-video rate, traffic sources, search queries, follower demographics, or rewatches. Those live only in TikTok Studio. **[secondary: personaxpand.com — "How to Use TikTok Studio" (API vs Studio comparison)]**

**Consequence for the experiment protocol:** the two deciding metrics are comments/view (available from the API) and completion rate (available only from TikTok Studio). The factory can automate the counts; completion must always be read by a human from TikTok Studio and recorded into the experiment log with the read date. That is a permanent feature of the system, not a temporary gap.

**What is not applicable:** the TikTok Research API is a separate application for qualified academic and nonprofit researchers, and the TikTok API for Business is a separate portal for business accounts and advertising. The factory's account must be a **Personal** account for Creator Rewards eligibility, so the Business API is not the path for this account's organic analytics. **[secondary: scrapeio.com; tryadeli.com]**

---

## 7. Monetization status — how it is actually verified

**The only source is TikTok Studio → Monetization → Creator Rewards Program.** That screen shows eligibility and the application; TikTok generally replies within about three days of an application. **[secondary: biogpt.io — "TikTok Creator Rewards Explained"; socialappfix.com — "TikTok Creator Rewards Program: Requirements and Appeals"]**

**Eligibility (for reference, consistent across secondary guides citing TikTok's own Creator Academy page, last updated September 11, 2026):** 18 or older; Personal account (Business accounts are excluded); at least 10,000 followers; at least 100,000 video views in the last 30 days; based in an eligible country with the account registered there (the US, UK, Germany, France, Japan, South Korea, Brazil, and Mexico are named; other lists add Canada, Italy, Spain, Australia); original videos over 1 minute; at least 1,000 qualified For You views per video; account in good standing. TikTok Studio shows estimated rewards, qualified views, RPM, video eligibility, and performance trends; earnings estimates may take 1–3 days to appear after qualifying activity. **[secondary: biogpt.io; toptal.com — "How to Join the TikTok Creator Rewards Program in 2026"; lilachbullock.com — "How Much Does TikTok Pay?"; socialappfix.com]**

**What this means for the factory:** monetization status is UNKNOWN until Mohamed reads that screen for the actual account. The factory records it only in the allowed values from the experiment protocol (`UNKNOWN` / `NOT ELIGIBLE — reason` / `ELIGIBLE — NOT APPLIED` / `APPLIED — PENDING` / `ENROLLED — date` / `REJECTED — reason`). TikTok publishes no RPM, so no revenue forecast is ever written as a fact.

---

## 8. What is NOT a legitimate option

Named only to exclude them:

- **Unofficial scraping, crawling, or data extraction.** TikTok's Terms of Service (updated 2026-07-15) prohibit using automated systems to scrape, crawl, export, or extract data or content from the platform without TikTok's written approval. TikTok's own Privacy Center states: *"You may not use any automated scripts to collect information from, or interact with our services"* and *"You may not use another's TikTok account without their authorization."* **Source: TikTok Privacy Center, "Our approach to automated data collection" (tiktok.com), quoting the Terms of Service; corroborated by the Terms themselves as quoted in secondary reporting.**
- **Automation bots and "tricks designed to bypass our systems."** TikTok's Community Guidelines state: *"We strictly prohibit automation tools, scripts, or other tricks designed to bypass our systems"* — including fake engagement, follow/like/comment/DM bots, account farms, and engagement panels. Consequences run from content removal to account bans. **[secondary: lits (citing TikTok Community Guidelines); tokconnect]**
- **Credential-based automation** — logging in as the user with saved credentials and driving the app or website with a script (browser automation, anti-detect browsers, emulators) — is the same category: automation of the user interface instead of the official API. It is excluded for the same reason.
- **Buying views, followers, or engagement** is excluded by the same rules and by the Creator Rewards rules (artificial follower activity can affect eligibility; buying views or tampering with the program can get an account removed from it). **[secondary: socialappfix.com]**

**The rule in one line:** the factory may use only TikTok's official API surface (Content Posting API, Login Kit, Display API) and TikTok's own tools (the app, TikTok Studio). Anything else is not a shortcut — it is a risk to the account itself.

---

## 9. What Mohamed would need to do, per option

| Option | Mohamed's actions |
|---|---|
| **A. Manual (first)** | Create the dedicated TikTok account. Post each factory video from the app or TikTok Studio web (upload file, paste caption, set the AI-generated label, privacy Public, publish). Once a week, read the per-video numbers from TikTok Studio and pass them to the factory. Check TikTok Studio → Monetization → Creator Rewards when the account grows, and report what it shows. |
| **B. Upload (draft) API** | Everything in A, plus: create a TikTok developer account, register an app, add the Content Posting API, request the `video.upload`, `video.list`, `user.info.basic`, `user.info.stats` scopes, record the demo video, submit for app review, and authorize the app on the account (one browser authorization, desktop/localhost flow). After approval: one tap in the TikTok app per video to finish the draft. |
| **C. Direct Post API** | Everything in B, plus: enable Direct Post, request the `video.publish` scope, and submit for the separate audit — with the expectation, from TikTok's own guidelines, that a single-account internal tool may be rejected. |
| **D. Display API only** | The Login Kit authorization and the `video.list` scope (part of B's registration). No posting. |

The factory prepares everything it can (app description, scope justifications, demo script, caption, checklist). The registrations, the authorization, and the publishing taps are human actions on TikTok's own sites and cannot be done by the factory.

---

## 10. Cost table

| Item | Cost |
|---|---|
| TikTok developer account | $0 — no fee found in any TikTok documentation |
| App registration | $0 — no fee found |
| App review (scopes) | $0 — no fee found |
| Content Posting API audit | $0 — no fee found; no published timeline |
| Content Posting API use (Direct Post / Upload) | $0 — no fee found; no paid tier found |
| Login Kit / Display API | $0 — no fee found |
| TikTok Studio (app and web) | $0 — no paid tier found |

No paid tier, subscription, or credit balance was found for any of these. If TikTok introduces a fee, it would appear at registration — and the zero-spend rule means the factory stops and asks before paying anything.

---

## 11. Recommended first path

1. **Start with Option A (manual publishing) from day one.** The account is safe, nothing needs approval, and the experiments can begin the day the account exists. The factory's job is to make the manual step trivial: one video file, one caption, one checklist, one tap.
2. **In parallel, pursue Option B (Upload / draft API).** Register the developer app, request `video.upload` + `video.list` + `user.info.basic` + `user.info.stats`, test in the sandbox, and submit for review. If approved, the factory uploads drafts and Mohamed finishes them with one tap — the upload is automated, the publish stays human.
3. **Treat Option C (Direct Post) as a bonus, not the plan.** The audit's intended-use test explicitly rejects a utility tool that uploads content to the account(s) its team manages. Apply for it if the app is approved for the other scopes, but do not design the factory around it.
4. **Analytics from the start:** Display API for counts once the scopes are approved; **TikTok Studio, read by a human, for completion rate, watch time, traffic, and monetization status — permanently**, because no API provides them.

---

## 12. Open questions

1. **The single biggest open question: will TikTok approve a single-account internal app for the posting scopes — and pass the Direct Post audit — given that its Content Sharing Guidelines explicitly say a client must be "intended for a wide audience, not limited to internal groups/private use" and that a "utility tool to help upload contents to the account(s) you or your team manages" is not acceptable?** The legitimate API path may end at the review/audit gate. That is why the manual path is first.
2. How long does the app review take, and how long does the audit take? TikTok publishes no timeline for either.
3. Will the dedicated account be a Personal account registered in an eligible country (required for Creator Rewards)? Unknown until the account exists and TikTok Studio → Monetization is read.
4. Does the factory need a public website with terms and privacy policy URLs for app review? Secondary guides report that apps created after 9 September 2024 must verify their terms, privacy policy, and web URLs, and that review rejects landing-page-only sites — the factory has no public website. **[secondary: scrapeio.com; tryadeli.com]**
5. Is the `is_aigc` flag required on Direct Post requests, or is the in-app AI label toggle sufficient? The flag is reported in secondary sources; TikTok's own Help Center requires the label for realistic AI content. **[secondary: vorp-labs.com; TikTok Help Center via the niche discovery]**
6. The account's maximum video duration (3 minutes for every creator; some get 5 or 10). The factory's ~90-second videos fit either way, so this is a check, not a risk.

---

## 13. Sources

Primary (TikTok's own documentation and site), read 2026-11-22:
- Content Posting API — Get started: https://developers.tiktok.com/doc/content-posting-api-get-started — two modes (Direct Post, Upload), prerequisites, unaudited clients restricted to private viewing (SELF_ONLY, ≤5 users/24h, accounts private), creator-info query first, post_info/source_info fields, status fetch.
- Content Posting API reference — Upload video: https://developers.tiktok.com/docs/en/content-posting-api-reference-upload-video — `video/init/` and `inbox/video/init/` endpoints, `video.publish` and `video.upload` scopes, chunked upload details.
- Media Transfer Guide: https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide — video formats/codecs, 23–60 fps, 360–4096 px, max 4 GB, up to 10 min via API (creator limit applies), chunk sizes 5–64 MB (final up to 128 MB), upload URL valid 1 hour.
- Content Sharing Guidelines: https://developers.tiktok.com/docs/en/content-sharing-guidelines — intended-use test (authentic creators, wide audience, not internal/private use), explicitly unacceptable single-account upload utility, manual privacy selection, manual duet/comment/stitch toggles, preview and consent, no watermarks.
- TikTok API scopes: https://developers.tiktok.com/doc/tiktok-api-scopes — `user.info.basic` (default), `user.info.profile`, `user.info.stats`, `video.list`, `video.upload`, `video.publish`, `video.manage`, `video.collab`.
- Login Kit — Overview: https://developers.tiktok.com/docs/en/login-kit-overview — OAuth 2.0, register app, Login Kit product, redirect URI configuration.
- Login Kit — Web: https://developers.tiktok.com/docs/en/login-kit-web — redirect URI rules (HTTPS, absolute, static, no query params, ≤10, <512 chars), desktop apps may use localhost, PKCE required for desktop.
- Manage OAuth Access Tokens: https://developers.tiktok.com/doc/oauth-user-access-token-management — access token 2 hours, refresh token 180 days and rotating, server-side token calls, stored values.
- Video Query (Display API): https://developers.tiktok.com/docs/en/tiktok-api-v1-video-query — `video/query/`, scope `video.list`, max 20 IDs, returns view/like/comment/share counts, duration, create_time, title, etc.
- TikTok Privacy Center — "Our approach to automated data collection": https://www.tiktok.com/safety/en/our-approach-to-automated-data-collection/ — Terms of Service prohibit automated scripts to collect information or interact with the services, and using another's account without authorization.
- TikTok Studio: https://www.tiktok.com/tiktokstudio — the web creator hub (upload, scheduling, analytics, monetization).

Secondary (guides quoting TikTok; used only where TikTok's own pages do not state the point):
- https://www.tryadeli.com/blog/how-to-get-tiktok-api-access — two developer portals, app-review steps, website requirements.
- https://scrapeio.com/blog/how-to-get-a-tiktok-api-key — demo videos (1–5, ≤50 MB), sandbox (5 sandboxes, 10 target users), URL verification, no published review time, token lifetimes.
- https://easycoexistence.com/docs/tiktok/app-review-rejected — app-review checks, demo-video requirements, "several days to two weeks".
- https://bundle.social/blog/tiktok-api-vs-instagram-api-vs-youtube-api — approval timeline 1–4 weeks.
- https://www.vorp-labs.com/tiktok-content-posting-api — 15 posts/day cap, `is_aigc` flag.
- https://blog.lots.social/blog/tiktok-content-posting-api — 15 posts/day cap, unaudited restrictions.
- https://tokconnect.app/blog/top-8-tiktok-api-posting-tools — Upload mode 5 pending shares/24h, sandbox limits.
- https://www.skedcast.com/blog/tiktok-content-posting-api — 6 requests/min rate limit.
- https://personaxpand.com/blog/how-to-use-tiktok-studio — TikTok Studio tabs and per-video metrics; what the API does not provide.
- https://sociality.io/blog/tiktok-studio/ and https://trackmedia.co/blog/tiktok-studio-review — TikTok Studio analytics structure, date ranges, downloads.
- https://www.schedulenchill.com/blog/how-to-upload-videos-to-tiktok-from-your-pc — web uploader limits (10 GB, 30 min).
- https://instantdm.io/blog/the-only-legitimate-ways-to-post-to-tiktok — native scheduler / Content Posting API as the only legitimate posting routes.
- https://www.biogpt.io/tiktok-creator-rewards-explained-how-it-works-and-pays-creators/ — Creator Rewards eligibility, Studio → Monetization check, ~3-day reply.
- https://www.toptal.com/creator/post/how-to-join-the-tiktok-creator-rewards-program — eligibility, application steps.
- https://www.lilachbullock.com/how-much-does-tiktok-pay/ — Creator Academy country list (8 countries), eligibility table, no published RPM.
- https://socialappfix.com/tiktok/creator-rewards-not-eligible/ — eligibility, appeal windows, buying views/followers can remove an account from the program.
- https://www.affiversemedia.com/tiktok-creator-monetization-guide/ — Studio → Monetization application path.
- https://lits (TikTok Community Guidelines, as quoted) — "We strictly prohibit automation tools, scripts, or other tricks designed to bypass our systems."
