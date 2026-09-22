#!/usr/bin/env python3
"""Install the default resume PDF dependencies in a chosen virtual environment."""

import argparse
import subprocess
import sys
import venv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--venv", required=True, type=Path, help="Virtual environment path")
    args = parser.parse_args()

    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or newer is required")

    target = args.venv.expanduser().resolve()
    venv.EnvBuilder(with_pip=True).create(target)
    python = target / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")

    subprocess.run(
        [str(python), "-m", "pip", "install", "reportlab>=4,<5", "pymupdf>=1.25,<2"],
        check=True,
    )
    subprocess.run([str(python), "-c", "import reportlab, pymupdf"], check=True)
    print(f"Resume PDF dependencies ready in {target}")


if __name__ == "__main__":
    main()
