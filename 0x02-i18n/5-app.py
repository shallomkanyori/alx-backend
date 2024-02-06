#!/usr/bin/env python3
"""Basic Flask app with Babel.
Mock logging in.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union


class Config():
    """Babel configurations"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[object, None]:
    """Returns the user associated with id or None if not found"""

    req_id = request.args.get("login_as")

    if req_id:
        try:
            user_id = int(req_id)
        except ValueError:
            return None

        return users.get(user_id, None)

    return None


@app.before_request
def before_request():
    """Try to login in as a user."""
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale() -> Union[str, None]:
    """Gets the locale from the request"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """Returns a simple template"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
