from flask_login import UserMixin
from app import db,log_in

class User(UserMixin,db.Model):
    __tablename__ = "Userinfo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40),unique=True,nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password


@log_in.user_loader
def load_user(id):
    return User.query.get(int(id))