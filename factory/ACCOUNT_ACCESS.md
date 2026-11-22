# Account Handover & Access Protocol — how the factory takes over and uses a TikTok account without being detected as a robot

**Status:** written 2026-11-22, **before any account has been handed over.
No account exists yet. Nothing here has been used on a real account.**
This file is the operating protocol the factory follows the moment an
account is handed to it. It is binding on every run that touches a
TikTok account.

**Current situation (2026-11-22):** Mohamed is registering a clean
British TikTok account in his own browser and will hand it over. The
Muse cloud browser window on the TikTok signup page was closed —
registration happens in Mohamed's browser, not in the factory's.
The registration country is therefore the UK, verified from the
account itself at handover. "British" implies nothing beyond that
fact: not the audience, not the content, not monetization
eligibility. Those are discovered and verified, never assumed (§7).

**Purpose:** make the factory's access to a TikTok account
indistinguishable, in TikTok's own terms, from a legitimate
authorized tool: the factory touches the account only through
TikTok's official surfaces, at a human pace, with the owner's
authorization, and never by any means TikTok classifies as
automation or evasion. The account's standing is the asset; this
protocol protects it.

---

## 0. The principle — legitimate access is the only access

1. **The factory accesses a TikTok account ONLY through TikTok's
   official surfaces** (see §1): Login Kit OAuth, the Content
   Posting API (Upload / draft mode first), the Display API, and
   TikTok's own app and TikTok Studio for human steps. There is no
   other route. If a task cannot be done through these surfaces, it
   is not done — it is recorded as a gap, and the factory asks for
   the human step instead.
2. **Evasion is not a solution. Evasion is itself a detection
   signal.** Every technique that exists to hide automation from
   TikTok is a thing TikTok's detection is built to find. Using one
   trades a small convenience for the account's standing.
3. **The factory never pretends to be a human.** It is an authorized
   tool acting on the owner's behalf, within the scopes the owner
   granted, at a pace a human owner would recognise. The difference
   between a legitimate tool and a bot is not speed — it is
   authorization, official surfaces, and restraint (§4).
4. **A restriction is information, not an obstacle to route around**
   (§5). If TikTok challenges, rate-limits, or restricts an action,
   the factory stops, records, and escalates. It never switches to
   another route to get the same result.

---

## 1. Legitimate surfaces — the only ways the factory touches an account

| Surface | What the factory uses it for | What it never does |
|---|---|---|
| **Login Kit (OAuth 2.0)** | Identity and authorization: the owner authorizes the factory's developer app in his own browser; the factory receives tokens, never the password (§2.1). | Never used to sign in *as* the user. Login Kit is a permissioned API key, not account control (see `research/tiktok-connection-2026-11-22.md` §5). |
| **Content Posting API — Upload (draft) mode** | Upload a finished video to the creator's inbox as a draft (`video.upload` scope). The owner finishes it in the app: caption, privacy, AI label, publish tap (§4.4). | Never used to publish directly until and unless the `video.publish` scope is approved and the audit passed — which the connection research says is unlikely for a single-account internal tool. Direct Post is a bonus, never the plan. |
| **Display API** | Read per-video counts (`video.query/`, `video.list` scope) and account totals (`user.info.stats`). | Never used to infer what it does not return: no completion rate, no retention curve, no traffic source, no demographics, no rewatches. Those live only in TikTok Studio. |
| **TikTok app / TikTok Studio (human steps)** | Publishing taps, privacy selection, the AI-generated label toggle, reading retention, traffic, search queries, demographics, and the Monetization → Creator Rewards status. | Never automated. These are the owner's actions, in TikTok's own interfaces, exactly as TikTok designed them. |

**Scopes requested, and no more** (see `research/tiktok-connection-2026-11-22.md` §5):
`user.info.basic` (default), `user.info.stats`, `video.list`,
`video.upload`. `video.publish` only if and when the Direct Post
audit is attempted. Unneeded scopes are removed before review —
requesting more than the factory uses is itself a review risk.

---

## 2. Forbidden routes — named, with why each gets detected

