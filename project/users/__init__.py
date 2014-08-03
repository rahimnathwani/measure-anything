import sys

from flask import Flask, g, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import login

# App
users = Blueprint('users', __name__, template_folder='templates')

# DB
from .. import db

from . import models, views, forms
from .models import User

sys.path.append('../..')

from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.template_filters import backends


login_manager = login.LoginManager()
login_manager.login_view = 'main'
login_manager.login_message = ''

@users.record_once
def on_load(state):
    login_manager.init_app(state.app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.user.User.query.get(int(userid))
    except (TypeError, ValueError):
        pass

