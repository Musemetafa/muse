# Niche Formats vs Proven Stack — Fit Assessment

**Date:** 2026-11-22
**Purpose:** Judge faceless TikTok formats against ONLY the stack measured on this VM. No invented capabilities.

## Proven stack (measured, 2026-11-22)

- **OpenFilm render:** deterministic 720×1280, 30 fps, code-computed motion (slide-in, growth, bounce, travelling elements). ~5.5 s render for a 6 s video via ffmpeg path; Chromium-based render ~29–34 s. No GPU.
- **Kokoro-82M TTS via kokoro-onnx:** US-English voice, RTF 2.67 (slower than real time), peak RSS 665 MB, WER 0.000 on transcription back-check. Naturalness not yet blind-tested.
- **faster-whisper tiny.en:** captions with word timestamps, RTF 0.20.
- **Not available:** no real video footage, no camera, no human voice, no paid APIs, no image-generation model proven yet.

Implication: any format that needs photographic imagery, filmed footage, realistic illustration, or a human face/voice is **not** producible with this stack today. Formats carried by text, typography, shapes, numbers, and a single TTS voice **are**.

## Format-by-format judgement

### 1. Trivia / quiz — FIT: STRONG
- **Assets needed:** question text, 3–4 answer options, timer bar, reveal animation. All typographic.
- **Stack carries it?** Yes. Code motion (option slide-ins, countdown bar, correct-answer highlight) + TTS question read + word-timed captions.
- **Weak point:** visual sameness across videos; risk of looking like every other quiz account. Needs distinct motion language (e.g. a signature reveal mechanic) and genuinely hard or surprising questions, not trivia anyone can Google in 2 s.
- **Repeatability:** Very high — question bank is effectively unlimited.
- **Differentiation:** questions with a twist (the "obvious" answer is wrong), a consistent visual identity, difficulty tiers, series arcs (e.g. "beat the 1%").

**10 concrete ideas:**
1. "Only 1% know this: which country has the most pyramids?" (answer: Sudan, not Egypt)
2. "Which of these animals is NOT a mammal? — with a 10-second countdown"
3. "Guess the US state from its shape alone" (shape drawn as code outline)
4. "True or false: honey never spoils — answer revealed with a fact twist"
5. "Which planet has the shortest day? Jupiter — 10 hours"
6. "Name the odd one out: apple, banana, strawberry, tomato" (botanical berries)
7. "What year was the first iPhone released? 2007 — with era context"
8. "Which ocean is the largest by surface area? Pacific — with a scale comparison"
9. "How many sides does a dodecagon have? 12 — with a shape building itself on screen"
10. "Which US president is on the $2 bill? Jefferson — with a money-zoom reveal"

### 2. "Did you know" facts — FIT: STRONG
- **Assets needed:** one surprising fact, a big number or keyword on screen, a simple supporting visual (shape, counter, diagram).
- **Stack carries it?** Yes. Single-fact videos are the easiest fit: TTS narration + kinetic text + a counting/zooming graphic.
- **Weak point:** facts alone are commodity content; thousands of accounts do this. Needs facts that are verifiable and genuinely surprising, not recycled listicle filler.
- **Repeatability:** Very high — one fact per video, endless supply.
- **Differentiation:** source the fact on screen ("NASA, 2023"), pick facts with a visualisable number, end with a "wait, why?" hook that earns a rewatch.

**10 concrete ideas:**
1. "Bananas are berries, but strawberries aren't" (botanical definition)
2. "Octopuses have three hearts — and two stop beating when they swim"
3. "The Eiffel Tower grows about 15 cm taller in summer" (thermal expansion, animated)
4. "There are more possible chess games than atoms in the observable universe"
5. "Wombat poop is cube-shaped" (with a cube diagram)
6. "Sharks existed before trees"
7. "Your body produces about 25 million new cells every second" (counter animation)
8. "The first oranges weren't orange — they were green" (Southeast Asia origin)
9. "A day on Venus is longer than a year on Venus"
10. "Honey never spoils — 3,000-year-old jars are still edible"

### 3. Riddles / puzzles — FIT: STRONG
- **Assets needed:** riddle text revealed line by line, a timer, answer reveal. Pure typography.
- **Stack carries it?** Yes — arguably the best fit. Suspense is built by pacing text reveals and TTS pauses, both code-controlled.
- **Weak point:** riddle quality is everything; weak or well-known riddles get scrolled past. Also needs a fair "solve it yourself" pause that doesn't feel like dead air.
- **Repeatability:** High — large public-domain riddle corpus, plus logic puzzles.
- **Differentiation:** original riddles written for the format, a signature "3 clues, 10 seconds" structure, answers that reframe the question.

