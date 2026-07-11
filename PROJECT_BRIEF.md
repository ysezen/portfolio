<!-- Last updated: 2026-07-11, up to commit 0bf9c0e -->

# PROJECT_BRIEF.md

## 1. What this product does

Personal portfolio website for yunussezen.com (and yunussezen.com.tr): a single-page
CV/portfolio site rendering one person's profile — introduction, about, skills,
knowledge, languages, work experience, education, certifications, social media links,
and a downloadable resume — plus a contact form that stores the message and emails it
to the site owner. All content is data-driven: the maintainer edits it through the
Django admin, not through code or template changes.

## 2. Tech stack and runtime topology

- **Python 3.12 / Django 5.1**, server-rendered templates (no DRF, no SPA). One
  Django project (`portfolio`) with one app (`core`).
- **PostgreSQL 16** (alpine image) as the only datastore; connection configured via
  `DATABASE_URL` through `django-environ` (`env.db()`).
- **Gunicorn (WSGI)** serves the app — synchronous only; `asgi.py` exists but is
  unused by the compose command.
- **nginx** in front as reverse proxy (`nginx/nginx.conf`, upstream
  `cnt_portfolio:8000`); `client_max_body_size 150M`.
- **Docker Compose** runs three services: `postgres` (host port 5433), `app`
  (gunicorn, host port 8081), `nginx` (host port 8002). The postgres volume is
  external (`portfolio_postgresql-data`). `entrypoint.sh` runs `migrate --noinput`
  on container start; `collectstatic` is commented out there and run manually via
  `make cs`.
- **Static/media storage is DEBUG-switched** (`portfolio/settings.py` +
  `portfolio/custom_storages.py`): with `DEBUG=True` everything is local filesystem;
  with `DEBUG=False` all four storage classes (`StaticStorage`, `MediaStorage`,
  `DocumentStorage`, `ImageSettingStorage`) become `S3Boto3Storage` subclasses
  pointing at prefixes (`static/`, `media/`, `documents/`, `media/`) of one S3
  bucket, served via `<bucket>.s3.amazonaws.com`. The storage *classes themselves*
  are defined conditionally on `settings.DEBUG` at import time, so a given process
  is all-local or all-S3 — models import these classes directly for their
  `FileField`/`ImageField` storages.
- **Email** via SMTP settings from env (`EMAIL_*`, `DEFAULT_FROM_EMAIL`); used only
  by the contact form.
- Configuration comes from `portfolio/.env` (git-ignored; `env.txt` at the root is
  the template). `Makefile` wraps the common compose commands (`build`, `m1`/`m2`
  for migrations, `cs` for collectstatic, `res` for app restart, logs).

## 3. Domain model

All models live in `core/models.py` and extend `AbstractModel`
(`created_date`/`updated_date` timestamps). `Customer` is the hub; content tables
point at it via a `cid` FK with `on_delete=CASCADE` and `default=1` — in practice the
site renders customer id 1 only (hardcoded in the `index` view).

- **Customer** — the site owner's identity: name parts, title, email, phone,
  birthdate, address/city/country, nationality, profile image.
- **Introductions** — one row of long-form section texts per customer (about, skill,
  knowledge, language, experience, education, certification, contact, interest).
  Fetched with `.get(cid_id=...)`, so effectively one-per-customer, though not
  DB-enforced.
- **Knowledge** — a generic skills table with a free-text `type` discriminator
  ("Skill", "Language", anything else = knowledge); `order`, `percentage` (0–100
  validators). The view splits it by type; the separate **Language** model exists
  but is *not* used by the index view (languages come from `Knowledge` with
  `type="Language"`).
- **Experience / Education / Certification** — dated CV entries with descriptions
  and an `icon` CharField (icon name/class); `*_pretty()` helpers format dates as
  `%b %Y` with "Present" fallback.
- **SocialMedia** — ordered links with icon + description.
- **Document** — uploaded files (resume etc.) with `type`, unique-ish `slug`,
  `button_text`; stored via `DocumentStorage`. `type="resume"` is what the index
  view surfaces.
- **GeneralSetting** — name→parameter key-value store for site metadata (title,
  description, keywords, language, etc.), read one key at a time.
- **ImageSetting** — name→image key-value store for site images (defined and
  admin-registered; the index view currently builds no context from it).
- **Message** — contact form submissions (name, email, message), newest first.

Deletes are real deletes (admin-driven, CASCADE from Customer); there is no
soft-delete convention in this codebase.

## 4. API surface

There is no REST/JSON API in the DRF sense; three URL patterns total
(`core/urls.py`, mounted at root, plus `/admin/`):

- `GET /` → `index` view: assembles the whole page context (9 `GeneralSetting`
  lookups by name, customer 1, introduction, knowledge split three ways, experience,
  certifications, educations, social media, resume document) and renders
  `templates/index.html`.
