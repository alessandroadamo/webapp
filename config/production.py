import os

basedir = os.path.abspath(os.path.dirname(__file__))

HOST = "127.0.0.1"
PORT = 8080

DEBUG = False

# This is a secret key that is used by Flask to sign cookies.
SECRET_KEY = "J@NcRfUjXn2r5u8x/A?D(G+KaPdSgVkYp3s6v9y$B&E)H@McQeThWmZq4t7w!z%C"

# used by Flask-Bcrypt to hash user passwords
BCRYPT_LOG_ROUNDS = 12

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, '../app/data/app.db')
SQLALCHEMY_ECHO = False
