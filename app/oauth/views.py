from flask import Blueprint,url_for,session,redirect,request
from authlib.integrations.flask_client import OAuth
from app import app
import os
from dotenv import load_dotenv
load_dotenv()
login_oauth = Blueprint('login_oauth',__name__)
oauth = OAuth(app)


# login fctionality with google
google = oauth.register(
    name='google',
    client_id=os.environ.get('GOOGLE_CLIENT_ID'),
    client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
)

@login_oauth.route('/google/login')
def googlelogin():
    redirect_uri = url_for('login_oauth.googleauthorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@login_oauth.route('/google/authorize')
def googleauthorize():
    token = google.authorize_access_token()
    resp = google.get('userinfo', token=token)
    resp.raise_for_status()
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return token

#login functionality with github

github = oauth.register(
    name='github',
    client_id= os.environ.get('GITHUB_CLIENT_ID'),
    client_secret= os.environ.get('GITHUB_CLIENT_SECRET'),
    access_token_url='https://github.com/login/oauth/access_token',
    access_token_params=None,
    authorize_url='https://github.com/login/oauth/authorize',
    authorize_params=None,
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@login_oauth.route('/github/login')
def githublogin():
    redirect_uri = url_for('login_oauth.githubauthorize', _external=True)
    return github.authorize_redirect(redirect_uri)


@login_oauth.route('/github/authorize')
def githubauthorize():
    token = github.authorize_access_token()
    resp = github.get('user', token=token)
    resp.raise_for_status()
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return token