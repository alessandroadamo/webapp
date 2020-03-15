import logging
import logging.config

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

logger = logging.getLogger(__name__)

app = Flask(__name__,
            instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('APP_CONFIG_FILE')

# SQLAlchemy
db = SQLAlchemy(app)
db.init_app(app)

# Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Migrate
migrate = Migrate(app, db)
migrate.init_app(app)

from app.views.main import main
from app.views.auth import auth

app.register_blueprint(main)
app.register_blueprint(auth)


from app.models.auth import User


@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