Each of these is forbidden, always, for any account. The reason is
not only that TikTok's Terms of Service prohibit them — it is that
each one is precisely what TikTok's detection is built to find, so
using one increases the chance of exactly the outcome Mohamed asked
to avoid: the factory being flagged as a robot.

| Forbidden route | Why it is detected — and why it is not a solution |
|---|---|
| **Scraping / crawling / automated data extraction** | TikTok's Terms of Service (updated 2026-07-15) prohibit using automated systems to scrape, crawl, export, or extract data or content without TikTok's written approval. The Privacy Center states: *"You may not use any automated scripts to collect information from, or interact with our services."* Request patterns, volume, and missing browser behaviour identify scrapers. Use the Display API and TikTok Studio instead. |
| **Automation bots** (follow/like/comment/DM bots, engagement panels, account farms) | The Community Guidelines state: *"We strictly prohibit automation tools, scripts, or other tricks designed to bypass our systems."* Bots act at machine regularity, in machine volumes, on machine schedules. Consequences run from content removal to account bans. The factory's cadence (§4.1) exists to stay far below any behaviour that looks like this. |
| **Credential-based browser automation** (logging in as the user with saved credentials and driving the app or website with a script) | This is automation of the user interface instead of the official API. It leaves the same signals — scripted input timing, headless/browser-automation fingerprints, session patterns — while carrying the extra risk of the account's password being used by a machine. The factory never signs in as the user. Authorization happens through Login Kit; the password never reaches the factory (§2.1). |
| **Emulators and anti-detect browsers** | These exist to fake a device. TikTok's detection includes device and environment signals; an environment built to look like a device it is not is itself anomalous. A desktop OAuth flow and the official API have no device to fake. |
| **Fingerprint spoofing** (forged canvas, WebGL, font, timezone, or hardware fingerprints) | Inconsistency is the signal. A fingerprint whose parts disagree with each other — or with the network and account signals — is more detectable than an honest one. The factory presents its real server-side API identity: a registered developer app, an authorized token, a declared user agent. |
| **Proxies / VPNs used to fake location** | A registration or access location that disagrees with the account's other signals (phone, SIM, payment method, language, time zone, the owner's own location) is an inconsistency TikTok can see, and misrepresenting location is a misrepresentation. The account's registration country is recorded as a fact (§7); it is never faked, and it is never "fixed" afterwards with a proxy. |
| **Buying views, followers, or engagement** | Banned by the Community Guidelines and by the Creator Rewards rules; artificial follower activity can affect eligibility, and buying views or tampering with the program can get an account removed from it. Bought numbers also corrupt the experiment protocol — the factory would be measuring money, not audience. |

**The test, applied before any new technique is adopted:** "Is
this TikTok's official surface, used as TikTok designed it, with
the owner's authorization?" If the answer is not yes, the technique
is not used. If the answer is uncertain, the technique is not used
until the uncertainty is resolved by reading TikTok's own
documentation — not by a vendor's claim that it is undetectable.

---

## 3. Handover procedure — what happens the moment an account is handed over

Handover is a checklist, run in order, before any strategy or
publish decision. The per-account diagnosis
(`factory/ACCOUNT_DIAGNOSIS.md`) is not started until this procedure
completes. No video is published, no experiment is run, and no
strategy is chosen before step 4.

### 3.1 Step 1 — Verify identity through official authorization

Two routes, in order of preference. Route A is the default; Route B
exists only if Mohamed explicitly chooses it for a specific handover.

**Route A — Login Kit authorization (preferred).**
1. The factory's developer app is registered and approved for the
   scopes in §1 (see `research/tiktok-connection-2026-11-22.md` §9
   for what Mohamed does: developer account, app registration, scope
   review, one browser authorization).
2. Mohamed authorizes the app **in his own browser**, on TikTok's
   own authorization page, for the scopes listed in §1. The factory
   never sees the authorization page, never receives a password, and
   never handles the owner's login session.
