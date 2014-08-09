from flask import render_template, request, current_app, session, flash, redirect, url_for
from flask.ext.security import login_required, current_user, login_user, LoginForm
from flask.ext.social.utils import get_provider_or_404
from flask.ext.social.views import connect_handler
from . import users
from .models import User, Role
from .forms import RegisterForm

@users.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        content='Profile Page',
        facebook_conn=current_app.social.facebook.get_connection())

@users.route('/register', methods=['GET', 'POST'])
@users.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    form = RegisterForm()

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    print "just before form.validate_on_submit"

    if form.validate_on_submit():
        ds = current_app.security.datastore
        user = ds.create_user(email=form.email.data, password=form.password.data)
        ds.commit()

        # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
        connection_values = session.pop('failed_login_connection', None)

        print connection_values

        if connection_values:
            connection_values['user_id'] = user.id
            connect_handler(connection_values, provider)

        print user

        if login_user(user):
            ds.commit()
            flash('Account created successfully', 'info')
            return redirect(url_for('users.profile'))

        return render_template('thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('register.html',
                           form=form,
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)
