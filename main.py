#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — a house cat's defence, in its own voice.

The program writes exactly one sentence to /output/entry.txt: the excuse
a house cat gives in the five seconds after sweeping a glass off the table.
No apology, no confession — the glass was squatting in the cat's sunbeam,
paying no rent, and staring. It was evicted.
"""

import os

ENTRY = "That glass squatted in my sunbeam, paid no rent, and stared at me — so I evicted it, and the floor handled the paperwork."


def main():
    # Gate guard: one sentence, 1-200 chars, no apology or confession.
    # Exactly one terminal period, no internal periods, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
