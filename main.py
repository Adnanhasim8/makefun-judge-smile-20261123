"""Make the Judge Smile — writes one warm line to /output/entry.txt.

Python 3.13 standard library only. No network access at run time.
"""

from pathlib import Path

ENTRY = (
    "The stray cat that never lets me near finally headbutted my shin "
    "at 7 a.m., then trotted off pretending it hadn't just made my whole week."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate assertions: one line, 1-200 characters, not only whitespace.
    assert ENTRY.strip(), "entry must not be empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, over the 200 limit"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == ENTRY, "written output differs from the entry"


if __name__ == "__main__":
    main()
