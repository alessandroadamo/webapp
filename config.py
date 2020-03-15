import os

basedir = os.path.abspath(os.path.dirname(__file__))

HOST = "0.0.0.0"
PORT = 8080

DEBUG = True

# This is a secret key that is used by Flask to sign cookies.
SECRET_KEY = "my-long-secret-key"

# used by Flask-Bcrypt to hash user passwords
BCRYPT_LOG_ROUNDS = 12

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, './app/data/app.db')
SQLALCHEMY_ECHO = False
