from flask import Blueprint

estimation = Blueprint('estimation', __name__)

from . import models, views, forms