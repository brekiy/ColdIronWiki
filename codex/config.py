"""Codex configuration."""

import os

APPLICATION_ROOT = "/"

# Security
SECRET_KEY = os.environ.get("SECRET-KEY") or "placeholder"
SESSION_COOKIE_NAME = "codex-login"

# File directories

ALLOWED_IMG_EXTENSIONS = set(["png", "jpg", "jpeg"])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024