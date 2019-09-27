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

class Game_Characters(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	character = db.Column(db.String(30), nullable=False)
	all_new_xmen = db.Column(db.Boolean, nullable=False)
	agents_of_shield = db.Column(db.Boolean, nullable=False)
	agile_fighters = db.Column(db.Boolean, nullable=False)
	anti_heroes = db.Column(db.Boolean, nullable=False)
	avengers = db.Column(db.Boolean, nullable=False)
	back_in_black = db.Column(db.Boolean, nullable=False)
	big_brains = db.Column(db.Boolean, nullable=False)
	the_crew = db.Column(db.Boolean, nullable=False)
	cutting_edge = db.Column(db.Boolean, nullable=False)
	defenders = db.Column(db.Boolean, nullable=False)
	family_values = db.Column(db.Boolean, nullable=False)
	femme_fatales = db.Column(db.Boolean, nullable=False)
	forces_of_nature = db.Column(db.Boolean, nullable=False)
	generations = db.Column(db.Boolean, nullable=False)
	gods_and_demons = db.Column(db.Boolean, nullable=False)
	guardians = db.Column(db.Boolean, nullable=False)
	heavy_hitters = db.Column(db.Boolean, nullable=False)
	heavy_metal = db.Column(db.Boolean, nullable=False)
	martial_artists = db.Column(db.Boolean, nullable=False)
	marvel_royalty = db.Column(db.Boolean, nullable=False)
	midnight_sons = db.Column(db.Boolean, nullable=False)
	new_avengers = db.Column(db.Boolean, nullable=False)
	original_avengers = db.Column(db.Boolean, nullable=False)
	partners = db.Column(db.Boolean, nullable=False)
	sharpshooters = db.Column(db.Boolean, nullable=False)
	team_leaders = db.Column(db.Boolean, nullable=False)
	ultimate_alliance_3 = db.Column(db.Boolean, nullable=False)
	villains = db.Column(db.Boolean, nullable=False)
	web_warriors = db.Column(db.Boolean, nullable=False)
	wise_cracking = db.Column(db.Boolean, nullable=False)
	women_of_marvel = db.Column(db.Boolean, nullable=False)
	x_force = db.Column(db.Boolean, nullable=False)
	x_men = db.Column(db.Boolean, nullable=False)

	def __repr__(self):
		return ("Character: ", self.character)