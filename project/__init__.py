import os
from flask import Flask, g
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import login
from flask.ext.migrate import Migrate, MigrateCommand
from social.apps.flask_app.models import init_social
from social.apps.flask_app.routes import social_auth
from social.apps.flask_app.template_filters import backends

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()

app = Flask(__name__)

app.config.from_object('project.settings')
    
bootstrap.init_app(app)
db.init_app(app)

from .estimation import estimation as estimation_blueprint
app.register_blueprint(estimation_blueprint)

app.register_blueprint(social_auth)
init_social(app, db)

from .users import users as users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

@app.before_request
def global_user():
    g.user = login.current_user

@app.teardown_appcontext
def commit_on_success(error=None):
    if error is None:
        db.session.commit()

@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()

@app.context_processor
def inject_user():
    try:
        return {'user': g.user}
    except AttributeError:
        return {'user': None}

app.context_processor(backends)