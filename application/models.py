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

class Gamecharacters(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	character_name = db.Column(db.String(30), nullable=False)
	all_new_xmen = db.Column(db.String(30), nullable=False)
	agents_of_shield = db.Column(db.String(30), nullable=False)
	agile_fighters = db.Column(db.String(30), nullable=False)
	anti_heroes = db.Column(db.String(30), nullable=False)
	avengers = db.Column(db.String(30), nullable=False)
	back_in_black = db.Column(db.String(30), nullable=False)
	big_brains = db.Column(db.String(30), nullable=False)
	the_crew = db.Column(db.String(30), nullable=False)
	cutting_edge = db.Column(db.String(30), nullable=False)
	defenders = db.Column(db.String(30), nullable=False)
	family_values = db.Column(db.String(30), nullable=False)
	femme_fatales = db.Column(db.String(30), nullable=False)
	forces_of_nature = db.Column(db.String(30), nullable=False)
	generations = db.Column(db.String(30), nullable=False)
	gods_and_demons = db.Column(db.String(30), nullable=False)
	guardians = db.Column(db.String(30), nullable=False)
	heavy_hitters = db.Column(db.String(30), nullable=False)
	heavy_metal = db.Column(db.String(30), nullable=False)
	martial_artists = db.Column(db.String(30), nullable=False)
	marvel_royalty = db.Column(db.String(30), nullable=False)
	midnight_sons = db.Column(db.String(30), nullable=False)
	new_avengers = db.Column(db.String(30), nullable=False)
	original_avengers = db.Column(db.String(30), nullable=False)
	partners = db.Column(db.String(30), nullable=False)
	sharpshooters = db.Column(db.String(30), nullable=False)
	team_leaders = db.Column(db.String(30), nullable=False)
	ultimate_alliance_3 = db.Column(db.String(30), nullable=False)
	villains = db.Column(db.String(30), nullable=False)
	web_warriors = db.Column(db.String(30), nullable=False)
	wise_cracking = db.Column(db.String(30), nullable=False)
	women_of_marvel = db.Column(db.String(30), nullable=False)
	x_force = db.Column(db.String(30), nullable=False)
	x_men = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return  self.character_name
		# ''.join(["Character: ", self.character_name, ' ', "ANX: ", self.all_new_xmen, ' ', "AOS: ", self.agents_of_shield, ' ', "AF: ", self.agile_fighters, ' ', "AH: ", self.anti_heroes, ' ', "AV: ", self.avengers, 
		# 	' ', "BIB: ", self.back_in_black, ' ', "BB: ", self.big_brains, ' ', "TC: ", self.the_crew, ' ', "CE: ", self.cutting_edge, ' ', "DF: ", self.defenders, 
		# 	' ', "FV: ", self.family_values, ' ', "FF: ", self.femme_fatales, ' ', "FON: ", self.forces_of_nature, ' ', "GEN: ", self.generations, ' ', "GAD: ", self.gods_and_demons, 
		# 	' ', "GRD: ", self.guardians, ' ', "HH: ", self.heavy_hitters, ' ', "HM: ", self.heavy_metal, ' ', "MA: ", self.martial_artists, ' ', "MR: ", self.marvel_royalty, 
		# 	' ', "MS: ", self.midnight_sons, ' ', "NA: ", self.new_avengers, ' ', "OA: ", self.original_avengers, ' ', "PRT: ", self.partners, ' ', "SHRP: ", self.sharpshooters, 
		# 	' ', "TL: ", self.team_leaders, ' ', "UA3: ", self.ultimate_alliance_3, ' ', "VL: ", self.villains, ' ', "WW: ", self.web_warriors, ' ', "WC: ", self.wise_cracking, 
		# 	' ', "WOM: ", self.women_of_marvel, ' ', "XF: ", self.x_force, ' ', "XM: ", self.x_men])
	def Gamecharacters_query():
		return Gamecharacters.query	



class Team(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	character1 = db.Column(db.String(150), nullable=False)
	character2 = db.Column(db.String(150), nullable=False)
	character3 = db.Column(db.String(150), nullable=False)
	character4 = db.Column(db.String(150), nullable=False)

	def __repr__(self):
		return ''.join(["Character 1: ", self.character1, "\r\n", "Character 2: ", self.character2, "\r\n", "Character 3: ", self.character3, "\r\n", "Character 4: ", self.character4])