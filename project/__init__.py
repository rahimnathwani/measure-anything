import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security import Security, SQLAlchemyUserDatastore

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()
from users.models import User, Role

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('project.settings')

    bootstrap.init_app(app)
    db.init_app(app)

    from .estimation import estimation as estimation_blueprint
    app.register_blueprint(estimation_blueprint)

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    # Set up Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)

    # Create a user to test with
    @app.before_first_request
    def create_user():
        db.create_all()
        user_datastore.create_user(email='user@domain.com', password='password')
        db.session.commit()

    return app
