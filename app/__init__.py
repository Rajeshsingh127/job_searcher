from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand
import os

app = Flask(__name__)
log_in = LoginManager(app)
log_in.login_view = 'login'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app,db)
from app.models import User

from app.oauth.views import login_oauth
from app.login_check import login

#blueprints
app.register_blueprint(login_oauth,url_prefix='/oauth_login')
app.register_blueprint(login,url_prefix='/loginsimple')




from app import views