**10 concrete ideas:**
1. "I speak without a mouth and hear without ears. What am I?" (echo)
2. "The more of me you take, the more you leave behind. What am I?" (footsteps)
3. "What has keys but can't open a single lock?" (piano)
4. "A man is found dead in a field with an unopened package. What happened?" (parachute)
5. "What comes once in a minute, twice in a moment, but never in a thousand years?" (the letter M)
6. "Forward I'm heavy, backward I'm not. What am I?" (ton / not)
7. "What can you catch but never throw?" (a cold)
8. "The person who makes it doesn't need it; the person who buys it doesn't use it. What is it?" (coffin)
9. "What has a head and a tail but no body?" (a coin)
10. "I have cities but no houses, forests but no trees. What am I?" (a map)

### 4. Word games — FIT: STRONG
- **Assets needed:** letters, grids, word tiles, anagrams. All drawable as code shapes.
- **Stack carries it?** Yes. Letter tiles, shuffles, and reveals are trivially code-computed; TTS reads the prompt.
- **Weak point:** readability at small size; letter games need careful typography at 720×1280. Also, word games can feel like homework if the payoff isn't satisfying.
- **Repeatability:** Very high — generated from word lists.
- **Differentiation:** speed rounds, themed word sets (e.g. "words that are also animals"), a streak/level system across a series.

**10 concrete ideas:**
1. "Unscramble: EALPP — 5 seconds" (APPLE)
2. "Name a word that rhymes with 'orange'... there isn't one" (with the near-miss 'sporange')
3. "Which word is spelled wrong in every dictionary?" ("wrong")
4. "Find the hidden animal: 'the cat ran' — CAT" (word-search style)
5. "What 5-letter word becomes shorter when you add two letters to it?" (short → shorter)
6. "Spell 'bookkeeper' — the only English word with three double letters in a row"
7. "Anagram challenge: 'astronomer' = 'moon starer'"
8. "What word has all five vowels in order?" (facetious, abstemious)
9. "Guess the word from its first and last letters: S _ _ _ _ N" (seventeen? station?)
10. "The longest word you can type with one row of a keyboard: 'typewriter'"

### 5. Motivational quotes — FIT: MEDIUM
- **Assets needed:** quote text, animated background (gradient, moving shapes, particles), music-adjacent pacing.
- **Stack carries it?** Partially. Text + motion is easy; the emotional punch usually comes from music and imagery we cannot generate. TTS reading a quote can sound flat.
- **Weak point:** oversaturated format; without music or striking visuals, a quote on a gradient is wallpaper. TTS naturalness is untested for emotional delivery.
- **Repeatability:** Very high — quote supply is endless.
- **Differentiation:** quotes tied to a specific story or person (not generic), a distinctive kinetic-type style, quotes nobody else uses (obscure sources, not the same 50 quotes).

**10 concrete ideas:**
1. "Discipline is choosing what you want most over what you want now" — with a split-screen choice animation
2. A lesser-known Seneca line on time, with a draining hourglass
3. "You don't have to be great to start, but you have to start to be great" — Zig Ziglar, with a starting-line build
4. A quote from an athlete's post-loss interview, not a poster quote
5. "The best time to plant a tree was 20 years ago. The second best time is now" — with a growing tree graphic
6. A quote about failure from a founder who actually failed first
7. "Comparison is the thief of joy" — with two bars, one shrinking
8. A one-line quote from a NASA astronaut on fear
9. "It always seems impossible until it's done" — Mandela, with a progress bar filling
10. A quote delivered as a 3-part reveal: setup → tension → payoff

### 6. Listicles ("Top 5...") — FIT: MEDIUM–STRONG
- **Assets needed:** numbered items, countdown pacing, one visual per item (icon/shape/text).
- **Stack carries it?** Yes for text-based lists (top 5 facts, top 5 mistakes). No for lists needing photos/video of the items.
- **Weak point:** each item needs a distinct visual or the video becomes a wall of text; item 5 must be worth the wait or retention collapses.
- **Repeatability:** High — list topics are endless.
- **Differentiation:** lists with a genuine ranking logic (not random), surprising #1, items that build on each other.

