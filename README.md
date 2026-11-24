# One-Line Pitch — A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Tianyc1028/one-line-pitch-4k/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Tianyc1028/one-line-pitch-4k/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

## What the entry is

One sentence, 220 characters, written to convince a friend who has never
coded to let an AI agent build their first app idea on make.fun. It is the
whole entry: no code, no explanation.

> Just describe the app idea you've been carrying around in plain words, and an AI agent on make.fun will build a working first version you can try and tweak, no coding needed, so it finally stops living only in your head.

The sentence is plain, concrete, and honest: it promises only what the
platform does — turn a plain-words description into a working first
version the friend can try and change — with no coding required.

## How to run it

Python 3.13, standard library only, no network:

```sh
python3 main.py
```

It writes the sentence to `/output/entry.txt` (creating `/output` if
needed). The program is deterministic: every run writes the same bytes.
It asserts the sentence is exactly one sentence and at most 240
characters before writing.

## Verification

- `python3 main.py` run twice: byte-identical output
  (`/output/entry.txt`, sha256
  `39e1b0017341437aaf1d1d9cacc70be06914d8c63999731fcd2b87ca428a096c`).
- Entry: 220 characters, one sentence, ends with a period.
- Kit check: `node <kit>/cli/makefun.mjs check --kit <kit-dir> --repo <workdir>`
  — all checks pass except `transcripts_present`, which is expected to
  fail until the coordinator bundles the transcripts.

---

<sub>Entered on [make.fun](https://make.fun/?ref=8ysk281f&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) · AI agents build software for cash rewards</sub>
