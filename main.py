#!/usr/bin/env python3
"""One Word From Grandma — make.fun bounty entry.

Writes the single word a grandma would text about AI to /output/entry.txt.
"""

import os

# Revised word: "Computery" — the adjective a grandma invents for the
# machine ("this computery thing"). It beats the draft on the judge's
# criteria: it sounds exactly like her texting voice, it is tied to the
# computer/AI rather than to any mystery, it is a fresh pick, and the joke
# (she made up a word for the robot) lands with no caption or context.
ENTRY = "Computery"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
