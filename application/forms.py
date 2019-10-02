from flask_wtf import FlaskForm
from application import db
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from application.models import Users, Gamecharacters
from flask_login import current_user, LoginManager
from wtforms_sqlalchemy.fields import QuerySelectField

class RegistrationForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	confirm_password = PasswordField('Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		])
	submit = SubmitField('Sign Up')

	def validate_email(self, email):
		user = Users.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use!')

class LoginForm(FlaskForm):
	email = StringField('Email',
		validators=[
			DataRequired(),
			Email()
		])
	password = PasswordField('Password',
		validators=[
			DataRequired()
		])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	email = StringField('Email',
		validators=[
		DataRequired(),
		Email()
		])
	submit = SubmitField('Update')

	def validate_email(self,email):
		if email.data != current_user.email:
			user = Users.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use - Please choose another')

class TeamForm(FlaskForm):
	character1 = SelectField("Character 1",
		choices=[Gamecharacters.query.get(Gamecharacters.character_name)]
		)
	character2 = StringField('Character 2',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	character3 = StringField('Character 3',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	character4 = StringField('Character 4',
		validators=[
			DataRequired(),
			Length(min=3, max=30)
		])
	submit = SubmitField('Create Team')