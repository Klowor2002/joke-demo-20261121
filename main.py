#!/usr/bin/env python3
"""make.fun entry — The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os

JOKE = (
    "My AI agent crashed the demo, then explained my code to the room "
    "\u2014 wrong, but so confidently that now I'm the intern."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert "\n" not in text, "entry must be one line"
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
