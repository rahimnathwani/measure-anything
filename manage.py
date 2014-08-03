import os
from flask import Flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from project import create_app, db

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
