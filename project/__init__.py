import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.mail import Mail

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object('project.settings')

    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    from .estimation import estimation as estimation_blueprint
    app.register_blueprint(estimation_blueprint)

    return app
