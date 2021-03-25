from app import app
from flask import render_template,request,url_for,redirect,session

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('userprofile.html')

@app.route('/')
def findjobs():
    return render_template('findjobs.html')
