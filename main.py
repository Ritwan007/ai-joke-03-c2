"""ai-joke-03 candidate #2.

Writes one one-liner joke about AI coding agents to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

JOKE = (
    "My coding agent doesn't write bugs. "
    "It writes features the spec will be updated to describe."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")
    print("wrote:", OUTPUT_PATH)


if __name__ == "__main__":
    main()
