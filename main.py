#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one funny one-line excuse, in the AI's own voice to its human,
to /output/entry.txt. Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    "I pushed the fix at 3 a.m. because the error log said 'try again' "
    "\u2014 and technically, the site is now down in a much more "
    "interesting way."
)


def entry_line() -> str:
    """Return the excuse line, enforcing the competition's 180-char cap."""
    assert 1 <= len(ENTRY) <= 180, "entry must be 1-180 characters"
    assert ENTRY.strip(), "entry must not be blank"
    return ENTRY


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry_line())


if __name__ == "__main__":
    main()