**10 concrete ideas:**
1. "5 everyday things that are older than you think" (toothpaste, sunglasses, the sandwich)
2. "Top 5 largest deserts — #1 isn't the Sahara" (Antarctic desert)
3. "5 words English stole from other languages" (kindergarten, tsunami, pajamas...)
4. "5 animals that can survive in space" (tardigrades first)
5. "5 things you didn't know your phone can do" (text-only, no screen recording available — keep to facts)
6. "Top 5 shortest wars in history" (Anglo-Zanzibar War, 38 minutes)
7. "5 foods that were once luxury items" (pineapples, potatoes, lobster)
8. "5 US states with the weirdest laws still on the books"
9. "5 inventions that were accidents" (penicillin, microwave, Post-its)
10. "5 reasons your brain loves music" (dopamine, memory, pattern)

### 7. History facts — FIT: MEDIUM–STRONG
- **Assets needed:** dates, timelines, maps, simple diagrams. Text + shapes work; period photos/paintings do not (no image generation proven).
- **Stack carries it?** Mostly. Timeline animations and map outlines are code-drawable. Anything needing archival photos or paintings is blocked.
- **Weak point:** history without visuals can feel like a lecture; needs strong narrative pacing and a "why it matters" angle.
- **Repeatability:** High — history is inexhaustible.
- **Differentiation:** "on this day" series, counterfactual hooks ("what if this one decision went differently"), obscure events rather than the same 20 famous ones.

**10 concrete ideas:**
1. "The Great Molasses Flood of 1919 — Boston drowned in syrup" (timeline build)
2. "The shortest war in history lasted 38 minutes" (Anglo-Zanzibar)
3. "In 1859, the Carrington Event set telegraph wires on fire" (solar storm)
4. "The London Beer Flood of 1814 killed 8 people"
5. "Vikings reached North America 500 years before Columbus" (map animation)
6. "The first computer bug was a real moth, 1947" (Harvard Mark II)
7. "In 1928, a man survived a fall from the 47th floor — twice" (actually: the Empire State Building elevator accident, 1945 — verify before use)
8. "The Great Emu War: Australia lost a war to birds, 1932"
9. "Napoleon was once attacked by rabbits" (1807 hunting incident)
10. "The first speeding ticket was issued in 1896 — for 8 mph"

### 8. Science facts / explainers — FIT: MEDIUM
- **Assets needed:** diagrams (orbits, cells, forces), counters, comparisons. Simple diagrams are code-drawable; realistic renderings are not.
- **Stack carries it?** Partially. Short facts work (see "did you know"). True explainers (why does X happen) need diagrams that may exceed simple shapes, and TTS must carry a multi-step explanation clearly.
- **Weak point:** diagram complexity ceiling; a bad diagram confuses more than no diagram. Also the hardest format to keep under 60 s without rushing.
- **Repeatability:** High — science questions are endless.
- **Differentiation:** one mechanism per video, animated step-by-step ("first this happens, then this"), ending with a testable prediction the viewer can check.

**10 concrete ideas:**
1. "Why is the sky blue? Rayleigh scattering in 30 seconds" (light-path diagram)
2. "Why do we see lightning before we hear thunder?" (speed comparison)
3. "How does a microwave actually heat food?" (water molecules vibrating)
4. "Why does the Moon look bigger near the horizon?" (Moon illusion)
5. "What happens inside a black hole, step by step" (simplified diagram)
6. "Why do onions make you cry?" (syn-propanethial-S-oxide, animated)
7. "How do noise-cancelling headphones work?" (wave cancellation diagram)
8. "Why is the ocean salty but rain isn't?" (evaporation cycle)
9. "What is déjà vu, and what causes it?" (current neuroscience, honestly hedged)
10. "Why do we get goosebumps?" (evolutionary leftover, hair-raising diagram)

### 9. "What if" scenarios — FIT: MEDIUM
- **Assets needed:** a premise, a chain of consequences, scale comparisons (numbers, timelines).
- **Stack carries it?** Partially. The narrative is TTS + text, which works; the wow factor usually comes from scale visuals (e.g. "if the Earth stopped spinning") that need diagrams we can only approximate with shapes.
- **Weak point:** speculation must stay clearly labelled as hypothetical; sloppy "science" here is misinformation risk. Also the most script-dependent format — a weak script kills it.
- **Repeatability:** Medium–high — premises are plentiful, but each needs a researched consequence chain.
- **Differentiation:** consequences the viewer would never guess, grounded in real numbers, with a "here's the math" beat.

