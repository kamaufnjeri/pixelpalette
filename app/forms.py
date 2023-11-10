from flask_wtf import FlaskForm
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, IntegerField, DateTimeField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from app.models import User


"""form for user registration"""
class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        """check if username exists and raise error"""
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        """check if username exists and raise an error"""
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists! Please try a different email adress')

    username = StringField(label='User name:', validators=[Length(min=6, max=30), DataRequired()])
    first_name = StringField(label='First name:', validators=[Length(min=3, max=20), DataRequired()])
    last_name = StringField(label='Last name:',  validators=[Length(min=3, max=20), DataRequired()])
    email_address = StringField(label='Email address:', validators=[Email()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[
        EqualTo('password1', message="The two passwords must be a match"),
        DataRequired()
        ]
    )
    category = SelectField(label='Category:', choices=[('artist', 'Artist'), ('art_enthusiast', 'Art Enthusiast')], validators=[DataRequired()])
    submit = SubmitField(label='Create account')


"""form to login"""
class LoginForm(FlaskForm):
    username = StringField(label='User name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Login')


"""artwork upload form"""
class ArtworkForm(FlaskForm):
    title = StringField(label='Title:', validators=[DataRequired()])
    description = TextAreaField(label='Description:', validators=[DataRequired()])
    price = StringField(label='Price:', validators=[DataRequired()])
    category = SelectField(
        label='Category:',
        choices=[
            ('painting', 'Painting'),
            ('sculpture', 'Sculpture'),
            ('photography', 'Photography'),
            ('others', 'Others')
        ],
            validators=[DataRequired()]
    )
    type = SelectField(
        label='Type of Artwork:',
        choices=[
            ('general_artwork', 'General Artwork'),
            ('exhibit_artwork', 'Exhibit Artwork')
        ],
            validators=[DataRequired()]
    )
    image = FileField('Choose image:', validators=[
            FileRequired(),
            FileAllowed('Images only! (JPEG, JPG, PNG)', ['jpg', 'png', 'jpeg'])
        ]
    )
    submit = SubmitField(label='Upload')


"""updating use info form"""
class ProfileForm(FlaskForm):
    username = StringField(label='User name:', validators=[Length(min=4, max=30), DataRequired()])
    first_name = StringField(label='First name:', validators=[Length(min=4, max=20), DataRequired()])
    last_name = StringField(label='Last name:',  validators=[Length(min=4, max=20), DataRequired()])
    email_address = StringField(label='Email address:', validators=[Email()])
    password1 = PasswordField(label='Password:')
    category = SelectField(label='Category:', choices=[('artist', 'Artist'), ('art_enthusiast', 'Art Enthusiast')], validators=[DataRequired()])
    submit = SubmitField(label='Save Changes')


"""updating artwork info form"""
class EditForm(FlaskForm):
    title = StringField(label='Title:', validators=[DataRequired()])
    description = TextAreaField(label='Description:', validators=[DataRequired()])
    price = StringField(label='Price:', validators=[DataRequired()])
    category = SelectField(
        label='Category:',
        choices=[
            ('painting', 'Painting'),
            ('sculpture', 'Sculpture'),
            ('photography', 'Photography'),
            ('others', 'Others')
        ],
            validators=[DataRequired()]
    )
    type = SelectField(
        label='Type:',
        choices=[
            ('general_artwork', 'General Artwork'),
            ('exhibit_artwork', 'Exhibit Artwork'),
        ],
            validators=[DataRequired()]
    )
    submit = SubmitField(label='Save Changes')
