import flask
from flask_pymongo import PyMongo

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (codex/config.py)
app.config.from_object('codex.config')
mongo = PyMongo(app)

import codex.model # noqa: E402  pylint: disable=wrong-import-position
import codex.views # noqa: E402  pylint: disable=wrong-import-position
