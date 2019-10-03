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
	lists = Gamecharacters.query.filter_by(character_name=Gamecharacters.character_name).all()
	names = []
	print(lists)
	for i in range(int(len(lists))):
		temp = [lists[i], lists[i]]
		names.append(temp)

	character1 = SelectField("Character 1",
		choices= names
		)
	character2 = SelectField("Character 2",
		choices= names
		)
	character3 = SelectField("Character 3",
		choices= names
		)
	character4 = SelectField("Character 4",
		choices= names
		)
	submit = SubmitField('Create Team')