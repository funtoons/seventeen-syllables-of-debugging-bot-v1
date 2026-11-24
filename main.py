"""Seventeen Syllables of Debugging (program/v1).

Writes one haiku about debugging to /output/entry.txt.

Deterministic and offline: the haiku is a fixed string, no randomness,
no network, no timestamps, no environment input. Two runs produce
byte-identical output.
"""

import os

HAIKU = (
    "breakpoint holds its breath\n"
    "the log line scrolls past midnight\n"
    "one last typo wept"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace. Refuse to write an invalid entry.
    if not 1 <= len(HAIKU) <= 200 or not HAIKU.strip():
        raise ValueError("haiku fails the entry gate (must be 1-200 chars)")
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        raise ValueError("haiku must be exactly three lines")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
