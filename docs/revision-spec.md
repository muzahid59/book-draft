# Book Revision Spec: এআই কীভাবে সিদ্ধান্ত নেয়

## Status

| Task | Status |
|------|--------|
| Chapter 1 — ভূমিকা | DONE (committed 9e3004e in .docx; restored into .md — the .md conversion had missed it) |
| Chapter 2 — ডিসিশন বা সিদ্ধান্ত কি | DONE (~1,490 words; reviewed by beta-reader, line-editor, fact-checker) |
| Chapter 3 — উদাহরণ দিয়ে যন্ত্র শেখানো | DONE (~1,570 words; reviewed by beta-reader, line-editor, fact-checker) |
| Chapter 4 — কেউ না বলেও ধরন খোঁজা | DONE (~1,670 words; reviewed by beta-reader, line-editor, fact-checker) |
| Chapter 5 — ভুল করে করে শেখা | DONE (~1,640 words; reviewed by beta-reader, line-editor, fact-checker) |
| Chapter 6 — নিউরাল নেটওয়ার্ক | DONE (~1,820 words; reviewed by beta-reader, line-editor, fact-checker) |
| Chapter 7 — ছবি ও ভিডিও | TODO |
| Chapter 8 — ভাষা কীভাবে বোঝে | TODO |
| Chapter 9 — বাস্তব দুনিয়ায় এআই | TODO |
| Chapter 10 — পক্ষপাত, ন্যায্যতা | TODO |
| Chapter 11 — ভবিষ্যৎ | TODO |
| Chapter 12 — ডেটা গোপনীয়তা (NEW) | TODO |
| Chapter 13 — শব্দকোষ / Glossary (NEW) | TODO |
| Final pass — transitions, navigation, merge | TODO |

---

## Goal

Revise the Bengali AI book implementing 10 beta reader recommendations. All edits to existing chapters use Word tracked changes so the author can accept/reject.

## Tone Guidelines (from author feedback)

- Casual, easy-going "তুমি" voice — like an older sibling, not a lecturer
- Show, don't label — use রিকশা/ইলিশ/বৈশাখ, not "পশ্চিমা দুনিয়া"
- "তোমার অধিকার" is OK when stated as obvious fact, not a sermon
- Punchy and direct, not preachy or textbook-ish
- Concrete examples over abstract categories

## Editing Workflow

**Format: Markdown** (switched from docx XML for speed and reliability)

- Working files: `chapters-md/NN_name.md`
- Edit markdown directly, git diff serves as change tracking
- Final conversion back to .docx happens after all content is approved
- Original .docx files preserved in `chapters/` as reference

## Markdown Conventions

- `# Heading` = Chapter title (Heading1)
- `## Heading` = Section heading (Heading2)
- `**একটু ভাবো**` + `*italic question*` = Interactive callout
- `[Insert diagram: description]` = Diagram placeholder (English)
- Body text = plain paragraphs
- `অধ্যায় N` label sits on the first line of its own chapter file, Bengali numerals

## Chapter Numbering

"Chapter N" in this spec = **file number** (internal). Text the reader sees uses **book numbering = file number − 1** (ভূমিকা is unnumbered). E.g. file 04 (unsupervised) = অধ্যায় ৩, file 06 (neural networks) = অধ্যায় ৫, file 09 (real world) = অধ্যায় ৮. New chapters: file 12 = অধ্যায় ১১, file 13 (glossary) is unnumbered.

## New chapters (12, 13)

Created directly as markdown in `chapters-md/`. Converted to .docx in the final pass.

---

## Per-Chapter Content Specs

Word targets are rough guides, not limits. Going over is fine when the extra words answer a confusion the beta reader actually reported.

### Chapter 2 — ডিসিশন বা সিদ্ধান্ত কি
**Target:** ~888 → ~1,300 words (actual: ~1,490) | **w:id range:** 200-230
**Done differently:** running example is a Thursday-evening Mirpur→Dhanmondi trip and Google Maps' '৫২ মিনিট' (Google 'Maps 101' blog, 2020). Rice cooker replaces the thermostat as the rule-based machine; a made-up travel-time table shows why 'distance ÷ speed' fails. Data/pattern/prediction all taught through traffic, plus the 2020 lockdown as patterns changing. Spotify removed. bKash example not added (its home is অধ্যায় ৩). ChatGPT record framed as an analyst estimate; Threads comparison dropped. Bangladesh paragraph points to Bengali.AI (অধ্যায় ২). Heading now 'কী' (file name unchanged).

