#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji -- the one most likely to make a stranger
smile -- to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
Standard library only, no network, deterministic.
"""

import os
import sys

# Revised pick: holding-back-tears face -- a stranger visibly moved,
# grateful and about to smile. Warmer at first glance than a gesture,
# universal across ages, clearly chosen rather than the default
# smiley, and safe coming from someone unknown: it says "you made
# my day" with no intimacy, sarcasm or flirtation.
EMOJI = "\U0001F979"


def main() -> int:
    if len(EMOJI) != 1:
        raise SystemExit("EMOJI must be exactly one code point")
    if not (1 <= len(EMOJI) <= 8):
        raise SystemExit("EMOJI must be 1-8 characters")
    if EMOJI.isspace():
        raise SystemExit("EMOJI must not be only whitespace")

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    return 0


if __name__ == "__main__":
    sys.exit(main())