3. The factory receives, server-side, the authorization code, and
   exchanges it for the access token and refresh token (§4, token
   hygiene). The redirect is a desktop-app localhost redirect with
   PKCE (the VM has no public HTTPS endpoint; see the connection
   research §5).
4. The factory confirms the authorization by calling the API for the
   account's own basic info (§3.2) — one call, one purpose.

**Route B — Login credentials, only through the Secure Vault, used once.**
1. If Mohamed hands over login credentials instead, they arrive
   **only through the Secure Vault** (the secure capture page, never
   chat, never a file, never memory). No credential value is ever
   written into a file, a chat message, a memory entry, or the repo.
2. The credentials are used **once**, for the single purpose of
   completing the official authorization (Route A) — i.e. signing in
   on TikTok's own site so the Login Kit authorization can happen.
   They are not used to drive the account afterwards, and they are
   not used to log in through any script or automation.
3. After the authorization completes and tokens are stored (§4),
   the credentials are discarded from the factory's working state.
   The tokens are the access mechanism from then on; the password is
   never needed again and never asked for again.
4. If the authorization cannot be completed with the credentials
   provided (wrong password, extra verification factor the factory
   cannot complete, account challenge), the factory stops, records
   exactly what happened, and escalates to Mohamed. It does not
   retry, does not guess, and does not try another route.

**What handover is NOT:** it is not the factory receiving the
account's password as a standing credential, not a shared login the
factory uses day to day, and not permission to act as the user. The
factory acts as an authorized tool, within granted scopes, or not
at all.

### 3.2 Step 2 — Confirm the account's own facts

One API call (or one Studio read where the API does not provide it),
recorded verbatim in `accounts/<handle>/DIAGNOSIS.md` §1 with the
date:

- `open_id` (the API identity — the factory's handle for this
  account from now on; the display name is not an identity).
- Display name and handle, as the account itself shows them.
- Account type: Personal / Business (Creator Rewards requires
  Personal; if the account is Business, that is recorded as a
  constraint and a decision for Mohamed, not something the factory
  changes silently).
- Follower / following / video counts at handover (a baseline, not a
  judgement).
- Creation date and account age, if visible.
- Any strikes, removals, or reviews already on the account, if
  visible.

If any fact cannot be confirmed from the account itself, it is
recorded as unknown — never filled in from what Mohamed remembers,
from another account, or from an assumption.

### 3.3 Step 3 — Read TikTok Studio → Monetization for the ACTUAL account

1. Mohamed (the person holding the account) reads TikTok Studio →
   Monetization → Creator Rewards Program for this account, and
   reports exactly what it shows.
2. The factory records the status using **only** the allowed values
   from `EXPERIMENTS.md` §7: `UNKNOWN` · `NOT ELIGIBLE — <reason as
   Studio states it>` · `ELIGIBLE — NOT APPLIED` · `APPLIED —
   PENDING` · `ENROLLED — <date>` · `REJECTED — <reason>`. Nothing
   else. The read date is recorded with the status.
3. **Never assume eligibility from the registration country** (§7).
   The UK being on the eligible-country list is a reason to check,
   not a result.
4. Until this step is done, the status stays `UNKNOWN` — in the
   diagnosis file, in the experiment log, and in every report.

### 3.4 Step 4 — Run the per-account diagnosis before any strategy or publish decision

Open `accounts/<handle>/DIAGNOSIS.md` from the template
(`factory/ACCOUNT_DIAGNOSIS.md`) and fill it in full: account facts
(§3.2), audience known/unknown, capabilities, constraints,
strategy hypothesis (with falsifier), monetization status (§3.3),
advantage map (empty at this point), assumption register, what is
NOT assumed, benchmark record (empty), the four audience tests
(unknown at this point), next actions.

**The rule from `ADVANTAGE.md` §1 applies here:** no strategy is
chosen before the diagnosis, and no strategy transfers between
accounts by assumption. The trivia-vs-riddles comparison (EXP-001 /
EXP-002) is published as the first *learning instruments* about this
account — with the explicit note that their strategy comes from desk
research, not from this account's data — only after the diagnosis
is written.

