from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField

class Login():
    name = StringField("Name")
    password = PasswordField("password")
    submit = SubmitField("Submit")