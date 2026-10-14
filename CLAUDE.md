# Book Draft: এআই কীভাবে সিদ্ধান্ত নেয় (How AI Makes Decisions)

A Bengali-language book explaining AI decision-making concepts to a general audience.

## Project Structure

- `এআই_কীভাবে_সিদ্ধান্ত_নেয়_Bengali.docx` — Master manuscript (all chapters combined)
- `chapters/` — Individual chapter `.docx` files (00–11), split from the master for easier editing
- `split_chapters.py` — Splits master `.docx` into per-chapter files in `chapters/`
- `merge_chapters.py` — Merges chapter files back into the master document

## Chapter Workflow

Edit individual chapters in `chapters/`, then merge back:

```bash
# Split master into chapters (overwrites chapters/)
python split_chapters.py

# Merge chapters back into master (overwrites master .docx)
python merge_chapters.py
```

Chapter files are numbered `00_title.docx` through `11_*.docx`. The split script detects chapters by `Heading1` style boundaries. The merge script re-adds a Table of Contents and page numbers.

## Document Format

- All content is `.docx` (Word format), not Markdown
- Font: **Noto Serif Bengali**
- Language: Bengali (বাংলা)
- Python tooling uses `python-docx` library
- Chapters are split on `Heading1` style; title page uses `Title` style

## Dependencies

```bash
pip install python-docx
```

## Writing

- **Read `docs/style-guide.md` before writing or editing any chapter.** It defines the voice, terms and numerals.
- Revision work happens in `chapters-md/` (see `docs/revision-spec.md`).
- `tools/check.sh <file>` runs Vale (`styles/Bangla/`) + Hunspell bn_BD; a hook runs it after every edit to `chapters-md/`. Add accepted words to `tools/wordlist.txt`.
- Editor agents in `.claude/agents/`: `beta-reader`, `line-editor`, `fact-checker` (all report-only).
- Website: every push to `main` publishes `chapters-md/` to GitHub Pages via mdBook (`book.toml`, `chapters-md/SUMMARY.md`, `site/`, `.github/workflows/pages.yml`). When a chapter is revised, delete its `> **খসড়া:** …` note.
- Setup on a new machine: `brew install vale hunspell`; put `bn_BD.aff`/`bn_BD.dic` (GPL-2, from the "bn-BD spellchecker" Firefox add-on by Bangla Type Foundry) in `~/Library/Spelling/`.

## Skills

- `.agents/skills/doc-coauthoring/` — Structured workflow for co-authoring documentation (context gathering, refinement, reader testing)
- `.agents/skills/docx/` — Creating, reading, and editing `.docx` files (docx-js for creation, XML unpack/edit/repack for editing existing docs)
