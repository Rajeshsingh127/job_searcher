from flask import Flask
import os

app = Flask(__name__)

from app import views
from app.oauth.views import login_oauth

app.register_blueprint(login_oauth,url_prefix='/oauth_login')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')