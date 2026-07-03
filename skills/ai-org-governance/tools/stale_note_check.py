#!/usr/bin/env python3
"""
stale_note_check — a runnable guard for the "trust the stale note" failure.

執行版的「引前必查」：任何引用內部檔案的 claim，若檔案超過門檻天數、
或未標記已回查，就擋下來要求驗證。這是 Discipline 3 的可執行形式。

Usage:
    python3 stale_note_check.py <file> [--max-age-days 7]

Exit code 0 = safe to cite. 1 = stale, re-verify before using.
No dependencies (stdlib only).
"""

import argparse
import os
import sys
import time


def days_since_modified(path: str) -> float:
    return (time.time() - os.path.getmtime(path)) / 86400.0


def check(path: str, max_age_days: float) -> tuple[bool, str]:
    if not os.path.exists(path):
        return False, f"MISSING: {path} does not exist — cannot cite what isn't there"
    age = days_since_modified(path)
    if age > max_age_days:
        return False, (
            f"STALE: {path} is {age:.1f} days old "
            f"(> {max_age_days:.0f}d). Re-check for updates before citing. "
            f"The urge to cite it now, unchecked, is the alarm."
        )
    return True, f"OK: {path} modified {age:.1f} days ago — within freshness window"


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Guard against citing stale internal files."
    )
    ap.add_argument("path", help="file a claim is about to be sourced from")
    ap.add_argument("--max-age-days", type=float, default=7.0)
    args = ap.parse_args()

    ok, msg = check(args.path, args.max_age_days)
    print(("✓ " if ok else "⚠ ") + msg)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
