"""Combines the freelance site (mounted at /) and the Help Desk Tracker (mounted at /tracker)
into one WSGI app. Used as the PythonAnywhere WSGI entry point -- see DEPLOY.md."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from werkzeug.middleware.dispatcher import DispatcherMiddleware

from database import init_db
init_db()

from app import app as tracker_app
from freelance_site.app import app as site_app

application = DispatcherMiddleware(site_app, {
    "/tracker": tracker_app,
})

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application, use_reloader=True)