### 3.5 Handover checklist (all four, in order, before first publish)

- [ ] Authorization completed through Login Kit (Route A), or once
  through the Secure Vault (Route B) and tokens stored (§4).
- [ ] Account facts confirmed from the account itself and recorded
  in `accounts/<handle>/DIAGNOSIS.md` §1 with the date.
- [ ] TikTok Studio → Monetization read for this account; status
  recorded with the date (or `UNKNOWN` with the reason it has not
  been read yet).
- [ ] Per-account diagnosis completed; no strategy chosen before it.

---

## 4. Token hygiene — the rules that keep access working and secret

| Rule | Detail |
|---|---|
| **Server-side only** | Token endpoints are called server-side. The client secret is never exposed — never in a URL, never in a browser, never in a log, never in the repo. |
| **Access token: 2 hours** | The loop wakes every 6 hours, so the access token will usually be expired at wake time. That is expected. The run refreshes it first, then calls the API. |
| **Refresh token: 180 days, rotating** | Each refresh returns a **different** refresh token. The stored one must be replaced on every refresh. **Never reuse a replaced refresh token** — reusing one fails and forces the owner to authorize again. |
| **Refresh at the start of each run** | The first action of any loop run that touches TikTok is: refresh the access token with the stored refresh token, store the new pair, then proceed. No API call is made with a token whose expiry has not been checked. |
| **Storage** | The refresh token lives in secure storage on the VM (the approved secure store), never in the repo, never in a file under `~/workspace/muse-repo/`, never in chat, never in a memory entry, never in a log. Its value is never printed, never pasted, never quoted — not even in part. |
| **Scope discipline** | The factory calls only the APIs the granted scopes cover. A call outside the granted scopes is not attempted "to see if it works" — an unauthorized-scope error is a signal, not a test. |
| **Revocation** | If tokens are lost, leaked, or suspected leaked: stop all TikTok calls immediately, record what happened, escalate to Mohamed, and let the owner revoke and re-authorize. Do not attempt to "recover" access by another route. |
| **No credential in the repo, ever** | No password, token, secret, or key is ever committed to the GitHub repo. The sync record lists text files only; a file containing a credential is never pushed. If a credential is found in a file that was about to be pushed, the push is cancelled and the file is removed. |

---

## 5. Behaviour rules — acting like a legitimate authorized tool

These rules are what keep the factory's API use from looking like a
bot's. They are limits the factory imposes on itself, below TikTok's
own caps, because the margin is the safety.

### 5.1 Cadence and volume

- **1 video per day, 7 per week** (the experiment protocol's
  cadence, `EXPERIMENTS.md` §8). This is far below the API caps:
  about 15 posts/day per creator account for Direct Post, and 5
  pending shares per 24 hours for Upload (draft) mode. The caps are
  not a target; the cadence is.
- **No burst.** One upload per run at most, and never two uploads
  back-to-back. A day's video is prepared, verified, and uploaded
  once. If an upload fails, it is recorded and retried once, after
  the cause is understood — not immediately, not repeatedly.
- **No mass actions.** No bulk follows, likes, comments, or messages.
  The factory does not follow, like, or comment on other accounts at
  all — its only outbound actions are the authorized upload and the
  authorized read calls.
- **No duplicate submissions.** Before any upload, check whether the
  same video is already pending or published (by video ID and by
  content hash). A retry after an ambiguous failure is preceded by a
  status check (`POST /v2/post/publish/status/fetch/`), never by
  re-sending the upload.

### 5.2 Rate limits

- **6 requests per minute per user access token** (Content Posting
  API, per the connection research §3, secondary source). The
  factory stays well under it: at most one API call per minute in
  normal operation, with a pause between calls. A 429 response is a
  hard stop for that provider in this task — no retry, no
  workaround, record it and escalate if it recurs.
- **Read calls are batched, not polled.** The Display API
  `video/query/` accepts up to 20 video IDs per call. The factory
  reads counts in one batched call per run, not one call per video,
  and never polls TikTok for updates. Measurement happens on the
  experiment schedule (7 days after publish), not continuously.

