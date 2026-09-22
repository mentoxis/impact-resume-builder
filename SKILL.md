---
name: impact-resume-builder
description: Use when building a new, impact-driven resume from a person's existing resume or career notes.
---

# Impact Resume Builder

Create a new resume grounded in the candidate's real work. Keep the source resume and all candidate data outside this skill's directory.

## Collect the facts

Ask for the existing resume before drafting. If there is no resume, request career history, education, skills, and contact details instead. Read the full source, then ask for the target role and any job description when they would affect emphasis. Do not ask for facts already clear in the source.

Identify the most useful gaps in each role: ownership, problem, action, beneficiaries, scale, and result. Ask focused questions in manageable groups, especially where a responsibility could become an achievement. Request numbers only when the candidate can verify them; useful evidence includes before and after measures, volume, adoption, revenue, time saved, reliability, and team scope. Ask follow-up questions when an answer remains ambiguous. If a number is unavailable, write a concrete qualitative outcome. Never invent achievements, metrics, employers, dates, credentials, or technologies. Flag unresolved claims for confirmation before finalizing.

## Write the resume

Select experience relevant to the target role. Write concise bullets that connect the candidate's action to its context and outcome. Lead with the strongest supported impact, and preserve the meaning of the source. Avoid generic duties, inflated language, and keyword stuffing. Use ATS-friendly headings, a clear reading order, and a simple single-column layout by default. Choose page count based on experience and the target market, rather than forcing a fixed length.

## Create and verify files

Ask for an output format if it is unclear and materially affects the work; otherwise provide a PDF and editable source. For the default PDF workflow, run `python3 <this-skill>/scripts/setup_dependencies.py --venv <work-dir>/.venv` before generating the resume. This installs ReportLab for PDF creation and PyMuPDF for rendering and text extraction in an isolated environment. Use that environment's Python for the work. If installation is blocked, explain the specific blocker and request the needed access; do not claim the PDF is ready.

Extract text from the finished PDF and compare names, dates, headings, and achievement claims with the approved draft. Render and inspect every page for clipping, overlap, alignment, and legibility. Deliver the editable source and final PDF, along with any facts still awaiting confirmation. Never publish the candidate's resume or personal details as part of this skill.
