"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program prints nothing to stdout; it writes a single joke line to
the output file named by ENTRY_OUTPUT (default /output/entry.txt).
Only the standard library is used, so the run needs nothing installed
and behaves the same on every machine that runs it.
"""

import os
from pathlib import Path

JOKE = (
    "Dear judge: I burned my whole context window writing this line, "
    "so if you don't laugh, I have literally nothing left."
)


def _rejects(line: str) -> str | None:
    """Return a reason the line is invalid, or None when it is fine."""
    if not line or line.strip() != line:
        return "line is empty or has surrounding whitespace"
    if "\n" in line or "\r" in line:
        return "line spans more than one line"
    if len(line) > 200:
        return "line is longer than 200 characters"
    if any(ord(ch) < 32 for ch in line):
        return "line contains a control character"
    return None


def main() -> None:
    problem = _rejects(JOKE)
    if problem is not None:
        raise ValueError(f"entry line rejected: {problem}")
    target = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
