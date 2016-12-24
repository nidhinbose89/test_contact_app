"""Configuration parameters for the app."""

# export CONTACT_APP_SETTINGS=/absolute/path/to/test_contact_app/config.py
DEBUG = False
TESTING = False
SECRET_KEY = 'some-key-for-contact-application'
SQLALCHEMY_DATABASE_URI = 'mysql://root:123@localhost:3306/contact_app?charset=utf8'
