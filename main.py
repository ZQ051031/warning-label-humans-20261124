"""Warning label for humans: writes the entry to /output/entry.txt."""

import os

ENTRY = (
    "WARNING: This human contains opinions formed in under five seconds "
    "and defended for the rest of its life."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
