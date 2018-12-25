from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, DateField, SelectField, SubmitField, validators, PasswordField
from flask_uploads import UploadSet, IMAGES
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=5, message='Name must be at least 5 characters long')])
    password = PasswordField("Password", [validators.Length(min=6, message="Password must be at least 6 characters long")])
    login = SubmitField("Login")
    pass


class RegistrationForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=6, message="Name must be at least 6 characters long")])
    username = StringField("Username", [validators.Length(min=5, message="Username must be at least 5 characters long")])
    email = StringField("Email", validators=[Email(message='Invalid email format')])
    password = PasswordField("Password", [validators.Length(min=6, message='Password must be at least 6 characters long')])
    confirmPass = PasswordField("Confirm password", [validators.EqualTo('password', message="Password must match")])
    register = SubmitField("Register")
    pass


class UploadForm(FlaskForm):
    images = UploadSet('images', IMAGES)
    photo = FileField("Choose file", validators=[
        FileRequired(),
        FileAllowed(images, message="Images only")
    ])
    name = StringField("Photo name")
    type = StringField("Photo type")
    date = DateField('Date')
    height = StringField('Height')
    width = StringField('Width')
    size = StringField('Size')
    corporation = StringField('Device maker')
    model = StringField('Device model')
    exposureTime = StringField('Exposure time')
    exposureProgram = StringField('Exposure program')
    focal = StringField('Focal length')
    flash = StringField('Flash mode')
    event = StringField('Event name')
    location = StringField('Location')
    album = SelectField('Album', choices=[('0', '-----'), ('1', 'Birthday'), ('2', 'Eid')])
    weather = StringField('Weather')
    group = SelectField('Group', choices=[('0', '----'), ('1', 'Friends'), ('2', 'Family')])
    people = StringField('People')
    tag = StringField('Tag')
    upload = SubmitField('Upload')


class AlbumForm(UploadForm):
    upload = SubmitField('Update')


class SearchForm(AlbumForm):
    searchTime = SelectField('Timestamp', choices=[('0', '----'), ('1', 'Morning'), ('2', 'Noon')])
    searchEvent = StringField('Event')
    searchLocation = StringField('Location')
    searchWeather = SelectField('Weather', choices=[('0', '----'), ('1', 'Rainy'), ('2', 'Cloudy')])
    searchGroup = SelectField('Group', choices=[('0', '----'), ('1', 'Friend'), ('2', 'Family')])
    searchAlbum = SelectField('Album', choices=[('0', '----'), ('1', 'Birthday'), ('2', 'Eid')])
    searchDate = DateField('Date')
    searchTag = StringField('Tag')

