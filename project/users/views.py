from social.apps.flask_app import routes
from flask import render_template, redirect
from flask.ext.login import login_required, logout_user
from . import users

@users.route('/')
def main():
    return render_template('home.html')


@login_required
@users.route('/done/')
def done():
    return render_template('done.html')


@users.route('/logout')
def logout():
    """Logout view"""
    logout_user()
    return redirect('/')