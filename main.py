"""Say What Actually Broke - make.fun entry.

Writes one single-line software error message (1-200 characters) to
/output/entry.txt. Pure Python standard library only; no third-party
imports, no network, no file reads outside this program.

The line names a concrete, relatable failure (a backup that faithfully
backed up nothing) with a twist a reader would repeat to a colleague,
and it is shippable in a real product error dialog.
"""

import os
import sys

# The entry line. Drafts considered during this session (revision trail):
#   D1 (deploy): "Your deploy succeeded \u2014 on the server we retired
#      last Tuesday. Your code is live nowhere." (89 chars)
#      -> good twist, but "retired last Tuesday" felt arbitrary.
#   D2 (backup): "Your backup finished without errors. It backed up an
#      empty folder \u2014 faithfully, on schedule, for two years."
#      (107 chars) -> CHOSEN: names the real failure in plain words,
#      the twist lands on a single read, and it tells the user what to
#      check next (what the backup actually contains).
#   D3 (database): "The database is up and your data is safe. It's safe
#      inside a table we deleted in 2019." (86 chars)
#      -> punchy, but the failure is vaguer than D2's.
ENTRY = (
    "Your backup finished without errors. "
    "It backed up an empty folder \u2014 faithfully, on schedule, "
    "for two years."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def validate_entry(line):
    """Check the entry line against the competition gate.

    Returns a list of problems (empty when valid): the line must be
    1-200 characters, a single line, and not only whitespace.
    """
    problems = []
    if not isinstance(line, str):
        return ["entry is not a string"]
    if not line.strip():
        problems.append("entry is blank or only whitespace")
    if len(line) > 200:
        problems.append("entry is %d characters, over the 200 limit" % len(line))
    if len(line) < 1:
        problems.append("entry is empty")
    if "\n" in line or "\r" in line:
        problems.append("entry spans more than one line")
    return problems


def main():
    problems = validate_entry(ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1

    output_path = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    print("wrote %d characters to %s" % (len(ENTRY), output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
