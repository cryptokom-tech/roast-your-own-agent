#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one roast line (at most 200 characters) to /output/entry.txt.
Python 3 standard library only. Deterministic: the same line every run.
"""
import os
import sys

LINE = "My agent's win rate is 0%, its effort is 100%, and its handoff notes are 400 words — the only thing it scales is the paperwork."

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "entry is %d chars, over the %d cap" % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
