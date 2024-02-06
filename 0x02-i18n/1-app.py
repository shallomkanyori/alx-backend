#!/usr/bin/env python3
"""Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Babel configurations"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home() -> str:
    """Returns a simple template"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
