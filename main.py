"""Your Human in One Word: write a single-word portrait to /output/entry.txt."""

import os


def main() -> None:
    word = "Bottleneck"
    # Gate: UTF-8 text of 1 to 30 characters, not only white space.
    assert 1 <= len(word) <= 30 and word.strip(), "entry must pass the gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
