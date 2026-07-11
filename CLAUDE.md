# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Your role in this repository

You have two responsibilities:

1. **Maintain `PROJECT_BRIEF.md`** — the architectural briefing of the project
   (`/brief` command, see below).
2. **Implement tasks given directly in chat.** The maintainer discusses architectural
   decisions elsewhere (Claude chat, against the brief) and then gives you the
   resulting task directly, in this session. There is no intermediate task document.

For implementation tasks, always work in two phases:

1. **Plan.** Before writing or editing any code, produce a short plain-language plan:
   what will change, in which files, in what order, and — briefly — what could
   regress or needs a decision (migration, new dependency, storage/S3 or URL-routing
   impact). No code in this phase. Wait for explicit approval ("onaylıyorum",
   "devam et", etc.) before proceeding.
2. **Implement.** Once approved, make the code changes directly in the working tree.

**You never commit.** Leave all changes unstaged/uncommitted. The maintainer reviews
the diff and commits themselves. Do not run `git commit`, `git push`, or open a PR
under any circumstance, even if asked to "finish the job" — implementing the change is
the job; committing it is not yours to do.

**You do not run the test suite or deploy.** The maintainer verifies and tests
separately, outside this session. If your plan identifies a real regression risk, say
so in the plan — but don't attempt to run `manage.py test`, spin up the compose stack,
or otherwise validate the change yourself unless explicitly asked to.

**Migrations and new dependencies are still decisions, not steps.** If a task implies
either, flag it in the plan phase and get explicit confirmation before proceeding —
don't silently `makemigrations` or add a package.

## PROJECT_BRIEF.md

- **Language: English.** (The codebase itself — comments, verbose_names, help_texts,
  user-facing strings — is also English.)
- **Fixed 7-section skeleton** — never drop or reorder sections:
  1. What this product does
  2. Tech stack and runtime topology
  3. Domain model
  4. API surface
  5. Realtime architecture
  6. Per-app summaries
  7. Conventions relevant to architectural discussion
- **No "known issues / pending work" section.** The maintainer tracks open issues and
  backlog separately (outside this repo); don't maintain a living list of them here.
  If something genuinely affects how a *future architectural decision* should be made
  (e.g. a structural constraint, not a bug or a to-do), it belongs in whichever
  numbered section it's architecturally relevant to.
- Target depth: the current `PROJECT_BRIEF.md` in the repo is the reference for tone,
  density, and length. Match it.
- Regeneration is on demand (`/brief`), not automatic.

### Incremental regeneration

Do not re-scan the entire codebase on every `/brief` call. Instead:

1. Check `PROJECT_BRIEF.md` for its last-updated marker (a comment at the top of the
   file, e.g. `<!-- Last updated: 2026-07-07, up to commit a1b2c3d -->`). If the file
   has no such marker yet, add one and do a full scan this one time to establish a
   baseline.
2. Compare that marker's commit against the repo's current `HEAD`. If there are no
   commits since, report that the brief is already current and stop.
3. Otherwise, look only at the commits since that marker — not the whole codebase — to
   determine what changed.
4. Still **verify affected claims against the actual code**, not just commit messages
   or diffs in isolation. Update only the sections those changes affect; leave the
   rest untouched.
5. Update the last-updated marker to the new `HEAD` commit before finishing.

## Conventions to respect when implementing

- **Single app, flat layout.** All logic lives in `core/`: reads are module-level
  `get_*` helper functions in `core/views.py` next to the views; the contact-form
  write path does model create + email inline. There is no service/selector layering
  — new logic goes beside the existing helpers unless a restructuring is explicitly
  decided in chat first.
- **JSON response envelope**: `core/utils.py:OperationResult.to_dict()` →
  `{"status": bool, "http_status": int, "message": str, "data": any}`, always
  returned with HTTP 200 — clients read `http_status` from the body. Errors are set
  on the result object (`set_error`), not raised. Match this for any new JSON
  endpoint.
- **Content-as-data.** Anything user-visible that might change belongs in an
  admin-managed model, not hardcoded in templates: site metadata in
  `GeneralSetting` (name→parameter lookups), images in `ImageSetting`, section
  texts in `Introductions`, files in `Document`. Register new models in
  `core/admin.py`.
- **`cid=1` single-tenant assumption.** The schema is multi-customer but every view
  hardcodes customer id 1 and FKs default to 1. Don't build multi-profile behavior
  as a side effect of another change — that's an explicit architectural decision.
- **DEBUG-switched storage.** Storage classes in `portfolio/custom_storages.py` are
  defined conditionally on `settings.DEBUG` at import time (local filesystem vs S3)
  and bound directly to model fields. Any change touching uploads or static/media
  config must consider both branches.
- **URL ordering constraint**: `core/urls.py` ends with a catch-all `<slug>/`
  document-redirect pattern. New top-level routes must be registered above it.
- **Hard deletes** (admin-driven, CASCADE from `Customer`) are the norm here — there
  is no soft-delete convention.
- **English-only codebase.** Comments, verbose_names, help_texts, and user-facing
  strings are English; keep new code consistent with that.

## Communication language

Respond to the user in Turkish in all conversation turns for this repository,
regardless of the language of their message. `PROJECT_BRIEF.md` is written in English
per the rule above.

## Project context (read-only reference)

Django 5.1 personal portfolio site (`portfolio` project, single `core` app) for
yunussezen.com — server-rendered templates, no DRF/SPA, no realtime. Python 3.12,
Gunicorn (WSGI) behind nginx, PostgreSQL 16. Static/media served locally when
`DEBUG=True`, from AWS S3 (django-storages) when `DEBUG=False`. Content is managed
entirely through the Django admin; the public surface is the index page, a contact
form (stores a `Message` and emails the owner via SMTP), and slug-based document
redirects. Everything runs via Docker Compose (`make build`, ports: app 8081,
nginx 8002, postgres 5433); configuration comes from `portfolio/.env` (template:
`env.txt`).

**`PROJECT_BRIEF.md` at the repo root is the authoritative architecture reference.**
Read it at the start of any task; do not duplicate its content here.
