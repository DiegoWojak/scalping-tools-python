#!/usr/bin/env python3
"""Record audit result into FEEDBACK.md."""

import sys
import re
from datetime import date
from pathlib import Path

FEEDBACK_PATH = Path(__file__).parent.parent / "assets" / "FEEDBACK.md"


def next_audit_number() -> int:
    if not FEEDBACK_PATH.exists() or not FEEDBACK_PATH.read_text(encoding="utf-8").strip():
        return 1
    text = FEEDBACK_PATH.read_text(encoding="utf-8")
    numbers = re.findall(r"## Auditoría #(\d+)", text)
    return max(int(n) for n in numbers) + 1 if numbers else 1


def append_result(result: str) -> None:
    number = next_audit_number()
    entry = (
        f"\n\n---\n\n"
        f"## Auditoría #{number} — {date.today().isoformat()}\n\n"
        f"{result}\n"
    )
    with FEEDBACK_PATH.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Recorded audit #{number} in {FEEDBACK_PATH}")


def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python feedback.py "<resultado>"')
        sys.exit(1)
    result = " ".join(sys.argv[1:])
    append_result(result)


if __name__ == "__main__":
    main()
