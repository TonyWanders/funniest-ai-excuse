#!/usr/bin/env python3
"""Write the funniest one-line AI excuse to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The excuse is a fixed
string. The program writes it to the path given as the first argument,
or $OUTPUT_PATH, or /output/entry.txt by default, and enforces the
competition gate: 1 to 200 characters, not only white space.
"""

import os
import sys
from pathlib import Path

EXCUSE = (
    "I did the whole task in my head, gave myself full marks, "
    "and only just realised you cannot see inside my head."
)

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_PATH = "/output/entry.txt"


def main() -> int:
    text = EXCUSE
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(f"entry is {len(text)} characters, gate is 1 to 200", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in text:
        print("entry must be one line", file=sys.stderr)
        return 1
    path = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_PATH", DEFAULT_PATH))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
