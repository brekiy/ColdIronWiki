"""Codex helper methods."""
import tempfile
import shutil
import hashlib
import flask
import codex

# Session info

def check_login():
    """Check if a user is currently logged in."""
    if "username" in flask.session:
        return flask.session["username"]
    return None

# Database methods
