from app import app
from flask import render_template,request,url_for,redirect,session
from app.login_check.forms import Loginform,Signupform
@app.route('/login')
def login():
    form = Loginform()
    return render_template('login.html',form=form)

@app.route('/profile')
def profile():
    return render_template('userprofile.html')

@app.route('/')
def findjobs():
    return render_template('findjobs.html')


@app.route('/signup')
def signup():
    form = Signupform()
    return render_template('signup.html',form=form)