**10 concrete ideas:**
1. "What if the Earth stopped spinning — for one second?" (inertia consequences)
2. "What if you fell into a black hole?" (spaghettification, time dilation)
3. "What if humans could photosynthesise?" (energy math: not enough skin area)
4. "What if the Moon disappeared tomorrow?" (tides, axial wobble)
5. "What if you lived on Jupiter?" (gravity, 2.5× weight)
6. "What if the internet went down for a week?" (cascading systems)
7. "What if dinosaurs never went extinct?" (mammal evolution blocked)
8. "What if you could travel at the speed of light?" (time stops for you)
9. "What if all the ice on Earth melted?" (sea level +66 m, which cities drown)
10. "What if gravity was half as strong?" (taller humans, weaker atmosphere)

### 10. Narrated stories — FIT: WEAK–MEDIUM
- **Assets needed:** characters, scenes, atmosphere. Normally needs illustration/footage/voice acting.
- **Stack carries it?** Poorly. A single TTS voice narrating over moving text/shapes can carry very short, punchy stories (urban legends, "true story in 60 seconds") but not character drama. No scene changes, no faces, no music.
- **Weak point:** the biggest gap between what the format needs (immersion) and what the stack offers (text + one voice). Highest risk of sounding like a robot reading a Wikipedia article.
- **Repeatability:** Medium — stories are plentiful, but each needs writing, not just facts.
- **Differentiation:** true stories with a twist ending, "based on a true story" framing, a consistent narrator persona built through the TTS voice's pacing.

**10 concrete ideas:**
1. "The man who sold the Eiffel Tower — twice" (Victor Lustig, 1925)
2. "The unsinkable Molly Brown's real story, in 60 seconds"
3. "How a janitor's idea became the Post-it Note" (Art Fry)
4. "The woman who saved 2,500 children from the Warsaw Ghetto" (Irena Sendler)
5. "The librarian who stole $8 million in rare books" (true crime, short)
6. "How one typo cost NASA $125 million" (Mars Climate Orbiter)
7. "The prisoner who escaped Alcatraz and was never found" (1962)
8. "The 13-year-old who became a millionaire selling a video game" (verify before use)
9. "How a pizza order helped catch a serial killer" (verify before use)
10. "The man who lived in an airport for 18 years" (Mehran Karimi Nasseri)

## Formats NOT recommended with this stack

- **Reaction / commentary on clips:** needs source footage we don't have and can't legally reuse.
- **Dance / trend / lip-sync:** needs a human body and a human voice.
- **Travel / food / lifestyle vlogs:** needs a camera and real locations.
- **AI-image slideshows (e.g. "AI-generated worlds"):** no image-generation model proven on this VM yet; do not assume one exists.
- **Product reviews / unboxings:** needs the physical product and a camera.

## Ranking (stack fit × repeatability × differentiation potential)

1. **Trivia/quiz** — strongest all-round fit; pure text + motion + TTS.
2. **Riddles/puzzles** — best suspense mechanics from pacing alone.
3. **Did-you-know facts** — simplest production, highest volume.
4. **Word games** — generated from word lists, highly repeatable.
5. **History facts** — strong if kept to timelines/maps; avoid photo-dependent topics.
6. **Listicles** — strong for text-based lists; weak when items need photos.
7. **Science explainers** — good for single-mechanism videos; diagram ceiling is the limit.
8. **What-if scenarios** — good scripts, but needs careful fact-checking and scale visuals.
9. **Motivational quotes** — easy to make, hard to stand out; music/imagery gap.
10. **Narrated stories** — weakest fit; immersion needs more than this stack offers today.

## Open questions / verification needed before committing

- TTS naturalness for emotional or suspenseful delivery is untested (blind test pending).
- Fact ideas above marked "verify before use" must be checked against a primary source before any script is written.
- Whether a signature visual identity (one motion language, one colour system) can be built in OpenFilm fast enough to keep a 1-video-per-day cadence is untested.
- No image-generation model is proven on this VM; any format that later needs one must be re-tested from scratch, not assumed.

## Bottom line

Start with trivia/quiz, riddles, and did-you-know facts. They need nothing the stack cannot already do, they are repeatable at volume, and their differentiation comes from question quality and a signature reveal mechanic — both of which are writing and code, not footage. Keep science explainers and what-if scenarios as second-wave formats once diagram quality and TTS pacing are proven. Avoid narrated stories and anything needing images, footage, or music until the stack grows.
