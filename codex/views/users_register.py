"""Routes for registering accounts."""
import uuid
import hashlib
import flask
import codex


@codex.app.route('/users/register/', methods=['GET', 'POST'])
def register():
    """create."""
    context = {}
    username = codex.model.check_login()
    if username is None:
        return flask.redirect(flask.url_for('home_page'))
    if flask.request.method == 'POST':
        data = flask.request.get_json()
        # codex.app.mongo.db.users
        return flask.redirect(flask.url_for('home_page'))
    return flask.render_template("users_register.html", **context)


def hash_pass(password):
    """hash_pass."""
    algorithm = "sha512"
    salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    return "$".join([algorithm, salt, password_hash])
