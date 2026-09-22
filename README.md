# Impact Resume Builder

A reusable [Agent Skill](https://agentskills.io/) for Codex, Claude Code, and OpenCode. It creates an impact-driven, ATS-friendly resume from an existing resume or career notes. It asks for missing evidence before writing and never invents metrics, roles, dates, or credentials. Candidate resumes and personal details stay outside this repository.

## What it does

1. Reads the candidate's existing resume. If there is none, gathers career history, education, skills, and contact details.
2. Asks focused questions about ownership, the problem solved, actions, scale, and outcomes. It asks for numbers only when the candidate can verify them.
3. Writes concise, relevant achievement bullets and builds a single-column LaTeX resume designed for straightforward ATS parsing.
4. Compiles the PDF with Tectonic and checks page count, extracted text, fonts, links, and rendered pages with Poppler tools.

The output is an editable `.tex` file and a PDF, organized in numbered versions. Unconfirmed facts are flagged for review.

## Supported agents

The skill uses the portable `SKILL.md` format. Install the same repository in the personal skill directory for your agent.

| Agent | Documentation | Personal skill directory |
|---|---|---|
| Codex | [Agent Skills](https://developers.openai.com/codex/skills/) | `~/.agents/skills/` |
| Claude Code | [Agent Skills](https://code.claude.com/docs/en/skills) | `~/.claude/skills/` |
| OpenCode | [Skills](https://opencode.ai/docs/skills/) | `~/.config/opencode/skills/` |

## Install

### Codex

```bash
git clone https://github.com/santoshyadav979439/impact-resume-builder.git ~/.agents/skills/impact-resume-builder
```

### Claude Code

```bash
git clone https://github.com/santoshyadav979439/impact-resume-builder.git ~/.claude/skills/impact-resume-builder
```

### OpenCode

```bash
git clone https://github.com/santoshyadav979439/impact-resume-builder.git ~/.config/opencode/skills/impact-resume-builder
```

Restart the agent after installation so it can discover the skill.

Python 3 is required for the dependency checker. From the cloned repository, run:

```bash
python3 scripts/setup_dependencies.py
```

The script checks for Tectonic and Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`, and `pdffonts`). When Homebrew is available, it installs missing packages with `brew install`. On other platforms, install Tectonic and Poppler with your package manager, then rerun the script.

## Use

Attach an existing resume or provide career notes, then ask your agent:

> Use the impact-resume-builder skill to create a resume for a senior software engineer role. Read my existing resume, ask about unclear achievements and missing impact, then produce the LaTeX source and PDF.

The skill instructions are in [SKILL.md](SKILL.md), and the editable starting point is [assets/resume-template.tex](assets/resume-template.tex).
