"""The Perfect Pickup Line — make.fun bounty entry.

Prints the pickup line (one line, no extra output) and writes the exact
same line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), as the
house template judged-artifact expects.

The line's angle: nerdy romantic — a million simulated meetings, one
hopeful outcome, delivered with a wink rather than a boast.
"""

import os

LINE = "I ran a million simulations of us meeting, and every one ended the same way: me hoping you'd say hi."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    print(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
