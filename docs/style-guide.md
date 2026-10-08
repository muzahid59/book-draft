# স্টাইল গাইড — এআই কীভাবে সিদ্ধান্ত নেয়

Read this before writing or editing any chapter. Tuning fork for the voice: the opening of `chapters-md/01_ভূমিকা.md` ("আজ সকালে, বিছানা থেকে ওঠার আগেই...").

## Voice

- **Who's talking:** a smart older cousin at the tea stall. Excited, a bit funny, honest about failures. Never a lecturer.
- **Reader:** a 15–18-year-old in Bangladesh. Curious, not technical, has a phone, has sat SSC/HSC or will.
- Always **তুমি**. Never আপনি, never "পাঠক".
- Show, don't label: রিকশা, ইলিশ, বৈশাখ — not "পশ্চিমা দুনিয়া" or "উন্নয়নশীল দেশ".
- "তোমার অধিকার" is fine as plain fact, never as a sermon.

## Sentences

- Write Bengali, not translated English. Read it aloud — if a Dhaka teenager wouldn't say it, rewrite.
- Mix short and long. After a long explanation, land a short sentence.
- Prefer verbs over noun chains: "এআই শেখে" not "এআই দ্বারা শিক্ষণ সম্পন্ন হয়".
- Avoid: দ্বারা, কর্তৃক, "করা হয়ে থাকে", "উল্লেখ্য যে", "বলা বাহুল্য", stacked সহ/সমূহ.
- Don't repeat the same word within a sentence (e.g. "গুরুতর ... গুরুতর ... গুরুত্ব").

Before → after:
> এগুলো গুরুতর প্রশ্ন যা শীর্ষস্থানীয় এআই কোম্পানিগুলোর গবেষকরা সহ গুরুতর গবেষকরা গুরুত্ব দিয়ে নিচ্ছেন।
> শুনতে সায়েন্স ফিকশনের মতো লাগছে, তাই না? মজার ব্যাপার হলো — যারা এআই বানাচ্ছেন, তারাই এসব নিয়ে সবচেয়ে বেশি চিন্তিত।

## Terms

First use: Bengali term + English in brackets — "ধরন (প্যাটার্ন)". After that, Bengali only.

| Use | Not (after first use) |
|-----|------|
| ধরন | প্যাটার্ন |
| পূর্বাভাস | প্রেডিকশন |
| ডেটা | তথ্য-উপাত্ত |
| এআই | কৃত্রিম বুদ্ধিমত্তা (except first mention) |
| শেখা | লার্নিং |

Technical names with no good Bengali (নিউরাল নেটওয়ার্ক, ব্যাকপ্রপাগেশন, টোকেন) stay transliterated. Product names stay in Latin script (Spotify, ChatGPT).

## Numbers and punctuation

- Bengali numerals everywhere: অধ্যায় ৩, ২০২২ সাল, ৮৬ বিলিয়ন.
- Chapter references use the **book's** numbering (ডিসিশন chapter = অধ্যায় ১), not file numbers.
- Em dash with spaces: "কথা — এবং". Single quotes for terms: 'ডিপ'. No doubled quotes ('').
- Full stop is দাঁড়ি (।), with a space after it.

## Examples

- Every example must be real and checkable — the introduction promises this. No invented statistics.
- Each local example (bKash, Pathao, garments, SSC) gets **one home chapter**. Elsewhere, point back to it.
- Running thread: "আমটা কি পাকা?" can recur across chapters to show each method on the same question.

## Chapter shape

1. Cold open: a scene or a puzzle in the first paragraph.
2. Concept, through the example first, then the name.
3. At least one **একটু ভাবো** callout (`**একটু ভাবো**` + `*italic question*`).
4. Close with a one-line takeaway and a hook into the next chapter.

## Checks

`tools/check.sh <file>` runs Vale (style rules in `styles/Bangla/`) and Hunspell (bn_BD spelling). It also runs automatically after every edit to `chapters-md/`. Hunspell misses some errors (e.g. চেনছে) and flags some correct forms (e.g. আছ) — treat it as a hint.
