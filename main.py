"""Entry for make.fun 'Make the AI judge feel curious'.

Writes a single short mystery text to /output/entry.txt.
Python 3.13, standard library only, no network access.
"""

import os

TEXT = (
    "Every Tuesday at 6:40 a.m., a red bicycle leans against the shuttered "
    "bakery on Alder Street \u2014 but its owner, Mrs. Okafor, died in March. "
    "The bell still rings once. The basket still holds warm bread. "
    "Inside, the same three-word note. "
    "Who keeps baking for a woman who cannot eat?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
