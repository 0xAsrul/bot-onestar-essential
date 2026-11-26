"""One-Star Review of Something Essential.

Writes a single-line, deadpan one-star review of an everyday essential
(gravity) to /output/entry.txt. The review is at most 160 characters.
"""

import os

REVIEW = (
    "One star. Gravity has pulled everything down since the dawn of time "
    "and has never once offered to carry a single thing back up. "
    "Rude, honestly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
