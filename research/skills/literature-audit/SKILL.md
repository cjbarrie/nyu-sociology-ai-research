---
name: literature-audit
description: Conduct a bounded scoping review of an empirical social-science question, with a source-checked evidence table and bibliography. Use for literature mapping and claim checking; do not label the result a systematic review.
allowed-tools: Read Grep Glob WebSearch WebFetch Write Edit Bash(pdftotext *) Bash(pdfinfo *)
---

## Tool permissions (Claude Code example)

The `allowed-tools` header pre-approves the listed tools for the turn in which this skill is invoked in Claude Code. Read, Grep and Glob inspect local files; WebSearch and WebFetch retrieve web material; Write and Edit produce the research files. The Bash patterns allow `pdftotext` and `pdfinfo` commands for PDF extraction and metadata inspection; those programs must already be installed. This is not unrestricted Bash access, and unlisted tools remain subject to the session's permission settings. The header does not install tools, provide subscriptions or bypass access restrictions. Other agent environments may handle permissions differently; use their own permission controls.

Reference: [Claude Code skill permissions](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill).

Start by specifying the population, exposure, comparison and outcome. If the outcome is ambiguous, ask one concrete question while searching the independent parts.

Search primary research with several recorded queries. Record the date, search service, inclusion decisions and stopping rule. Aim for 8–12 relevant studies unless the researcher specifies otherwise. Follow useful citations, but report incomplete coverage.

Open the primary source. For each study record authors, title, year, DOI or stable URL, publication status and version, design, sample, exposure, actual outcome instrument, main finding, limitation and a passage locator. Distinguish full-text reading from abstract-only access. A successful HTTP response is not proof that a paper was retrieved.

Keep measured behavior distinct from intentions, perceived support, loneliness and general social interaction. Keep randomized assignment distinct from voluntary use. Separate a null finding from evidence of no meaningful effect.

Write evidence.csv, search-log.md and references.bib in the research folder. Check bibliography metadata against the source. Write a short synthesis identifying which claims are supported and which need a different study.

If asked to use a team, assign one reviewer to source support and another to design and measurement. Have each read the other's objections. Preserve disagreements and ask the researcher about consequential choices. Do not invent the researcher's answers or treat agreement among agents as validation.

When revising, preserve the previous draft and record the substantive change. Link every empirical claim to its evidence record. Label proposed studies and simulated examples explicitly.
