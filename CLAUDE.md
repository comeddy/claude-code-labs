# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

Materials for the **Claude Code Deep Dive Workshop** (2nd run): self-paced, Korean-language hands-on lab documents, each shipped as a single self-contained HTML file. There is no application code, package manager, or test framework — the deliverables are the HTML docs themselves.

## Where things live

- `labs/` — the deliverables: `index.html` (portal), `ClaudeCode_Ch1..Ch6_HandsOnLab.html` (chapter labs), `ClaudeCode_Capstone{1-4,A-D}_HandsOnLab.html` (capstone labs), `ClaudeCode_Capstone_Setup.html`, `ClaudeCode_Preflight_Check.html`, `ClaudeCode_Reference{1-3}_*.html`, `eDM.html` (session intro).
- `.claude/skills/HoL-Style-01/` — the **HoL-Style-01 design system skill** (auto-discovered as a project skill): `SKILL.md` plus the build assets `assets/lab_head.html`, `assets/lab_tail.html`, `assets/helpers.py`, `assets/qa.py`.
- `.remember/` — Remember plugin session-history storage (git-ignored). Never store deliverables here; the copies of the skill zip/SKILL.md remaining there are stale duplicates of `.claude/skills/HoL-Style-01/`.

## Creating or editing a lab document

Always follow `.claude/skills/HoL-Style-01/SKILL.md` — it is the authoritative spec. The short version:

1. **Clarify variant first**: Chapter Lab (40–80 min, T0 + 3–5 Tasks, CHECKPOINT verdicts) vs Capstone Mission (135 min target, MISSION 00–05, DEFINITION OF DONE verdicts, plus MISSION BRIEFING divider, OPTION sections, and a cut-line/troubleshooting appendix).
2. **Assets before prose**: every code snippet that appears in a doc must first exist as a real file in a separate directory and be verified there (`node --check`, `bash -n`, unit tests for pure logic, mock-server e2e for scripts). Unverified code never ships in a doc.
3. **Assemble**: `assets/lab_head.html` verbatim (swap only the `<title>`) + body generated via Python using `assets/helpers.py` (`esc`/`code`/`sol`/`heredoc`) + `assets/lab_tail.html` (substitute `{{LAB_TITLE}}`, `{{BASELINE}}`, `{{TASK_GROUPS}}`, `{{TASK_COUNT}}`). Never write new CSS — the head template is the validated design system.
4. **Validate**: `python3 assets/qa.py <output>.html <asset-dir>` must fully pass (HTML balance, JS syntax, punctuation rules, banned words, heredoc round-trip, 1280/420px viewport fit).
5. **Pixel spot-check**: `wkhtmltoimage` render at 1280px — dark-pixel ratio 75%+, right-edge overflow < 0.03%, traffic-light colors present.
6. **Ship**: name it `ClaudeCode_<Name>_HandsOnLab.html`, add a row to the portal `index.html`, and verify the link resolves.

## Hard content rules (frequent failure points)

- Punctuation: no middle dot (U+00B7) and no em-dash (U+2014); use commas/slashes, and hyphens for dashes. One exception per document for verbatim UI-string quotes.
- Heredoc markers must be unique uppercase+`EOF` per document (e.g. `MEDICEOF`) and never reused — the QA round-trip check depends on this.
- `details.solution` blocks must stay **byte-identical** to their source asset files; editing one side means updating the other.
- Self-paced only: no wording that assumes a facilitator, neighbors, or synchronized group activity. DoD/CHECKPOINT statements must be observable facts a solo learner can verify.
- Escape everything placed inside `<pre>` via `esc()`; raw `<` or `&` from string concatenation breaks the parser.
- Model IDs used in labs: Bedrock default `global.anthropic.claude-sonnet-4-6` with a single alternative row for `global.anthropic.claude-sonnet-5`; embeddings `amazon.titan-embed-text-v2:0`.