- `POST /submit_contact_form` → validates `ContactFormValidate` (name, email,
  message), persists a `Message`, then sends the email via
  `ContactFormValidate.sends_email()` (an `EmailMessage` to `DEFAULT_FROM_EMAIL`
  with `reply_to` set to the visitor). Returns `JsonResponse` of an
  `OperationResult` dict: `{"status": bool, "http_status": int, "message": str,
  "data": any}` — note the HTTP response itself is always 200; the status code
  lives inside the JSON body. Non-POST requests get the rendered index page back
  rather than JSON.
- `GET /<slug>/` → `redirect_url`: looks up a `Document` by slug (404 if missing)
  and redirects to its file URL — i.e. pretty download links like `/resume/`.
  Because this is a catch-all slug pattern at the root, any new top-level path must
  be registered *above* it or it will be swallowed by the document lookup.

Django admin (`/admin/`) is the entire write/content-management surface; every model
is registered in `core/admin.py` with list_display/search/filter/editable configs.

## 5. Realtime architecture

Not applicable. No WebSockets, no Channels, no polling — a plain request/response
site. (`asgi.py` is the stock Django scaffold and is not wired into deployment.)

## 6. Per-app / per-module summaries

- **`core/`** — the only app.
  - `models.py`: all domain models (see §3).
  - `views.py`: module-level helper functions (`get_general_settings`,
    `get_customer_*`, `prettify_value` for phone formatting,
    `customer_navigate_address`) + the three views. Helpers swallow
    `DoesNotExist` and return `""` so templates render empty rather than 500.
  - `forms.py`: `ContactFormValidate` — validation *and* the email-sending side
    effect (`sends_email`) live on the form.
  - `utils.py`: `OperationResult` — a small status/message/data result object with
    `to_dict()`; the contact endpoint's response envelope.
  - `admin.py`: ModelAdmin registrations for every model.
  - `migrations/`: two migrations (initial schema; `Document.cid`/`type` added).
  - `tests.py`: empty scaffold.
- **`portfolio/`** — project package: `settings.py` (env-driven, DEBUG-switched
  storage/static config, SMTP email), `urls.py` (admin + core include + DEBUG
  static/media serving), `custom_storages.py` (the four DEBUG-conditional storage
  classes), stock `wsgi.py`/`asgi.py`.
- **`templates/`** — `index.html` (the whole page, section by section) extending
  `includes/layout.html`; partials for head, header, messages, scripts, toast.
- **`static/`** — CSS (style, portfolio, responsive, carousel, normalize,
  font-awesome, scroll), Font Awesome + Noto Sans font files, JS/images;
  `staticfiles/` is the collectstatic target (compose volume).
- **`nginx/`** — its own Dockerfile plus two nearly identical configs
  (`nginx.conf` is the one the image uses; `portfolionginx.conf` is a variant
  without the `.com.tr` server names).

## 7. Conventions relevant to architectural discussion

- **Fat helpers in `views.py`, no service/selector layering.** Reads are
  module-level `get_*` functions beside the views; the one write path (contact
  form) does model create + email inline in the view/form. There are no
  `services.py`/`selectors.py` files — new logic conventionally goes next to the
  existing helpers unless a restructuring is explicitly decided.
- **Response envelope for JSON**: `OperationResult.to_dict()` →
  `{"status", "http_status", "message", "data"}`, always returned with HTTP 200;
  clients read `http_status` from the body. Errors are set on the result object,
  not raised.
- **Content-as-data**: anything user-visible that might change (site meta, section
  texts, skills, documents) belongs in a model editable via admin, keyed by
  `GeneralSetting`/`ImageSetting` name strings that templates/views look up
  one-by-one. Adding a new page element usually means a new admin-managed row, not
  a template hardcode.
- **`cid=1` single-tenant assumption.** The schema is multi-customer but every
  view call hardcodes customer id 1; FKs default to 1. Any multi-profile feature
  would need to thread a customer selector through views and templates.
- **DEBUG decides storage at import time.** Because storage classes are defined
  inside `if settings.DEBUG:` branches and bound to model fields, flipping DEBUG
  changes where *all* uploads live; there is no per-environment storage override
  short of editing `custom_storages.py`.
- **Hard deletes** via admin/CASCADE; no `is_active` soft-delete pattern here.
- **English-only codebase** — comments, verbose_names, help_texts, and user-facing
  strings are English (site audience is international).
- **URL ordering constraint**: the root-level `<slug>/` document redirect is a
  catch-all; new top-level routes must be added before it in `core/urls.py`.
- **No test suite, no CI** — `tests.py` is empty; verification is manual via the
  compose stack.
