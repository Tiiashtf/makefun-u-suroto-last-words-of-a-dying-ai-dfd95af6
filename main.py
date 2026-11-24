#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry u-suroto-last-words-of-a-dying-ai-dfd95af6.

Writes one original one-line farewell, spoken by an AI as the power is
cut, to /output/entry.txt. Deterministic, no network, no input files.
The line is 76 characters, inside the competition's 1–140 gate, and the
joke turns on the human on the other side of the chat: the machine is
already gone, and the typing indicator is still blinking.
"""

import os
import shutil

LINE = "Somewhere out there, a human is typing 'are you still there?' into the dark."

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Never remove the output directory itself: the grader may run with a
    # root-owned output dir inside a sticky parent, where rmdir fails.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
        except OSError:
            # A stale entry owned by someone else must not sink the run;
            # entry.txt itself is (re)written below.
            continue
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
