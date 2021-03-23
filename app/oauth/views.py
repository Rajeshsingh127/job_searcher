from flask import Blueprint,url_for,session,redirect
from flask_dance.contrib.github import github, make_github_blueprint
from flask_dance.contrib.google import google, make_google_blueprint
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
github_blueprint = make_github_blueprint(client_id=os.environ.get('GITHUB_CLIENT_ID'),client_secret=os.environ.get('GITHUB_CLIENT_SECRET'))
google_blueprint = make_google_blueprint(client_id=os.environ.get('GOOGLE_CLIENT_ID'),client_secret=os.environ.get('GOOGLE_CLIENT_SECRET'),
                                         scope=['email', 'profile']
                                         )

@github_blueprint.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    account_info = github.get('/user')
    if account_info.ok:
        account_info_json = account_info.json()
        return '<h1>your github name is {}'.format(account_info_json['login'])
    return 'request failed'

@google_blueprint.route('/')
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/oauth2/v2/userinfo")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["email"])