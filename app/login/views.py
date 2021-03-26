from flask import render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from app.login.forms import Loginform,Signupform
from app.login import login


@login.route('/login')
def login():
    form = Loginform()
    return render_template('login.html',form=form,title='login')