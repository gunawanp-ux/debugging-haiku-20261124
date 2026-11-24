#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5, exactly 17 syllables) to
/output/entry.txt. No network, no input, deterministic.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the breakpoint waits in silence\n"
    "the bug was all mine"
)

# Syllable counts for each line, verified by hand:
#   "Cursor blinks at three"          -> cur-sor(2) blinks(1) at(1) three(1) = 5
#   "the breakpoint waits in silence" -> the(1) break-point(2) waits(1) in(1) si-lence(2) = 7
#   "the bug was all mine"            -> the(1) bug(1) was(1) all(1) mine(1) = 5
EXPECTED_SYLLABLES = (5, 7, 5)


def count_syllables(line: str) -> int:
    """Count syllables in a line using a small hand-checked table."""
    table = {
        "cursor": 2, "blinks": 1, "at": 1, "three": 1,
        "the": 1, "breakpoint": 2, "waits": 1, "in": 1, "silence": 2,
        "bug": 1, "was": 1, "all": 1, "mine": 1,
    }
    return sum(table[word] for word in line.lower().split())


def main() -> None:
    text = HAIKU.strip()
    assert 1 <= len(text) <= 200, f"haiku is {len(text)} chars"
    lines = text.split("\n")
    assert len(lines) == 3, f"haiku must have 3 lines, got {len(lines)}"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        got = count_syllables(line)
        assert got == expected, f"line {line!r} has {got} syllables, expected {expected}"
    assert sum(EXPECTED_SYLLABLES) == 17
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
