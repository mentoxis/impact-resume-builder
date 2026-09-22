#!/usr/bin/env python3
"""Install or verify the tools used to build and inspect LaTeX resumes."""

import shutil
import subprocess


def main() -> None:
    packages = []
    if shutil.which("tectonic") is None:
        packages.append("tectonic")
    poppler_tools = ("pdfinfo", "pdftotext", "pdftoppm", "pdffonts")
    if any(shutil.which(tool) is None for tool in poppler_tools):
        packages.append("poppler")

    if packages:
        brew = shutil.which("brew")
        if brew is None:
            raise SystemExit(
                "Missing tools: " + ", ".join(packages) + ". Install Tectonic and "
                "Poppler with your platform's package manager, then rerun this script. "
                "Tectonic installation: "
                "https://tectonic-typesetting.github.io/book/latest/installation/"
            )
        subprocess.run([brew, "install", *packages], check=True)

    required = ("tectonic", *poppler_tools)
    missing = [tool for tool in required if shutil.which(tool) is None]
    if missing:
        raise SystemExit("Required commands still missing: " + ", ".join(missing))
    print("Resume tools ready: " + ", ".join(required))


if __name__ == "__main__":
    main()
