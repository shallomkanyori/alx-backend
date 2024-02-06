# i18n

## Tasks

### Task 0
Files: [0-app.py](0-app.py), [templates/0-index.html](templates/0-index.html)

First you will setup a basic Flask app in `0-app.py`. Create a single` /` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

### Task 1
Files: [1-app.py](1-app.py), [templates/1-index.html](templates/1-index.html)

Install the Babel Flask extension:
```
$ pip3 install flask_babel==2.0.0
```
Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.
Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).
Use that class as config for your Flask app.

### Task 2
Files: [2-app.py](2-app.py), [templates/2-index.html](templates/2-index.html)

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

### Task 3
Files: [3-app.py](3-app.py), [templates/3-index.html](templates/3-index.html)

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing
```
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with
```
$ pybabel extract -F babel.cfg -o messages.pot .
```
and your two dictionaries with
```
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:
| msgid         | English                  | French                       |
| ------------- | ------------------------ | ---------------------------- |
| `home_title`  | `"Welcome to Holberton"` | `"Bienvenue chez Holberton"` |
| `home_header` | `"Hello world!"`         | `"Bonjour monde!"`           |

Then compile your dictionaries with
```
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.