### 5.3 Human-in-the-loop — the owner is the publisher of record

- **Every publish is a human tap** until and unless the Direct Post
  path is approved. The factory uploads a draft; Mohamed finishes
  it in the app. The human tap is the safeguard TikTok wants, and
  it is also the safeguard the factory wants: no video goes public
  without a person having seen the final form.
- **Privacy selection is the owner's, every time.** No default
  privacy level is assumed. The owner selects Public at publish
  time (per the experiment protocol's checklist).
- **The AI-generated label toggle is the owner's, every time.**
  Every factory video is labelled as AI-generated where TikTok
  requires it (the `is_aigc` flag on API upload, the in-app toggle
  on publish). The toggle is never pre-set by the factory and never
  skipped.
- **Comment / duet / stitch settings are the owner's choice per
  video**, recorded in the experiment log. The factory proposes; the
  owner decides at publish time.
- **No action the owner did not authorize.** The factory does not
  change the profile, bio, links, profile picture, username, or any
  account setting. It does not reply to comments, send messages, or
  interact with other accounts. Its authorized scope is: upload
  drafts, read counts. Anything else is a request to the owner, not
  an action.

### 5.4 What the factory never does on the account

- Never logs in as the user through a browser or script.
- Never uses the account's session outside the official API.
- Never posts, deletes, or edits a published video except through
  the authorized API scopes and with the owner's decision recorded.
- Never touches direct messages, comments, watch history, or
  followers' data — the granted scopes do not cover them, and the
  factory does not go looking for them.
- Never runs any action while a challenge, rate limit, or
  restriction is in force (§6).

---

## 6. Detection-response procedure — when TikTok pushes back

A challenge, a rate limit, a rejection, or a restriction is
**information, not an obstacle to route around.** It tells the
factory something about how its access is being seen. The response
is always the same, in this order:

1. **STOP the action immediately.** Do not retry. Do not retry
   faster, slower, or from a different route. Do not switch to
   manual publishing to get the same video out the same day unless
   the owner decides that — the restriction may apply to the
   account, not to the route, and working around it is exactly what
   gets accounts flagged.
2. **Record exactly what happened.** Timestamp (UTC), the action
   attempted, the endpoint or surface, the exact response or message
   TikTok returned (verbatim, no paraphrase), the token state at the
   time (was it freshly refreshed?), and what had just happened
   before it. The record goes in the account's diagnosis file and in
   the run log. A restriction with no record is a lesson lost.
3. **Check the obvious, legitimate causes first.** Expired token?
   Replaced refresh token reused? Scope not granted? App review
   expired? Video outside the format limits? Account-level issue
   (strike, review, private setting)? Each is checked against the
   documentation, not guessed at.
4. **Escalate to Mohamed with the facts.** What was attempted, what
   TikTok said (verbatim), what the factory has checked, and what
   the factory proposes — including "wait and do nothing" as a
   serious option. The escalation is a report, not a question that
   transfers the work: the factory prepares the next step, the
   owner decides whether it happens.
5. **Do not resume the restricted action until the cause is
   understood and the owner has decided.** If the cause was a token
   error, re-authorization is the owner's action. If the cause was a
   rate limit, the factory waits out the window and reduces its own
   pace further. If the cause was a policy or review issue, the
   factory stops that line of work entirely until the owner decides.

**What is never done in response to a restriction:**
- Never retry aggressively or in a tight loop.
- Never switch to scraping, credential-based automation, an
  emulator, an anti-detect browser, a proxy, or a VPN to get around
  it.
- Never create a second account to work around it. One restriction
  on one account is not a reason to open another.
- Never delete evidence of the restriction, and never reword
  TikTok's message to sound less serious than it is.

---

## 7. Registration-country note — what "British" does and does not imply

Record the account's registration country as a fact, verified from
the account itself at handover (§3.2). The country implies
**nothing else**:

| It is a fact | It is NOT evidence of |
|---|---|
| The country the account was registered in (UK, for the account Mohamed is registering in his own browser). | The audience. A UK-registered account can be watched anywhere; the audience is discovered from TikTok Studio (traffic sources, demographics, search queries) once the account has viewers. |
| | The content. English-language content for a US audience is a strategy choice, recorded in `STATE.md`; the registration country does not choose it. |
| | Monetization eligibility. The UK is on TikTok's Creator Rewards eligible-country list **per current research** (secondary sources citing TikTok's Creator Academy page; the Help Center page does not enumerate the list, and secondary lists disagree on the full set). Eligibility is **only** established by reading TikTok Studio → Monetization for the actual account (§3.3). Until that read, the status is UNKNOWN — including for a UK account. |
| | The account's standing. A clean registration is a starting point, not a guarantee. Standing is earned by what the account does afterwards, under this protocol. |

