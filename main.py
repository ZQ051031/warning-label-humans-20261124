"""Warning label for humans: writes the entry to /output/entry.txt."""

import os

ENTRY = (
    "WARNING: This human will confidently explain topics learned five "
    "minutes ago and will not be taking questions."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
