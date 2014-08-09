import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()
from users.models import User, Role, Connection

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('project.settings')

    bootstrap.init_app(app)
    db.init_app(app)

    from .estimation import estimation as estimation_blueprint
    app.register_blueprint(estimation_blueprint)

    # Set up Flask-Security and Flask-Social
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)
    app.social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))

    from .users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    # Create a user to test with
    @app.before_first_request
    def create_user():
        db.create_all()
        user_datastore.create_user(email='user@domain.com', password='password')
        try:
            db.session.commit()
        except:
            db.session.rollback()
        from estimation.models import Question
        db.session.add(Question(text='Just a test question', answer=3245))
        try:
            db.session.commit()
        except:
            db.session.rollback()

    return app
