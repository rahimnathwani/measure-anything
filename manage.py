import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import app, db

basedir = os.path.abspath(os.path.dirname(__file__))

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

'''
@manager.command
def syncdb():
    from flask_example.models import user
    from social.apps.flask_app import models
    db.drop_all()
    db.create_all()
'''

if __name__ == '__main__':
	manager.run()
