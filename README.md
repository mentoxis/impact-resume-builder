# Impact Resume Builder

A reusable [Agent Skill](https://agentskills.io/) for Codex, Claude Code, and OpenCode. It creates an impact-driven, ATS-friendly resume from an existing resume or from career details pasted as text. It asks for missing evidence before writing and never invents metrics, roles, dates, or credentials. Candidate resumes and personal details stay outside this repository.

## What it does

1. Lets the candidate choose how to start: paste their full career content and experience as text, or share an existing resume file.
2. Asks focused questions about ownership, the problem solved, actions, scale, and outcomes. It asks for numbers only when the candidate can verify them.
3. For candidates with more than 3 years of professional experience, removes 10th and 12th grade entries and academic scores (percentage, CGPA, GPA) from Education, and tells the candidate why.
4. Recommends a one-page resume for candidates with less than 4 years of experience and builds two pages otherwise.
5. Writes concise, relevant achievement bullets and builds a single-column LaTeX resume designed for straightforward ATS parsing, with every page filled and no blank gaps.
6. Compiles the PDF with Tectonic, checks page count, extracted text, fonts, links, and rendered pages with Poppler tools, and runs `scripts/check_page_fill.py` to catch blank space.

The output is an editable `.tex` file and a PDF, organized in numbered versions. Unconfirmed facts are flagged for review.

## What's new in v2.1

- **No blank space:** every page, including the first, must be filled to within 0.75in of the bottom margin. `scripts/check_page_fill.py` fails on any page that leaves more. Short pages are filled with verified content; if there isn't enough, the resume drops to fewer pages.
- **Template fix:** removed `\needspace` from job headings. It could push a whole job to the next page and leave several inches blank on page 1.
- **Page length by experience:** less than 4 years of experience gets a recommended one-page resume; 4 years or more gets two pages.

## What's new in v2

- **Two input modes:** paste career content as text, or share an existing resume.
- **Education trimming:** with more than 3 years of experience, 10th and 12th grade details and academic scores are removed from Education, and the candidate is told these details are not required at that level. Work-impact percentages in experience bullets are kept.
- **ATS-friendly filenames:** outputs use names such as `First_Last_Resume.pdf`, with version numbers kept in the directory.

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
git clone https://github.com/mentoxis/impact-resume-builder.git ~/.agents/skills/impact-resume-builder
```

### Claude Code

```bash
git clone https://github.com/mentoxis/impact-resume-builder.git ~/.claude/skills/impact-resume-builder
```

### OpenCode

```bash
git clone https://github.com/mentoxis/impact-resume-builder.git ~/.config/opencode/skills/impact-resume-builder
```

Restart the agent after installation so it can discover the skill.

Python 3 is required for the dependency checker. From the cloned repository, run:

```bash
python3 scripts/setup_dependencies.py
```

The script checks for Tectonic and Poppler (`pdfinfo`, `pdftotext`, `pdftoppm`, and `pdffonts`). When Homebrew is available, it installs missing packages with `brew install`. On other platforms, install Tectonic and Poppler with your package manager, then rerun the script.

## Use

Choose one input mode, then ask your agent.

With an existing resume attached:

> Use the impact-resume-builder skill to create a resume for a senior software engineer role. Read my existing resume, ask about unclear achievements and missing impact, then produce the LaTeX source and PDF.

With career details as text:

> Use the impact-resume-builder skill to create a resume for a senior software engineer role. Here is my full experience: roles, employers, dates, what I worked on, results, education, skills, and contact details. Ask about missing impact, then produce the LaTeX source and PDF.

The skill instructions are in [SKILL.md](SKILL.md), and the editable starting point is [assets/resume-template.tex](assets/resume-template.tex).

## How to contribute

Contributions are welcome: new resume rules, template fixes, support for more agents, better checks, and documentation.

### Repository layout

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | The skill instructions the agent follows. Most behavior changes go here. |
| [assets/resume-template.tex](assets/resume-template.tex) | Single-column, ATS-friendly LaTeX template. |
| [scripts/setup_dependencies.py](scripts/setup_dependencies.py) | Checks and installs Tectonic and Poppler. |
| [scripts/check_page_fill.py](scripts/check_page_fill.py) | Fails when a rendered page leaves blank space. |

### Workflow

1. Open an [issue](https://github.com/mentoxis/impact-resume-builder/issues) describing the bug or idea before large changes, so the approach can be agreed first.
2. Fork the repository and create a branch from `main`, for example `fix/page-fill-threshold` or `feat/cover-letter-mode`.
3. Install the skill from your fork into your agent's skill directory (see [Install](#install)) and run `python3 scripts/setup_dependencies.py`.
4. Make the change, then test it end to end: ask your agent to build a resume with a **sample or anonymized profile**, compile the PDF, and run `python3 scripts/check_page_fill.py` on it.
5. Commit with [Conventional Commits](https://www.conventionalcommits.org/) prefixes (`feat:`, `fix:`, `docs:`), matching the existing history.
6. Open a pull request against `main`. Describe what changed, why, which agent you tested with (Codex, Claude Code, or OpenCode), and attach a screenshot of the generated PDF when the layout changes.

### Ground rules

- **No personal data.** Never commit real resumes, names, contact details, or generated PDFs. Use fictional or anonymized examples.
- **No invented facts.** Changes must keep the core rule: the skill never fabricates metrics, roles, dates, or credentials.
- **ATS first.** Keep the template single-column and text-extractable; avoid tables, icons, and multi-column layouts in the resume body.
- **Keep it portable.** `SKILL.md` must stay valid for every supported agent; agent-specific notes belong in the README.
- **Document user-visible changes** in the README's "What's new" section.
