# AGENTS.md — Star Rail Meme Wiki

## 1. Purpose

Build and maintain a **Traditional Chinese Markdown LLM Wiki** about the interaction between meme culture and official narratives in *Honkai: Star Rail*. Focus on: (1) the Trailblazer/trash-can meme, (2) Elation and related game content, and (3) the boundary between official content, officially supported fanworks, community interpretations, and unverified rumors.

The final output is a beginner-friendly **teaching HTML slide deck** in `slides/index.html`, written in Traditional Chinese with English technical field names. Tone: educational and semi-academic, with restrained humor. Do not assume readers know the game.

## 2. Repository Layout

```text
raw/                 # Curated source snapshots; never silently alter originals
  official/
  articles/
  community/
wiki/
  index.md            # Linked catalog of Wiki pages
  log.md              # Append-only operations and review log
  sources/            # One source note per ingested document
  concepts/           # Cross-source concepts
  cases/              # Case studies
  syntheses/          # Cross-case analysis
slides/
  index.html          # Standalone HTML/CSS/JS teaching slides
AGENTS.md
README.md
```

Create directories and pages when needed; do not create empty placeholder files merely to match the tree.

## 3. Source and Evidence Policy

- Ingest **at least five distinct, inspectable source documents**. A case study is not itself a source. Use a mix of official publications, secondary reporting, and community discussions.
- Store a local snapshot or readable transcription/notes for each source in `raw/`, with its title, original URL, publisher, publication date (if known), and access date. Respect copyright: summarize rather than reproducing long copyrighted text.
- Treat `raw/` as immutable: never overwrite or silently rewrite an original source. If a snapshot changes, create a new version and log the reason.
- Never invent source texts, URLs, quotations, dates, internal development motives, or citations. If a source is inaccessible, mark it `unverified` and do not treat it as ingested evidence.
- Distinguish **source_authenticity** (who published it) from **canonical_status** (whether a specific claim belongs to the game's canon). An official publication does **not** automatically imply canonical status.
- Use `source_authenticity`: `official`, `official_supported`, `community`, `secondary`, `unknown`.
- Use `canonical_status` per claim: `canon`, `non_canon`, `interpretation`, `unverified`, `not_applicable`.
- Clearly label jokes, sarcasm, fan theories, rumors, and the Wiki author's interpretation. Political or development rumors must not be presented as confirmed causes without direct supporting evidence.

## 4. Wiki Page Conventions

- Write explanatory prose in Traditional Chinese; use English for technical field names, file names, and identifiers.
- Every `wiki/sources/SRC-XXX.md` must include metadata: `id`, `title`, `type: source`, `publisher`, `url`, `published_at` (or `unknown`), `accessed_at`, `source_authenticity`, `raw_path`.
- Each case/concept/synthesis page must identify supporting `source_ids` and explicitly qualify significant claims. If a page mixes multiple types of claims, **assign `canonical_status` at claim level**, not only at page level.
- Each important claim must be traceable to a source note, ideally to a section, timestamp, or quoted short excerpt. Conflicting sources should be described side by side rather than silently reconciled.
- Use relative Markdown links between Wiki pages. Keep `wiki/index.md` current and avoid unlinked/orphaned pages.

## 5. Ingest Workflow — Human Review Required

For **each source, one at a time**:

1. **Register**: identify the document and preserve the raw source with provenance.
2. **Extract**: draft a source note with a concise summary, key claims, and relevant evidence pointers.
3. **Classify & check**: label source authenticity and each claim's canonical status; flag uncertainty, contradictions, and missing evidence.
4. **Stop for human review**: present the proposed summary, labels, and intended Wiki page changes. **Do not modify `wiki/` until the user explicitly approves this ingest.**
5. **Integrate after approval**: write/update the source note and affected case, concept, synthesis, and index pages; preserve prior valid knowledge.
6. **Log**: append source ID, date, updated files, user decision, and remaining uncertainties to `wiki/log.md`.

If review rejects any claim, return to **Extract / Classify** and revise before integration. Never record a proposed ingest as completed.

## 6. Query Workflow

1. Read `wiki/index.md` and retrieve relevant Wiki pages.
2. Produce an answer using Wiki evidence, with source IDs and links to relevant pages.
3. Separate supported facts, interpretation, and unknowns. When evidence is missing or contradictory, say so; propose a source to investigate rather than filling the gap from memory.
4. Do not edit the Wiki merely by answering a query. Propose useful new synthesis pages for user review and approval.

## 7. Lint Workflow

Check for: broken internal links; missing or duplicate IDs; missing provenance; claims without source support; inconsistencies between pages; conflation of official/official-supported/canon; outdated or contradicted information; and orphan pages.

Report problems with **file, claim, severity, proposed fix**, and whether human judgment is required. Mechanical repairs may be proposed, but any **substantive knowledge change requires user approval**. Record completed checks and repairs in `wiki/log.md`.

## 8. Generate HTML Slides Workflow

1. Define a beginner-friendly learning objective and outline (typically 10–12 slides).
2. **Query the existing Wiki first**. Create a slide-to-claim/source mapping before writing slide prose.
3. Verify that each factual statement is supported by a source already represented in the Wiki. If not, return to **Query**; if the Wiki itself lacks evidence, return to **Ingest and human review**.
4. Create `slides/index.html` using native HTML, CSS, and JavaScript; no framework or build step required. Make it readable on desktop and mobile, with keyboard/navigation controls and accessible text.
5. Check navigation, rendering, references, beginner comprehension, and distinctions between fact, fan interpretation, and unverified rumor. Fix and recheck failures.
6. Record generation inputs, tested outputs, found errors, fixes, and verification results in `wiki/log.md`.

Use images only when licensing and attribution are appropriate. Do not embed copyrighted music or long copyrighted text.

## 9. Loop / Graph Rules

- **Ingest loop:** Register → Extract → Classify/Validate → **Human Review** → Integrate → Log. Failure or rejection returns to Extract/Classify.
- **Query loop:** Retrieve → Check evidence → Answer. Missing evidence returns to retrieval or a new reviewed ingest.
- **Generate loop:** Wiki query → Outline → Claim check → HTML → UI/content check. Unsupported claims return to Wiki query/ingest; UI failures return to HTML generation.
- Keep a genuine run record: what actually ran, what failed, what was changed, and what passed. Do **not** invent test results, error counts, or before/after improvements.

## 10. Completion Checklist

- [ ] At least five **distinct source documents** have been ingested and human-approved.
- [ ] `wiki/index.md` and `wiki/log.md` reflect actual Wiki updates.
- [ ] Claims distinguish source authenticity from canonical status.
- [ ] Slides teach the topic to beginners and trace key claims back to Wiki sources.
- [ ] HTML slides are browsable and checked on the intended deployment.
- [ ] The submitted report explains the graph, repeated nodes, one real run, errors, changes, and reflection.

When uncertain, **ask before changing facts**; prioritize accuracy and traceability over novelty or jokes.
