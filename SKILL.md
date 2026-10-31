---
name: impact-resume-builder
description: Use when building a new, impact-driven resume from a person's existing resume file or from career details pasted as text.
metadata:
  version: "2.1"
---

# Impact Resume Builder

Create a new, evidence-based resume from a candidate's existing resume or from career details they provide as text. Keep candidate files and personal details outside this reusable skill directory.

## Keep the skill reusable and private

Use [assets/resume-template.tex](assets/resume-template.tex) as the canonical visual style for every resume. Put candidate-specific content only in the generated version directory. Do not add names, contact details, employers, dates, achievements, links, or other candidate data to this skill, its template, or its scripts. Keep generic placeholders in the template.

## Choose the input mode

Before gathering evidence, offer the candidate two ways to start, unless their first message already makes the choice clear:

1. **Text input:** paste their full career content and experience as text, including roles, employers, dates, responsibilities, achievements, education, skills, and contact details.
2. **Resume input:** share an existing resume file such as PDF, DOCX, or TeX.

Treat both modes the same after intake. Read the full source. For text input, extract the same facts a resume would contain and ask for any missing basics: role titles, employers, start and end dates, education, skills, and contact details. Ask for the target role, seniority, and job description when they affect emphasis. Do not repeat questions already answered in the source.

## Gather evidence

For each role, find the important gaps: ownership, problem, action, beneficiaries, scale, and result. Ask focused questions in manageable groups, especially where a duty could become an achievement. Request numbers only when the candidate can verify them: before and after measures, volume, adoption, revenue, time saved, reliability, or team scope. Follow up on ambiguous answers. Use a concrete qualitative outcome when no reliable metric exists. Never invent achievements, metrics, employers, dates, credentials, or technologies. Mark unresolved claims for confirmation before finalizing.

## Calculate experience

Calculate total professional experience from the role dates in the source. Count full-time and contract roles, merge overlapping periods, count a current role up to today, and exclude internships and academic projects. If missing dates or an unclear employment type could change which side of the 3-year or 4-year thresholds the total falls on, ask before applying the rules below. Record the calculated experience in `VERSION.md`.

## Trim education for experienced candidates

When total experience is more than 3 years:

- Remove 10th grade (secondary school, SSC, or equivalent) and 12th grade (higher secondary, HSC, or equivalent) entries from the Education section. Keep the highest degree and any later degrees or certifications.
- Remove academic scores from education entries, including percentages, CGPA, and GPA. Keep the degree, institution, and dates.
- Tell the candidate in one short message, sent with your evidence questions and before drafting, that these details will be left out because recruiters do not require them for a candidate with more than 3 years of experience. Include their calculated experience. Keep the details only if the candidate explicitly asks.
- Record the removed education details in `VERSION.md`.

This rule applies only to education. Keep verified percentages that describe work impact, such as latency reduced by 40%, in experience bullets.

When total experience is 3 years or less, keep education details as provided.

## Choose the page length

- When total experience is less than 4 years, recommend a one-page resume. Tell the candidate in the same message as other intake notes, with their calculated experience, and build one page unless they explicitly ask for two.
- When total experience is 4 years or more, build two pages unless the candidate explicitly asks for another length.

Record the chosen page count and the reason in `VERSION.md`.

## Write for impact and ATS parsing

Select relevant experience and write concise bullets that connect action, context, and supported outcome. Lead with the strongest evidence. Avoid generic duties, inflated language, and keyword stuffing.

Start from [assets/resume-template.tex](assets/resume-template.tex), copy it into the new version directory, and replace every placeholder there with verified candidate information. Preserve the template's visual system so new resumes match earlier skill-created resumes.

### ATS layout rules

- Use a single text column with a direct reading order. Do not use tables, sidebars, text boxes, icons, charts, headers, footers, or multi-column content.
- Use letter paper, 10pt Latin Modern Roman, 0.65in margins, black text, uppercase ruled section headings, and the spacing values in the template.
- Keep body and contact text readable with comfortable line and vertical spacing.
- Use the template's fixed-width skills label column so all skill values start at the same horizontal position.
- Use simple section names, standard bullet lists, and text contact links that remain meaningful after PDF text extraction.
- Prevent automatic line-end word hyphenation, but preserve explicit compound hyphens.
- Disable common font ligatures so extracted ATS text contains ordinary letter sequences.
- Keep job headings with the first bullet when space permits. Do not allow clipped, overlapping, or orphaned content.
- Produce the page count chosen under "Choose the page length". Do not shrink text, margins, or template spacing to force it; select and tighten content instead.
- Leave no blank space. Every page, including the first and the last, must be filled to within 0.75in of the bottom margin, with no gaps between sections beyond the template spacing. Do not use `\vfill`, `\newpage`, `\needspace`, or manual `\vspace` to move content; the template's section headings already stay with the line that follows them.
- When a page runs short, add verified, relevant content first: stronger bullets for recent roles, projects, certifications, or skills from the evidence. Ask the candidate for more when the evidence runs out. Never fill space with generic duties, repetition, or invented content. If verified content still cannot fill the pages, drop to fewer pages and tell the candidate. When content overflows, cut the weakest bullets.

Bold only short achievement spans showing measurable business impact, performance change, scale, time or cost savings, or leadership scope. Keep technologies, dates, action verbs, responsibilities, evaluation criteria, and qualitative claims in regular weight. Never change wording merely to create a bold span.

## Build and verify

Run `python3 <this-skill>/scripts/setup_dependencies.py` before building. It checks for Tectonic and Poppler tools and installs missing packages through Homebrew when available. On another platform, install the missing tools with its package manager and rerun the check. If installation is blocked, report the specific blocker.

Save each revision in `versions/<resume family>/vN/`, choosing the next number within that family. Include the editable `.tex` source, compiled PDF, and `VERSION.md` recording family, version, key change, and email variant. Use ATS-friendly resume filenames such as `First_Last_Resume.pdf` and matching `First_Last_Resume.tex`; add a short role suffix only when needed to distinguish variants. Use plain ASCII letters and underscores, with no spaces or version numbers in the resume filenames. Keep version numbers in the directory and `VERSION.md`. Do not modify or remove earlier numbered versions. Create only the primary-email variant unless another is requested.

Compile twice with Tectonic and inspect its logs for errors or layout warnings. Use Poppler `pdfinfo` to check the page count, paper size, and links; use `pdftotext -layout` to verify reading order, facts, contact details, and unbroken keywords; and use `pdffonts` to confirm that Latin Modern fonts are embedded with Unicode mappings. Run `python3 <this-skill>/scripts/check_page_fill.py <resume>.pdf` and fix every page it reports as FAIL, including the first page; a section or job pushed to the next page must not leave a gap behind it. Render every page with `pdftoppm` and visually check clipping, overlap, alignment, page balance, blank space, readable spacing, and legibility. Check extracted text for ligature characters and confirm that important ATS keywords are intact. When the experience rule applies, confirm that the extracted Education section contains no 10th or 12th grade entries and no percentages, CGPA, or GPA. Deliver the `.tex` source and PDF with any facts awaiting confirmation and a note on any removed education details. Never publish candidate data with this skill.
