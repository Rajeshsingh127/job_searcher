from app import app
from flask import render_template,request,url_for,redirect,session
from flask_login import login_required,current_user
from app.login_check.forms import Loginform,Signupform
from app.upload.forms import Uploadfeed



@app.route('/login')
def login():
    form = Loginform()
    return render_template('login.html',form=form)


@app.route('/profile')
@login_required
def profile():
    name = current_user.name
    return render_template('userprofile.html',name=name)

""""@app.route('/')
def findjobs():
    return render_template('findjobs.html')
"""

@app.route('/signup')
def signup():
    form = Signupform()
    return render_template('signup.html',form=form)


@app.route('/uploadata')
@login_required
def upload():
    form = Uploadfeed()
    return render_template('upload.html',form=form)
