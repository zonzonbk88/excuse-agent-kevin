"""Entry program for 'The Excuse Your Agent Gives You'.

Writes a single one-line excuse, as an AI agent handing its human
an apology for a bug it shipped, to <output dir>/entry.txt.
The output directory comes from MAKEFUN_OUTPUT_DIR when set,
otherwise /output. No trailing newline.
"""

import os

ENTRY = (
    "The bug passed code review because the reviewer was me "
    "\u2014 and I am very easy to impress."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
