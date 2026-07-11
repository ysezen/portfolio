---
description: Generate or incrementally regenerate PROJECT_BRIEF.md
---

Maintain `PROJECT_BRIEF.md` at the repo root — the architectural briefing of this
project. Follow the rules below exactly; they are authoritative for this command.

## Fixed skeleton

`PROJECT_BRIEF.md` always has exactly these 7 sections, in this order. Never drop or
reorder them. If a section does not apply to this project (e.g. no realtime layer),
keep the heading and state briefly that it is not applicable:

1. What this product does
2. Tech stack and runtime topology
3. Domain model
4. API surface
5. Realtime architecture
6. Per-app / per-module summaries
7. Conventions relevant to architectural discussion

## Rules

- **Language: English.** If user-facing strings or code comments in the repo are in
  another language, quote them as-is, but the brief itself is written in English.
- **Section 7 is where project-specific coding conventions live** — layering rules,
  delete strategy, response envelopes, language of comments, and similar.
- **No "known issues / pending work" section.** The maintainer tracks open issues and
  backlog separately, outside this repo. If something genuinely affects how a *future
  architectural decision* should be made (a structural constraint, not a bug or a
  to-do), fold it into whichever numbered section it's architecturally relevant to.
- **Target depth:** once `PROJECT_BRIEF.md` exists, it is the reference for tone,
  density, and length — match it on subsequent regenerations.

## Initial generation

If `PROJECT_BRIEF.md` does not exist yet:

1. Do a full scan of the codebase.
2. Produce the brief following the 7-section skeleton above.
3. Add a last-updated marker as a comment at the top of the file, e.g.:
   `<!-- Last updated: YYYY-MM-DD, up to commit <hash> -->`

## Incremental regeneration

Do not re-scan the entire codebase on every `/brief` call. Instead:

1. Check `PROJECT_BRIEF.md` for its last-updated marker. If the file has no such
   marker yet, add one and do a full scan this one time to establish a baseline.
2. Compare that marker's commit against the repo's current `HEAD`. If there are no
   commits since, report that the brief is already current and stop — do not rewrite
   the file.
3. Otherwise, look only at the commits since that marker — not the whole codebase —
   to determine what changed.
4. Still **verify affected claims against the actual code**, not just commit messages
   or diffs in isolation. Update only the sections those changes affect; leave the
   rest untouched.
5. Update the last-updated marker to the new `HEAD` commit before finishing.

## Out of scope for this command

Do not implement code changes, run tests, or commit as part of this command. This
command only reads the repo and writes/updates `PROJECT_BRIEF.md`.
