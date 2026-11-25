"""Make the AI Judge Laugh: Office Jokes — one funny line about office life.

The program writes a single line to /output/entry.txt: an employee who
declined a meeting to finish the work from the last meeting, and got
invited to a meeting about why they declined the meeting.
"""

import os

MAX_CHARS = 199
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The joke's twist lands in the last words: a meeting about the decline.
# The loop is the joke: the decline itself needs a meeting.
LINE = "I declined a meeting to finish the work from the last meeting, and got invited to a meeting about why I declined the meeting."


def build_line():
    """Return the entry line, checked: one line, under 200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-199 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
