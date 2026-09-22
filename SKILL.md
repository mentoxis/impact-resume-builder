---
name: impact-resume-builder
description: Use when building a new, impact-driven resume from a person's existing resume or career notes.
---

# Impact Resume Builder

Create a new, evidence-based resume from a candidate's existing resume. Keep candidate files and personal details outside this reusable skill directory.

## Gather evidence

Ask for the existing resume before drafting. If none exists, ask for career history, education, skills, and contact details. Read the full source. Ask for the target role, seniority, and job description when they affect emphasis. Do not repeat questions already answered in the source.

For each role, find the important gaps: ownership, problem, action, beneficiaries, scale, and result. Ask focused questions in manageable groups, especially where a duty could become an achievement. Request numbers only when the candidate can verify them: before and after measures, volume, adoption, revenue, time saved, reliability, or team scope. Follow up on ambiguous answers. Use a concrete qualitative outcome when no reliable metric exists. Never invent achievements, metrics, employers, dates, credentials, or technologies. Mark unresolved claims for confirmation before finalizing.

## Write for impact and ATS parsing

Select relevant experience and write concise bullets that connect action, context, and supported outcome. Lead with the strongest evidence. Avoid generic duties, inflated language, and keyword stuffing.

Start from [assets/resume-template.tex](assets/resume-template.tex), replacing every placeholder with verified candidate information. Use its single-column layout with straightforward headings and reading order. Default to 0.65in margins and exactly two pages unless the candidate explicitly requests another length. Keep body and contact text readable with comfortable line spacing. Use a fixed-width label column so skills values align. Prevent automatic line-end word hyphenation, while preserving explicit compound hyphens. Disable font ligatures so extracted ATS text keeps ordinary letter sequences.

Bold only short achievement spans showing measurable business impact, performance change, scale, time or cost savings, or leadership scope. Keep technologies, dates, action verbs, responsibilities, evaluation criteria, and qualitative claims in regular weight. Never change wording merely to create a bold span.

## Build and verify

Run `python3 <this-skill>/scripts/setup_dependencies.py` before building. It checks for Tectonic and Poppler tools and installs missing packages through Homebrew when available. On another platform, install the missing tools with its package manager and rerun the check. If installation is blocked, report the specific blocker.

Save each revision in `versions/<resume family>/vN/`, choosing the next number within that family. Include the editable `.tex` source, compiled PDF, and `VERSION.md` recording family, version, key change, and email variant. Do not modify or remove earlier numbered versions. Create only the primary-email variant unless another is requested.

Compile twice with Tectonic and inspect its logs for errors or layout warnings. Use Poppler `pdfinfo` to check the page count and links, `pdftotext` to verify reading order, facts, and unbroken keywords, and `pdffonts` to inspect embedded fonts. Render every page with `pdftoppm` and visually check clipping, overlap, alignment, and legibility. Check extracted text for ligature characters. Deliver the `.tex` source and PDF with any facts awaiting confirmation. Never publish candidate data with this skill.
