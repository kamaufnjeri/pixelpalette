from flask_wtf import FlaskForm
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, SelectField
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import SubmitField
from app.models import User
 
class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
 
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email adress')
 
    username = StringField(label='User name:', validators=[Length(min=4, max=30), DataRequired()])
    first_name = StringField(label='First name:', validators=[Length(min=4, max=20), DataRequired()])
    last_name = StringField(label='Last name:',  validators=[Length(min=4, max=20), DataRequired()])
    email_address = StringField(label='Email address:', validators=[Email()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    category = SelectField(label='Category:', choices=[('artist', 'Artist'), ('enthusiast', 'Art Enthusiast')], validators=[DataRequired()])
    submit = SubmitField(label='Create account')
 
 
class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

