import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

#    app.config.from_object(config[config_name])
#    config[config_name].init_app(app)
    app.config['SECRET_KEY'] = 'any string which is not guessable'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    bootstrap.init_app(app)
    db.init_app(app)

    from .estimation import estimation as estimation_blueprint
    app.register_blueprint(estimation_blueprint)

    return app