**Why this note exists:** the previous plan was blocked because
the Muse cloud browser egresses from Fez, Morocco, and an account
created from it would likely have registered as Moroccan — and
Morocco is not on the current Creator Rewards country list. Mohamed
is now registering the account in his own browser, in the UK. That
changes the registration country, and only the registration country.
It does not change the factory's job: verify everything from the
account itself, assume nothing from a label — including the label
"British".

**The country decision is made before creation, not after.**
Registration country is set at creation; it is not "fixed"
afterwards with a proxy, a VPN, or a settings change. If the
registration country turns out to be wrong for the factory's goals,
the decision is Mohamed's, and it is made with the facts in front
of him — not by the factory working around it.

---

## 8. How this protocol connects to the rest of the factory

| This protocol | Connects to | How |
|---|---|---|
| Handover (§3) | `factory/ACCOUNT_DIAGNOSIS.md` | Handover fills the diagnosis file. No diagnosis, no strategy (`ADVANTAGE.md` §1). |
| Handover (§3.3) | `factory/EXPERIMENTS.md` §7 | The monetization status recorded here is the only status the experiment log may use. |
| Token hygiene (§4) | `research/tiktok-connection-2026-11-22.md` §5 | Token lifetimes, rotation, and the localhost-redirect OAuth route come from the connection research. This protocol is the operating rule built on top of it. |
| Behaviour rules (§5) | `factory/EXPERIMENTS.md` §3, §8 | The publishing checklist and the 1/day cadence are the experiment protocol's rules; this protocol adds the API-side limits (rate, duplicates, batching) that keep the account looking like a legitimate authorized tool. |
| Detection response (§6) | `factory/ADVANTAGE.md` §7 | A restriction is an asset-protection event. The check in ADVANTAGE §7.2 applies: if every competitor did this and TikTok enforced its own rules, would the account still be standing, eligible, and trusted? |
| Registration country (§7) | `factory/ACCOUNT_DIAGNOSIS.md` §4 | The registration-country warning in the diagnosis template is replaced, at handover, by the verified fact and the route actually used. |

---

## 9. Current status — honest, 2026-11-22

| Item | State |
|---|---|
| Accounts handed over | **0.** No account has been handed to the factory yet. |
| Authorizations completed | **0.** No Login Kit authorization has happened. No tokens exist. |
| Developer app | **Not registered.** No developer account, no app, no scope review, no audit. The connection research (§9) lists what Mohamed would need to do; none of it has been done. |
| Handover route | **To be decided at handover.** Route A (Login Kit) is the default; Route B (Secure Vault credentials, used once) only if Mohamed explicitly chooses it. |
| Registration country | **UK (expected).** Mohamed is registering a clean British account in his own browser. To be verified from the account itself at handover (§3.2). |
| Monetization status | **UNKNOWN.** No account exists to read it from. |
| First actions when the account arrives | Handover checklist (§3.5), in order — then the per-account diagnosis, then EXP-001/EXP-002 as learning instruments. |

This protocol is itself subject to the factory's re-audit rules: it
is re-checked at every horizon scan and every learning review, and
whenever TikTok changes its documentation, its scopes, its rate
limits, or its policies. A rule in this file that TikTok's own
documentation contradicts is wrong, and is corrected — the
documentation is the authority, not this file.
