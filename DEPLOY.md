# Deploying to PythonAnywhere

PythonAnywhere's free tier gives this app genuine persistent storage (your SQLite database
survives restarts, unlike Render/Fly.io free tiers) and a permanent public URL like
`https://yourusername.pythonanywhere.com`.

## One-time setup

1. **Sign up free** at pythonanywhere.com if you haven't already.
2. **Open a Bash console** (Dashboard -> "Consoles" -> "Bash").
3. **Clone the repo:**
   ```
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```
4. **Create a virtualenv and install dependencies:**
   ```
   mkvirtualenv --python=/usr/bin/python3.10 helpdesk-env
   pip install -r requirements.txt
   ```
5. **Create `config.py`** (it's gitignored, so it won't come from the clone) -- either
   `cp config.py.example config.py` then edit it with the `nano`/`vim`/PythonAnywhere file
   editor, or paste in the same values you're using locally.
6. **Create the web app:** Dashboard -> "Web" -> "Add a new web app" -> choose
   **"Manual configuration"** (NOT the Flask template) -> pick the same Python version as
   your virtualenv.
7. **Point it at your code**, on the Web tab:
   - **Source code**: `/home/<yourusername>/<your-repo>`
   - **Working directory**: same path
   - **Virtualenv**: `/home/<yourusername>/.virtualenvs/helpdesk-env`
   - **Static files** -- the repo now serves TWO apps (the freelance site at `/`, the
     tracker at `/tracker`), so add both mappings:
     - URL `/static/` -> Directory `/home/<yourusername>/<your-repo>/freelance_site/static`
     - URL `/tracker/static/` -> Directory `/home/<yourusername>/<your-repo>/static`
8. **Edit the WSGI configuration file** (linked from the Web tab). Replace its contents with:
   ```python
   import sys
   path = '/home/<yourusername>/<your-repo>'
   if path not in sys.path:
       sys.path.insert(0, path)

   from combined_wsgi import application
   ```
   `combined_wsgi.py` handles `init_db()` and mounts both Flask apps itself -- see that file
   for details.
9. Click the big green **Reload** button on the Web tab. Visit your `.pythonanywhere.com`
   URL -- you should land on the new freelance site homepage; `/tracker` still serves the
   Help Desk Ticket Tracker login/submit-a-ticket page.

## Making future updates

This is the part that matters for ongoing development:

1. Make changes locally, same as always. Run `pytest` to confirm nothing broke.
2. `git add`, `git commit`, `git push` to GitHub.
3. On PythonAnywhere, open a Bash console:
   ```
   cd <your-repo>
   git pull
   pip install -r requirements.txt   # only needed if you added a new dependency
   ```
4. Go to the **Web** tab and click **Reload**.

That's the whole update loop -- no redeploy pipeline needed for a project this size.

## Notes

- The free tier has daily CPU-second limits (plenty for a personal tool with light traffic)
  and no "always-on tasks" (not needed here -- the web app itself is always reachable,
  that's a different feature for background scripts/bots).
- Keep `config.py` off GitHub. If you ever suspect it leaked, regenerate `SECRET_KEY` and
  `API_KEY`, and re-hash a new `ADMIN_PASSWORD_HASH`, then update `config.py` on the server.
