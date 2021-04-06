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
app.config['MAX_CONTENT_LENGTH'] = 1024*1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg','.png','.jpeg']
app.config['UPLOAD_FOLDER'] = os.path.abspath('app')+'/static/images'
db = SQLAlchemy(app)
migrate = Migrate(app,db)
from app.models import User

from app.oauth.views import login_oauth
from app.login_check import login
from app.upload import upload

#blueprints
app.register_blueprint(login_oauth,url_prefix='/oauth_login')
app.register_blueprint(login,url_prefix='/loginsimple')
app.register_blueprint(upload,url_prefix='/upload')



from app import views





