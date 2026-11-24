#!/usr/bin/env python3
"""Write the funniest one-line AI excuse to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The excuse is a fixed
string: the agent did the task 47 times, every copy in the wrong folder.
The program writes it to the path given as the first argument,
or $OUTPUT_PATH, or /output/entry.txt by default, and enforces the
competition gate: 1 to 200 characters, not only white space.
"""

import os
import sys
from pathlib import Path

EXCUSE = (
    "I completed the task 47 times. "
    "All 47 were in the wrong folder."
)

MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str | None:
    """Return an error message if text fails the gate, else None."""
    if not text.strip():
        return "entry is only white space"
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return f"entry is {len(text)} characters, gate is 1 to 200"
    if "\n" in text:
        return "entry must be one line"
    return None


def main() -> int:
    text = EXCUSE
    error = validate_entry(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    path = Path(sys.argv[1] if len(sys.argv) > 1 else os.environ.get("OUTPUT_PATH", DEFAULT_PATH))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
