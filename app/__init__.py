from flask import Flask
import os
from .oauth.views import github_blueprint, google_blueprint
app = Flask(__name__)
app.register_blueprint(github_blueprint,url_prefix='/github_login')
app.register_blueprint(google_blueprint,url_prefix='/google_login')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from app import views