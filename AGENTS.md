# AGENTS.md

## Project

CSP Math — a bilingual (English / 中文) GitBook built from the mathematics
requirements of the **NOI Syllabus, 2025 Edition** (全国青少年信息学奥林匹克系列
竞赛大纲 2025 年修订版). The source PDF lives outside this repo at
`D:\cspbook\syllabus\NOI_Syllabus_Edition_2025.pdf`.

## Layout

- `gitbook-docs.yaml` — GitBook Git Sync site configuration (schema:
  https://api.gitbook.com/gitbook-docs.yaml). Maps content directories to
  sections/spaces.
- `introductory/en/`, `introductory/zh/` — 入门级 (Introductory Level, CSP-J)
  content, one GitBook space per language, mirroring syllabus section 2.1.5
  "数学与其他" (Mathematics and Others).
- Each space directory contains `README.md` (landing page), `SUMMARY.md`
  (table of contents) and one Markdown page per syllabus topic. A topic with
  substantial content (e.g. 初等数论 / Elementary Number Theory) is a folder:
  `README.md` as the topic landing page plus one sub-page per syllabus item,
  each with description (讲解), worked examples (例题) and practice problems
  (练习).

## Conventions

- Content is bilingual: every topic exists as an English page under `en/` and a
  Chinese page under `zh/` with the same filename; keep the two in sync.
- Stay faithful to the syllabus: keep the 【n】 difficulty coefficient tags next
  to each item, and do not add topics beyond the syllabus section being covered.
- When adding a new syllabus level (e.g. 提高级, NOI 级), add a new top-level
  section in `gitbook-docs.yaml` with `en`/`zh` spaces, and keep exactly one
  `default: true` per section and exactly one default section per site.
- Every `content.directory` referenced in `gitbook-docs.yaml` must exist in the
  repo.

## Status / roadmap

- [x] 入门级 Introductory Level — 2.1.5 数学与其他 (en + zh)
- [ ] 提高级 Advanced Level — math sections
- [ ] NOI 级 NOI Level — math sections
