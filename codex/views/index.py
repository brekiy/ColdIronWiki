import os
import flask
import codex

@codex.app.route("/", methods=["GET", "POST"])
def show_index():
  """Display the index page."""
  codex.app.logger.debug("HELLO")
  context = {}
  return flask.render_template("index.html", **context)