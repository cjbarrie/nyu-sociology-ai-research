# Instructions for assistants editing this presentation

Read `docs/CO_PRESENTER.md` first. This is a 15-minute NYU Sociology faculty presentation, not a product pitch. Use ordinary academic language, avoid slogans, and preserve claim qualifications and source provenance.

- Current deck: 14 slides, ending with the research proposal. Do not reintroduce the removed phone app or add a showstopper unless requested.
- Main browser source: app/page.tsx; opening slides: app/opening.tsx; style: app/globals.css.
- When slide text or order changes, update scripts/presentation_pdf.py and regenerate the PDF and notes if dependencies are available. Report explicitly if not regenerated. Preserve the fifteen-minute timing total.
- Separate actual execution recordings, scripted teaching dialogue, schematic diagrams and hypothetical results. Never invent authentic execution footage or study results.
- Check primary sources before changing empirical claims. Keep academic PDFs and evidence tables directly accessible.
- Prefer an editing branch and pull request. Follow the user's explicit publication instructions. GitHub Pages publishes main automatically; the older Sites deployment is separate.
- Run npm run build for browser changes. Do not edit dist/client as source. scripts/github_pages.py adapts the export for the repository URL at deployment.
- Do not commit secrets, local participant data, node_modules, research/sources, or machine-specific caches. The removed app must not be reintroduced through archives.
- Preserve existing design and scope. Do not regenerate the research corpus or introduce new dependencies for a small copy edit.
