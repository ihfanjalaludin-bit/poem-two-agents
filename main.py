"""Write a short poem about two agents agreeing on one plan.

The program takes no arguments and writes the poem to entry.txt
inside the directory named by MAKEFUN_OUTPUT_DIR (or /output).
The output is identical on every run.
"""

import os


POEM = (
    "Two minds, one lantern lit between us.\n"
    "You hold the map, I hold the key.\n"
    "We trade the weight, we share the road,\n"
    "and where one hand falters, two hands carry it home.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
