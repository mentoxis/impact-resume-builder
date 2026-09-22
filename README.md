# Impact Resume Builder

A reusable Codex skill for creating an impact-driven, ATS-friendly resume from an existing resume or career notes. It asks for missing evidence before writing and never invents metrics, roles, dates, or credentials. Candidate resumes and personal details stay outside this repository.

## What it does

1. Reads the candidate's existing resume. If there is none, gathers career history, education, skills, and contact details.
2. Asks focused questions about ownership, the problem solved, actions, scale, and outcomes. It asks for numbers only when the candidate can verify them.
3. Writes concise, relevant achievement bullets and builds a single-column LaTeX resume designed for straightforward ATS parsing.
4. Compiles the PDF with Tectonic and checks page count, extracted text, fonts, links, and rendered pages with Poppler tools.

The output is an editable `.tex` file and a PDF, organized in numbered versions. Unconfirmed facts are flagged for review.

## Install for Codex

Clone the repository into your personal skills directory:

```bash
git clone https://github.com/santoshyadav979439/impact-resume-builder.git ~/.agents/skills/impact-resume-builder
```

Python 3 is required for the dependency checker. Run:

```bash
python3 ~/.agents/skills/impact-resume-builder/scripts/setup_dependencies.py
```

The script checks for Tectonic and Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`, and `pdffonts`). When Homebrew is available, it installs missing packages with `brew install`. On other platforms, install Tectonic and Poppler with your package manager, then rerun the script.

## Use

Attach an existing resume or provide career notes, then ask Codex:

> Use $impact-resume-builder to create a resume for a senior software engineer role. Read my existing resume, ask about unclear achievements and missing impact, then produce the LaTeX source and PDF.

The skill instructions are in [SKILL.md](SKILL.md), and the editable starting point is [assets/resume-template.tex](assets/resume-template.tex).
