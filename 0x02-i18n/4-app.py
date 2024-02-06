#!/usr/bin/env python3
"""Basic Flask app with Babel.
Force locale with URL parameter.
"""
from flask import Flask, render_template, request
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
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
