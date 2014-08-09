from flask import Blueprint
from flask.ext.security import Security, SQLAlchemyUserDatastore

users = Blueprint('users', __name__, template_folder='templates')

from . import models, views, forms
