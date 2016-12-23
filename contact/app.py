from flask import Flask


def make_app():

    app = Flask(__name__)
    # export CONTACT_APP_SETTINGS=/absolute/path/to/test_contact_app/config.py
    app.config.from_envvar('CONTACT_APP_SETTINGS')
    return app
