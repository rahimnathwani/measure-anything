import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'any string which is not guessable'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

try:
    from localsettings import *
except:
    print 'localsettings.py file not found.  you should put your oauth 2.0 keys in there'
