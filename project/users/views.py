from flask import render_template, request, current_app
from flask.ext.security import login_required
from . import users
from .models import User, Role

@users.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        facebook_conn=current_app.social.facebook.get_connection())


@users.route('/login2')
def login():
    return render_template(
        'login.html',
        content='Login Page')
