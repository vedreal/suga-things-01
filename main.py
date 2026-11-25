"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Line 1 explains a queue to a 10-year-old with one vivid analogy:
a queue is a snake made of people. Line 2 is honest about what
that analogy maps and what it leaves out.

The program writes the two-line entry to /output/entry.txt.
"""

import os
import sys

ENTRY = (
    "A queue is a snake made of people, with its head at the front "
    "and its tail growing longer every time someone new joins.\n"
    "It maps how the line grows from the back and shrinks from the "
    "front, but it leaves out the venom, the scales, and that a real "
    "snake never waits its turn."
)


def output_path():
    """Return the path the entry text must be written to."""
    return os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output"
    ) + "/entry.txt"


def main():
    """Write the two-line entry to the output file."""
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
