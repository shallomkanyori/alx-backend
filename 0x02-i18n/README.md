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
