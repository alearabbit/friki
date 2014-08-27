from flask import Flask
from flask_oauth import OAuth
import settings


app = Flask(__name__)
app.config.from_object('app.settings.Production')


oauth =OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=settings.Production.FACEBOOK_APP_ID,
    consumer_secret=settings.Production.FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
    )


import views


