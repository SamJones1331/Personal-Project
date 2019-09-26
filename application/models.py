from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable=False)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)


	def __repr__(self):
		return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name])
