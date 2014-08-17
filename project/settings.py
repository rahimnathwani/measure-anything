import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'any string which is not guessable'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data.sqlite')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_SUBJECT_PREFIX = '[Measure Anything]'

try:
    from localsettings import SOCIAL_GOOGLE, SOCIAL_FACEBOOK, MAIL_USERNAME, MAIL_PASSWORD
except:
    print 'localsettings.py file not found.  you should put your oauth 2.0 keys in there'

MAIL_SENDER = 'Measure Anything <%s>' % MAIL_USERNAME
