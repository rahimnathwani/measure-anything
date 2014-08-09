import os
from flask import Flask, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.social import Social, login_failed
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask.ext.social.utils import get_connection_values_from_oauth_response

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

    # Create a user to test with, and a sample question
    @app.before_first_request
    def create_user():
        db.create_all()
        user_datastore.create_user(email='user@domain.com', password='password')
        try:
            db.session.commit()
        except Exception, e:
            db.session.rollback()
        from estimation.models import Question
        db.session.add(Question(text='Just a test question', answer=3245))
        try:
            db.session.commit()
        except Exception, e:
            db.session.rollback()

    class SocialLoginError(Exception):
        def __init__(self, provider):
            self.provider = provider

    @login_failed.connect_via(app)
    def on_login_failed(sender, provider, oauth_response):
        app.logger.debug('Social Login Failed via %s; '
                         '&oauth_response=%s' % (provider.name, oauth_response))

        # Save the oauth response in the session so we can make the connection
        # later after the user possibly registers
        session['failed_login_connection'] = \
            get_connection_values_from_oauth_response(provider, oauth_response)

        raise SocialLoginError(provider)


    @app.errorhandler(SocialLoginError)
    def social_login_error(error):
        return redirect(url_for('users.register', provider_id=error.provider.id, login_failed=1))    

    return app
