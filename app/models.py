from flask_sqlalchemy import SQLAlchemy
from app import app
from flask_login import UserMixin, LoginManager

db = SQLAlchemy(app)
login_manager = LoginManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),unique=True, nullable=False)
    email = db.Column(db.String(40),nullable=False)
    password = db.Column(db.String(40), nullable=False)