from flask_wtf import FlaskForm
from application import db
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from application.models import Users, Gamecharacters, Team
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
	lists = []
	try:
		lists = Gamecharacters.query.filter_by(character_name=Gamecharacters.character_name).all()
	except:
  		print("gamecharacters don't exist, continuing with empty list")
	names = []
	for i in range(int(len(lists))):
		temp = [lists[i].character_name, lists[i].character_name]
		names.append(temp)

	character1 = SelectField("Character 1",
		choices= names,
		coerce=str
		)
	character2 = SelectField("Character 2",
		choices= names,
		coerce=str
		)
	character3 = SelectField("Character 3",
		choices= names,
		coerce=str
		)
	character4 = SelectField("Character 4",
		choices= names,
		coerce=str
		)
	submit = SubmitField('Create Team') 

	def validate_character1(self, character1):
		if character1.data == self.character2.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 2")
		elif character1.data == self.character3.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 3")
		elif character1.data == self.character4.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 4")

	def validate_character2(self, character2):
		if character2.data == self.character1.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 1")
		elif character2.data == self.character3.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 3")
		elif character2.data == self.character4.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 4")
	
	def validate_character3(self, character3):
		if character3.data == self.character1.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 1")
		elif character3.data == self.character2.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 2")
		elif character3.data == self.character4.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 4")

	def validate_character4(self, character4):
		if character4.data == self.character1.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 1")
		elif character4.data == self.character3.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 3")
		elif character4.data == self.character2.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 2")



class UpdateTeamForm(FlaskForm):
	lists = []
	try:
		lists = Gamecharacters.query.filter_by(character_name=Gamecharacters.character_name).all()
	except:
  		print("gamecharacters don't exist, continuing with empty list")
	names = []
	for i in range(int(len(lists))):
		temp = [lists[i].character_name, lists[i].character_name]
		names.append(temp)

	character1 = SelectField("Character 1",
		choices= names,
		coerce=str
		)
	character2 = SelectField("Character 2",
		choices= names,
		coerce=str
		)
	character3 = SelectField("Character 3",
		choices= names,
		coerce=str
		)
	character4 = SelectField("Character 4",
		choices= names,
		coerce=str
		)
	submit = SubmitField('Create Team') 

	def validate_character1(self, character1):
		if character1.data == self.character2.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 2")
		elif character1.data == self.character3.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 3")
		elif character1.data == self.character4.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 4")

	def validate_character2(self, character2):
		if character2.data == self.character1.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 1")
		elif character2.data == self.character3.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 3")
		elif character2.data == self.character4.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 4")
	
	def validate_character3(self, character3):
		if character3.data == self.character1.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 1")
		elif character3.data == self.character2.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 2")
		elif character3.data == self.character4.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 4")

	def validate_character4(self, character4):
		if character4.data == self.character1.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 1")
		elif character4.data == self.character3.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 3")
		elif character4.data == self.character2.data:
			raise ValidationError("Can't have multiple versions of the same character: Character 2")
