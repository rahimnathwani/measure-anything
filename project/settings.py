import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'any string which is not guessable'
SQLALCHEMY_DATABASE_URI = 'postgresql://measure:measure@localhost/measure'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SECURITY_POST_LOGIN = '/profile'

try:
    from localsettings import *
except:
    print 'localsettings.py file not found.  you should put your oauth 2.0 keys in there'
