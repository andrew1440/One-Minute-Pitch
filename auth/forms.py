from flask_wtf import FlaskForm
from wtfforms import stringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import user


class RegistrationForm(FlaskForm):
    email = stringField('Enter  Email Address',validators=[Required(),Email])
    username = stringField('Enter   username',validators= [Required])
    password = PasswordField('Pasword',validators = [Required(), EqualTo('password_confirm',message = 'password must match')] )
    password_confirm = PasswordField('Confirm Password', validators = [Required])

    class LoginForm(FlaskForm):
        email = stringField('Email Address',validators=[Required(),Email()])
        password = PasswordField('Password',validators =[Required()])
        remember = BooleanField('Remember me')
        submit = SubmitField('Sign In')