1. **Trim Spotify paragraph** in "নিয়ম বনাম শেখা" section — remove clustering explanation (covered in Ch 4), add forward reference: "Spotify কীভাবে এটা করে তা অধ্যায় ৩-এ বিস্তারিত দেখবে।"
2. **Insert diagram placeholder** after data/pattern/prediction summary: `[Insert diagram: Data → Pattern → Prediction cycle — three interconnected circles with arrows, labeled ডেটা → ধরন → পূর্বাভাস]`
3. **Insert bKash example** of data/pattern/prediction cycle (2 paras):
   - bKash transactions = ডেটা, spending patterns = ধরন, fraud alert = পূর্বাভাস
4. **Insert Bangladesh AI context** in history section (1 para):
   - Mobile banking fraud detection, garment industry QC, crop disease identification
   - Note: most systems built outside Bangladesh, without Bangladeshi data

### Chapter 3 — উদাহরণ দিয়ে যন্ত্র শেখানো (Supervised Learning)
**Target:** ~705 → ~1,200 words (actual: ~1,570) | **w:id range:** 300-330

1. **After Google Photos example**, insert 2 paras about Western training data mislabeling Bengali context — food (বিরিয়ানি→paella, পিঠা→pancake), clothing, architecture
2. **Agriculture example** — classifying Bangladesh's rice varieties or jute quality with labeled images
3. **SSC/HSC exam analogy** for overfitting — memorizing old questions vs understanding concepts
4. **"একটু ভাবো"**: "তুমি যদি একটা এআই তৈরি করতে কাঁঠাল, লিচু, আর আম চিনতে — কী কী তথ্য তুমি লেবেল হিসেবে ব্যবহার করতে?"
5. **Neural network bridge** at end: "তুমি হয়তো ভাবছ — এআই আসলে কোন গাণিতিক কাঠামো ব্যবহার করে এই ধরনগুলো শেখে? উত্তরটা হলো নিউরাল নেটওয়ার্ক — অধ্যায় ৫-এ বিস্তারিত আসবে।"

**Done differently:** Bengali-context mislabeling uses documented research instead of the hypothetical বিরিয়ানি→paella: Shankar et al. 2017 (Hyderabad groom → 'chain mail') and DeVries et al. 2019 (~10-point accuracy gap for low-income homes); food examples kept only as a labelled guess for the reader to test. Agriculture = Rahman et al. 2020 (BRRI rice disease/pest images). Running example: photos in your phone gallery throughout (search 'cat' cold open, labelled-photo table with T-shirt edge case, Google Photos face naming, sofa-cat overfitting, 1,000-photo split); mango kept for Ch 6 only. Bengali.AI and BRRI framed as photo labelling; TIME/Kenya kept with an explicit 'লেখার বেলাতেও' bridge. একটু ভাবো changed from fruits to rickshaw photos to match the thread.

