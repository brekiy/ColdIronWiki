import os
import flask
import codex

@codex.app.route("/", methods=["GET", "POST"])
def home_page():
  """Display the home page."""
  codex.app.logger.info("Hello from home page")
  context = {}
  username = codex.model.check_login()
  if username is not None:
    context["username"] = username
  codex.app.logger.info(codex.mongo.db.collection_names())
  return flask.render_template("home.html", **context)