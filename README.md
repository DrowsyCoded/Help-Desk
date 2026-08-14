# Jonathon Hunt — Web Design & Content

The source for [jonhunt.pythonanywhere.com](https://jonhunt.pythonanywhere.com), a Flask business site for freelance web design and content writing services (websites, ATS resumes, SEO blog writing, cover letters).

This repo also hosts the **Help Desk Ticket Tracker**, a separate Flask app served at `/tracker` as a portfolio piece — see the [Help Desk Ticket Tracker](#help-desk-ticket-tracker) section below for details on that project specifically.

## What's on the site

- **Home / About / Services** — service lineup (Web Design, ATS Resume + LinkedIn, SEO Blog & Article Writing, Cover Letters), pricing, and FAQ
- **Portfolio** — real project work: this repo's own Help Desk Ticket Tracker, a desktop AI transcription app, and client website mockups/redesigns
- **Blog** — SEO-focused articles on web design pricing, ATS resumes, local SEO, and content writing, written and published directly through the app
- **Contact** — a contact form for new inquiries

## Tech stack

Flask, Jinja2 templates, hand-written HTML/CSS (no frontend framework), deployed on PythonAnywhere.

## Project structure

```
app.py                  - Help Desk Ticket Tracker app (routes, logic)
database.py             - Tracker's SQLite schema and connection helper
charts.py                - Tracker's SVG chart generation
combined_wsgi.py         - Mounts both apps together for deployment (freelance site at /, tracker at /tracker)
templates/, static/       - Tracker's templates and static assets
tests/                    - Tracker's pytest suite

freelance_site/
  app.py                 - Business site app (routes, services/portfolio/blog content, contact form)
  templates/              - Business site templates
  static/                 - Business site CSS, images
```

## Running locally

```
pip install -r requirements.txt
python combined_wsgi.py   # or run freelance_site/app.py directly for just the business site
```

The business site runs at `/`, and the Help Desk Ticket Tracker at `/tracker`.

## Deployment

See [DEPLOY.md](DEPLOY.md) for the full PythonAnywhere setup and update workflow. Live at [jonhunt.pythonanywhere.com](https://jonhunt.pythonanywhere.com).

## Help Desk Ticket Tracker

The tracker itself is a full-stack ticket management system (ticket CRUD, dashboards with hand-rolled SVG charts, CSV export, a JSON REST API, private per-ticket messaging links, and a Windows Quick Assist remote-support workflow), built first as a standalone portfolio project and later folded into this same repo/deployment. Live demo: [jonhunt.pythonanywhere.com/tracker](https://jonhunt.pythonanywhere.com/tracker).
