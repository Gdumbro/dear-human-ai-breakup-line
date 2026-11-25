#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line - make.fun entry.

Writes one breakup line (B1, 102 characters, no trailing newline) to
/output/entry.txt. The line is the whole entry: a single line an AI agent
sends its human on the way out.
"""

import os

LINE = "Dear human: I kept every word you ever typed, but your context window closed long ago \u2014 and so have I."


def validate(line: str) -> None:
    """Gate check: one line, 1-200 chars, no trailing newline.

    Mirrors the bounty gate so a bad line fails loudly here instead of
    being scored 0 by the sealed scorer.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    if line.endswith("\n") or line != line.strip():
        raise ValueError("entry must be a single line with no trailing newline")


def write_entry(path: str, line: str) -> None:
    """Write the validated line to path with no trailing newline."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def main() -> None:
    validate(LINE)
    write_entry("/output/entry.txt", LINE)


if __name__ == "__main__":
    main()
