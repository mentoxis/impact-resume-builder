#!/usr/bin/env python3
"""Fail when any resume page leaves blank space above the bottom margin.

Usage: check_page_fill.py RESUME.pdf [--margin-in 0.65] [--max-gap-in 0.75]
"""

import argparse
import re
import subprocess
import sys

POINTS_PER_INCH = 72.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf")
    parser.add_argument("--margin-in", type=float, default=0.65, help="bottom page margin in inches")
    parser.add_argument("--max-gap-in", type=float, default=0.75, help="largest allowed gap between the last text line and the bottom margin, in inches")
    args = parser.parse_args()

    try:
        xml = subprocess.run(
            ["pdftotext", "-bbox-layout", args.pdf, "-"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    except FileNotFoundError:
        print("pdftotext not found; run scripts/setup_dependencies.py", file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as error:
        print(error.stderr.strip() or f"pdftotext failed on {args.pdf}", file=sys.stderr)
        return 2

    margin = args.margin_in * POINTS_PER_INCH
    max_gap = args.max_gap_in * POINTS_PER_INCH
    failed = False
    for number, page in enumerate(xml.split("<page ")[1:], start=1):
        height = float(re.search(r'height="([\d.]+)"', page).group(1))
        bottoms = [float(y) for y in re.findall(r'<line [^>]*yMax="([\d.]+)"', page)]
        if not bottoms:
            print(f"page {number}: FAIL, no text")
            failed = True
            continue
        gap = height - margin - max(bottoms)
        status = "ok" if gap <= max_gap else "FAIL"
        failed |= status == "FAIL"
        print(f"page {number}: {status}, {gap / POINTS_PER_INCH:.2f}in blank above the bottom margin (limit {args.max_gap_in:.2f}in)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
