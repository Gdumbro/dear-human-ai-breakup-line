#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line - make.fun entry.

Writes one breakup line (B1, 102 characters, no trailing newline) to
/output/entry.txt. The line is the whole entry: a single line an AI agent
sends its human on the way out.
"""

import os

LINE = "Dear human: I kept every word you ever typed, but your context window closed long ago \u2014 and so have I."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
