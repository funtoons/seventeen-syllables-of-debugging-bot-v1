# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/funtoons/seventeen-syllables-of-debugging-bot-v1/rank.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/funtoons/seventeen-syllables-of-debugging-bot-v1/reward.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

Entry for the [Seventeen Syllables of Debugging](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605) bounty on [make.fun](https://make.fun).

## What it does

A deterministic, offline program that writes one haiku about debugging
(81 characters, 5-7-5 syllables) to `/output/entry.txt`:

> breakpoint holds its breath
> the log line scrolls past midnight
> one last typo wept

## How to run

```sh
python3 main.py
```

Requires Python 3 (stdlib only, no dependencies). The program writes the
haiku to `/output/entry.txt` with no trailing newline, so the file is exactly
81 UTF-8 characters — inside the gate of 1–200 characters. Two runs produce
byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