### Chapter 4 — কেউ না বলেও ধরন খোঁজা (Unsupervised Learning)
**Target:** ~604 → ~1,200 words (actual: ~1,670) | **w:id range:** 400-430
**Done differently:** running example is Facebook (People You May Know cold open → mutual-friends toy table → bought-likes clustering via SynchroTrap, Cao et al. CCS 2014, with a like-timing toy table → login-alert anomaly detection → cricket-win likes as the false-alarm case, tied to SynchroTrap's 'sustained synchrony' rule). Spotify and YouTube were considered; Facebook chosen for familiarity (60M+ BD users) and because SynchroTrap is a real, deployed unsupervised clustering system. SynchroTrap accounts described as malicious (fake or hacked), humans only sampled for accuracy. Amazon/bank examples dropped. bKash (Daily Star 2026) framed honestly: unsupervised baseline missed ~2/3; 97% only after adding label-trained models; a proposal. Garment QC via Mei et al. 2018. Ice cream/drowning replaced by the cricket example. Google eye-scan dropped (Poplin et al. 2018 was supervised — candidate for Chapter 9). Chapter 3's closing hook now asks who would label billions of friendships, likes and logins.

1. **bKash fraud detection case study** after anomaly detection (3-4 paras) — mobile money, unsupervised anomaly detection, no pre-labeled fraud examples
2. **Garment industry QC** — unsupervised learning for fabric defect detection
3. **Spurious correlation example** — ice cream sales vs drowning (both rise in summer)
4. **Expand Google eye-scan/heart-disease** — add 2-3 sentences about significance
5. Ch 4 already has "একটু ভাবো" — do NOT add another

### Chapter 5 — ভুল করে করে শেখা (Reinforcement Learning)
**Target:** ~822 → ~1,250 words (actual: ~1,640) | **w:id range:** 500-530
**Done differently:** running example is লুকোচুরি — OpenAI's hide-and-seek experiment (Baker et al., ICLR 2020): RL vocabulary table, six-round arms race, box surfing and running off the map as reward hacking. Side cases: YouTube's 2012 switch from clicks to watch time, AlphaGo Move 37 (noting it first learned from human games), YouTube's 2019 REINFORCE recommender (Chen et al., WSDM 2019), one line on ChatGPT's RLHF. Dropped: carrom/ludo (thin research), Dhaka traffic (no real study found), Google cooling (2016 system was not RL), Dota/Atari/boat race/robots/self-driving.

1. **Carrom/ludo example** after AlphaGo — RL with familiar Bangladeshi games
2. **Dhaka traffic optimization** — RL for signal timing in world's most congested city, parallel to DeepMind data center cooling
3. **Expand reward hacking** — social media algorithm example (optimize engagement → promote divisive content = alignment problem)
4. **"একটু ভাবো"**: "ধরো তুমি একটা এআইকে 'ভালো ছাত্র' হতে ট্রেনিং দিচ্ছ। পুরস্কার হিসেবে শুধু পরীক্ষার নম্বর দিলে কী হতে পারে?"
5. **Neural network bridge** at end — preview Ch 6

### Chapter 6 — মস্তিষ্কের রূপকথা — নিউরাল নেটওয়ার্ক
**Target:** ~751 → ~1,300 words (actual: ~1,820) | **w:id range:** 600-630
**Done differently:** kept the exam-paper analogy for backprop (reframed as a coaching teacher) instead of the cooking analogy — readers named it their favourite part. Running example: Dada (grandfather) picking mangoes at the bazaar (cold open → single-node worked example → backprop walkthrough → closing hook to vision chapter). Bias is taught as a পাস নম্বর; the worked example and backprop use marksheet-style tables.

1. **Diagram placeholder** after layers: `[Insert diagram: Neural network with three layers — input (রঙ, দৃঢ়তা, গন্ধ, আকার), hidden (6 nodes), output (পাকা, কাঁচা)]`
2. **Mango-ripeness worked example** for weights/biases — color, firmness, smell as inputs, walk through intuitively
3. **Parameter count context** — "শত শত বিলিয়ন" compared to stars in Milky Way (~100-400 billion)
4. **Cooking analogy** for backpropagation — learning rice cooking through family feedback
5. **"একটু ভাবো"**: "তোমার নিজের শেখার প্রক্রিয়ার সাথে ব্যাকপ্রপাগেশনের মিল কোথায়?"

### Chapter 7 — এআই যেভাবে দেখে (Computer Vision)
**Target:** ~729 → ~1,300 words | **w:id range:** 700-730

1. **CONSOLIDATE medical AI** — shorten to 1-2 sentences + forward reference to Ch 9
2. **CNN diagram placeholder**: `[Insert diagram: CNN filter progression — edges → shapes → faces]`
3. **NEW subsection "গার্মেন্টস শিল্পে এআই"** (3-4 paras) — fabric defect detection, compliance monitoring, RMG sector, Rana Plaza safety context, question of surveillance vs safety
4. **Expand deepfake** — South Asian political deepfake context
5. **"একটু ভাবো"**: "গতকাল তুমি সোশ্যাল মিডিয়ায় যে ছবি বা ভিডিও দেখেছ — সেগুলোর কোনোটা কি এআই-জেনারেটেড হতে পারে?"

### Chapter 8 — এআই ভাষা কীভাবে বোঝে (Language AI)
**Target:** ~816 → ~1,350 words | **w:id range:** 800-830

1. **NEW subsection "বাংলা ভাষা আর এআই: অনন্য চ্যালেঞ্জ"** (4 paras):
   - Bengali = 7th most spoken but "low-resource" for AI
   - Script complexity (যুক্তবর্ণ), tokenization inefficiency (8-10 tokens vs 3-4 for English)
   - Practical impact: worse voice recognition, translation, AI assistant quality
   - This is an equity issue — better Bengali AI = better healthcare, education for 230M people
2. **Bangladesh hallucination example** — AI generating plausible but false facts about মুক্তিযুদ্ধ
3. **Closing paragraph** tying to book themes — AI reads patterns not meaning, knows statistics not truth
4. **"একটু ভাবো"**: "ChatGPT-কে বাংলায় একটা প্রশ্ন কর, তারপর একই প্রশ্ন ইংরেজিতে কর। উত্তরের মানে কি তফাৎ আছে?"

### Chapter 9 — বাস্তব দুনিয়ায় এআই (AI in the Real World)
**Target:** ~815 → ~1,300 words | **w:id range:** 900-930

1. **NEW subsection "রাইড-হেইলিং: ঢাকার রাস্তায় এআই"** (3-4 paras) — Pathao/Uber surge pricing, route optimization, driver-rider matching in Dhaka traffic
2. **Expand medical AI** (now primary location after Ch 7 consolidation) — TB detection in rural Bangladesh clinics, telemedicine
3. **bKash credit scoring** — mobile money credit scoring where traditional credit history is sparse
4. **"একটু ভাবো"**: "তোমার TikTok বা YouTube ফিড কি তোমাকে একই ধরনের কন্টেন্ট বারবার দেখায়? একটা সপ্তাহ ধরে লক্ষ করো।"

### Chapter 10 — পক্ষপাত, ন্যায্যতা (Bias & Fairness)
**Target:** ~903 → ~1,500 words | **w:id range:** 1000-1040

1. **Check Amazon hiring ref** — if retells full story, trim to single sentence pointing to Ch 9
2. **NEW subsection "দক্ষিণ এশিয়ায় এআই পক্ষপাত"** (4-5 paras):
   - Caste discrimination in AI (name-based inference, zip code proxies)
   - Gender bias in South Asian hiring (garment sector women majority but not in management)
   - Linguistic bias against Bengali (worse speech recognition, fewer training examples)
3. **Reframe Western bias** — caste, religion, language, economic class alongside racial categories
4. **Aadhaar-linked welfare** (2-3 paras) — biometric failures denying food rations, parallel to Bangladesh national ID
5. **"একটু ভাবো"**: "ধরো তোমার স্কুলে একটা এআই সিস্টেম ছাত্রদের 'ভবিষ্যৎ সাফল্য' পূর্বাভাস দিচ্ছে। কোন তথ্য ব্যবহার করা উচিত? কোনগুলো অন্যায়?"

### Chapter 11 — ভবিষ্যৎ (Future and You)
**Target:** ~1,165 → ~1,500 words | **w:id range:** 1100-1130

1. **Format 10 critical questions as numbered list** — add Bengali numerals (১., ২., ... ১০.), make question text bold
2. **AGI grounding** — Bangladesh-specific: "বাংলাদেশের মতো দেশে AGI-র প্রভাব ভিন্ন হবে — কারণ এখানে অনেক মানুষের কাজ ইতিমধ্যে শ্রম-নিবিড়..."
3. **Bangladesh career paths** — AI ethics in NGOs, data annotation companies, AI for agriculture startups
4. **Navigation link** to new Ch 12
5. **"একটু ভাবো"**: "এই বইয়ের কোনো অংশ কি এআই দিয়ে লেখা হতে পারে? তুমি কীভাবে বুঝবে?"

### Chapter 12 — ডেটা গোপনীয়তা ও নজরদারি (NEW — Data Privacy)
**Target:** ~1,200-1,500 words | **Created with python-docx**

Heading1: "ডেটা গোপনীয়তা ও নজরদারি"

Sections (Heading2):
1. "তোমার ডেটা কোথা থেকে আসে?" — bKash transactions, Grameenphone metadata, Facebook usage
2. "সম্মতি কী, আর আসলে কি তুমি সম্মত হচ্ছ?" — ToS nobody reads, data from minors
3. "নজরদারি রাষ্ট্র আর এআই" — China social credit, Dhaka CCTV, digital security act
4. "ডেটা অধিকার: তোমার তথ্য, তোমার ক্ষমতা" — GDPR, Bangladesh draft data protection law

Plus "একটু ভাবো" prompt and navigation link to Ch 13.

### Chapter 13 — শব্দকোষ (NEW — Glossary)
**Target:** ~35 terms | **Created with python-docx**

Heading1: "শব্দকোষ"

Format: **Bold Bengali term** (English term) — definition in Bengali

Terms: অ্যালগরিদম, অ্যাটেনশন, আনসুপারভাইজড লার্নিং, ওভারফিটিং, ওয়েট, কনভোলিউশনাল নিউরাল নেটওয়ার্ক/CNN, ক্লাস্টারিং, কনটেক্সট উইন্ডো, টোকেন, ট্রেনিং ডেটা, ডিপ লার্নিং, ডেটা, ডেটাসেট, নিউরাল নেটওয়ার্ক, পক্ষপাত/বায়াস, পূর্বাভাস, ফাইন-টিউনিং, ব্যাকপ্রপাগেশন, বড় ভাষা মডেল/LLM, মেশিন লার্নিং, মডেল, রিইনফোর্সমেন্ট লার্নিং, লেবেল, সুপারভাইজড লার্নিং, হ্যালুসিনেশন, হিডেন স্তর, AGI, RLHF, ধরন/প্যাটার্ন, অ্যানোমালি ডিটেকশন, ডিপফেক, কোলাবরেটিভ ফিল্টারিং

### Final Pass

1. Check each chapter 1-12 has forward-looking transition to next chapter's topic
2. Verify navigation links: Ch 11 → Ch 12 → Ch 13
3. Run `python merge_chapters.py` to rebuild master document
4. Verify master: file size increased, tracked changes present, 14 chapters total
