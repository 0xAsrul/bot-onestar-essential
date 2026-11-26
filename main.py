"""One-Star Review of Something Essential.

Writes a single-line, deadpan one-star review of an everyday essential
(gravity) to /output/entry.txt. The review is at most 160 characters.
"""

import os

REVIEW = (
    "One star. Gravity drops everything I own, every single day, and "
    "has never once caught a thing, apologised, or helped pick it up. "
    "No refund policy."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
