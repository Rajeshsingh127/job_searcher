from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,EqualTo
from wtforms.fields.html5 import EmailField


class Loginform(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Signin')



class Signupform(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_check = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',message='password must be equal')])
    submit = SubmitField('Signup')
