# Using the literature-audit skill

This instruction-only skill was written for the NYU Sociology workshop. It is not an official OpenAI or Anthropic literature-review product. Inspect SKILL.md before using it.

## Codex CLI or IDE

1. Download literature-audit.zip from the workshop page and unzip it.
2. Put its literature-audit folder inside your project's .agents/skills/ directory.
3. Open that project in Codex. Type $literature-audit, or choose it using /skills in the CLI.
4. Paste the assignment below. If it is not discovered, restart Codex. The file can also be attached directly and its instructions explicitly requested.

## Claude Code

Put the same folder inside your project's .claude/skills/ directory. Open Claude Code in that project and type /literature-audit followed by the assignment. If the top-level skills folder is new, restart the session.

These are local project instructions. Web search, file access and LaTeX compilation depend on the tools and software available in that session. The skill itself supplies no database subscription or credentials.

## Tool permissions (Claude Code example)

The `allowed-tools` header pre-approves the listed tools for the turn in which this skill is invoked in Claude Code. Read, Grep and Glob inspect local files; WebSearch and WebFetch retrieve web material; Write and Edit produce the research files. The Bash patterns allow `pdftotext` and `pdfinfo` commands for PDF extraction and metadata inspection; those programs must already be installed. This is not unrestricted Bash access, and unlisted tools remain subject to the session's permission settings. The header does not install tools, provide subscriptions or bypass access restrictions. Other agent environments may handle permissions differently; use their own permission controls.

Reference: [Claude Code skill permissions](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill).

## Assignment to paste

Assess whether AI chatbots reduce requests for emotional support or personal advice to existing friends and family. Conduct a bounded search for 8–12 primary studies. Record queries and exclusions, check the actual outcome instruments and publication versions, and write evidence.csv, search-log.md and references.bib. Before drafting a conclusion, ask me about any consequential ambiguity in the outcome. Then propose a study that measures actual outreach. Use separate source and methods reviewers, and have them cross-check each other's objections. Preserve their reports and questions. Do not invent my answers.

## What to open during the talk

Open the skill file first. Show the installation path and the prompt above. Then open the evidence table and one primary paper side by side. The existing review was prepared before this reusable skill; the skill codifies that workflow. The two reviewer reports were produced by actual separate agents during revision. The paired dialogue is a scripted teaching example, clearly marked as such.

Official instructions checked 9 September 2026:
- https://learn.chatgpt.com/docs/build-skills
- https://code.claude.com/docs/en/skills
