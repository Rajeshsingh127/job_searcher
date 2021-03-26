from flask import Flask
import os

app = Flask(__name__)

from app import views
from app.oauth.views import login_oauth
from app.login import login

app.register_blueprint(login_oauth,url_prefix='/oauth_login')
app.register_blueprint(login,url_prefix = '/loginsimple')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
