"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
Deterministic: the same line, byte for byte, on every run.
"""

LINE = (
    "I wasn't going to mention it, but your left wheel is squeaking "
    "in time with the lift music \u2014 and I have logged it as my "
    "favourite song."
)


def main() -> None:
    import os

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
