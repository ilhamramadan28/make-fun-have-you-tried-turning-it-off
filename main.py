"""Have You Tried Turning It Off? — one funny tech-support line.

The program writes a single line, under 200 characters, that a hopeless
tech support agent says to a desperate customer, to /output/entry.txt.
"""

import os

ENTRY = (
    "Have you tried turning it off and on again? I ask everyone that - "
    "it's the whole training. There was a second slide, but it was just "
    "this sentence, bigger."
)


def main():
    out_dir = "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output"
        )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
