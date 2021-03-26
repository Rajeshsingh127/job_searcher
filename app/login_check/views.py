from flask import render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
from app.login_check.forms import Loginform,Signupform
from app.login_check import login


@login.route('/login', methods=['POST'])
def login_process():
    form = Loginform()
    if form.validate_on_submit() and request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember_me =request.form['remember_me']





@login.route('/signup', methods=['POST'])
def signup_process():
    form = Signupform()
    if form.validate_on_submit() and request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
