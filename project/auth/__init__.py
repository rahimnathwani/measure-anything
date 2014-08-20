from flask import Blueprint, session
from .. import oauth

class RegisteringExampleBlueprint(Blueprint):
    def register(self, app, options, first_registration=False):
        self.google = oauth.remote_app(
            'google',
            consumer_key=app.config.get('SOCIAL_GOOGLE')['consumer_key'],
            consumer_secret=app.config.get('SOCIAL_GOOGLE')['consumer_secret'],
            request_token_params={
                'scope': 'https://www.googleapis.com/auth/plus.profile.emails.read https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/plus.me'
            },
            base_url='https://www.googleapis.com/oauth2/v1/',
            request_token_url=None,
            access_token_method='POST',
            access_token_url='https://accounts.google.com/o/oauth2/token',
            authorize_url='https://accounts.google.com/o/oauth2/auth',
        )
        @self.google.tokengetter
        def get_google_oauth_token():
            return session.get('google_token')

        super(RegisteringExampleBlueprint,
              self).register(app, options, first_registration)

auth = RegisteringExampleBlueprint('auth', __name__)

from . import views, models, forms
