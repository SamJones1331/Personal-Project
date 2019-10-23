from application import db
from application.models import Gamecharacters, Team
from flask_login import login_user, current_user, logout_user, login_required

def DurabilityBonus():
	finalDurabilityBonus = DefendersBonus() + FamilyValuesBonus() + GenerationsBonus() + HeavyMetalBonus() + NewAvengersBonus()
	return finalDurabilityBonus

def replaceFunction(query):
	lists = query.replace("[", "")
	lists = lists.replace("]", "")
	lists = lists.replace("(", "")
	lists = lists.replace(")", "")
	lists = lists.replace(",", "")
	lists = lists.replace("'", "")
	lists = lists.replace("'", "")
	return lists


def DefendersBonus():
	def bonusQuery1(query):
		query = db.session.query(Team.character1).filter_by(user_id=current_user.id).all()
		character1query = str(query)
		character1query = replaceFunction(character1query)
		g1query = db.session.query(Gamecharacters.defenders).filter_by(character_name=character1query).all()
		g1query =str(g1query)
		g1query = replaceFunction(g1query)
		return g1query
	def bonusQuery2(query):
		query = db.session.query(Team.character2).filter_by(user_id=current_user.id).all()
		character2query = str(query)
		character2query = replaceFunction(character2query)
		g2query = db.session.query(Gamecharacters.defenders).filter_by(character_name=character2query).all()
		g2query =str(g2query)
		g2query = replaceFunction(g2query)
		return g2query
	def bonusQuery3(query):
		query = db.session.query(Team.character3).filter_by(user_id=current_user.id).all()
		character3query = str(query)
		character3query = replaceFunction(character3query)
		g3query = db.session.query(Gamecharacters.defenders).filter_by(character_name=character3query).all()
		g3query =str(g3query)
		g3query = replaceFunction(g3query)
		return g3query
	def bonusQuery4(query):
		query = db.session.query(Team.character4).filter_by(user_id=current_user.id).all()
		character4query = str(query)
		character4query = replaceFunction(character4query)
		g4query = db.session.query(Gamecharacters.defenders).filter_by(character_name=character4query).all()
		g4query =str(g4query)
		g4query = replaceFunction(g4query)
		return g4query
	def bonusCountFunction(query):
		bonus = 0
		bonus_count = 0
		if bonusQuery1("") == 'True':
			bonus_count += 1
		if bonusQuery2("") == 'True':
			bonus_count += 1
		if bonusQuery3("") == 'True':
			bonus_count += 1
		if bonusQuery4("") == 'True':
			bonus_count += 1
		if bonus_count == 1:
			bonus = 0
		elif bonus_count == 2:
			bonus = 2
		elif bonus_count == 3:
			bonus = 4
		elif bonus_count == 4:
			bonus = 7
		return bonus
	defendersBonus = bonusCountFunction("")
	return defendersBonus

def FamilyValuesBonus():
	def bonusQuery1(query):
		query = db.session.query(Team.character1).filter_by(user_id=current_user.id).all()
		character1query = str(query)
		character1query = replaceFunction(character1query)
		g1query = db.session.query(Gamecharacters.family_values).filter_by(character_name=character1query).all()
		g1query =str(g1query)
		g1query = replaceFunction(g1query)
		return g1query
	def bonusQuery2(query):
		query = db.session.query(Team.character2).filter_by(user_id=current_user.id).all()
		character2query = str(query)
		character2query = replaceFunction(character2query)
		g2query = db.session.query(Gamecharacters.family_values).filter_by(character_name=character2query).all()
		g2query =str(g2query)
		g2query = replaceFunction(g2query)
		return g2query
	def bonusQuery3(query):
		query = db.session.query(Team.character3).filter_by(user_id=current_user.id).all()
		character3query = str(query)
		character3query = replaceFunction(character3query)
		g3query = db.session.query(Gamecharacters.family_values).filter_by(character_name=character3query).all()
		g3query =str(g3query)
		g3query = replaceFunction(g3query)
		return g3query
	def bonusQuery4(query):
		query = db.session.query(Team.character4).filter_by(user_id=current_user.id).all()
		character4query = str(query)
		character4query = replaceFunction(character4query)
		g4query = db.session.query(Gamecharacters.family_values).filter_by(character_name=character4query).all()
		g4query =str(g4query)
		g4query = replaceFunction(g4query)
		return g4query
	def bonusCountFunction(query):
		bonus = 0
		bonus_count = 0
		if bonusQuery1("") == 'True':
			bonus_count += 1
		if bonusQuery2("") == 'True':
			bonus_count += 1
		if bonusQuery3("") == 'True':
			bonus_count += 1
		if bonusQuery4("") == 'True':
			bonus_count += 1
		if bonus_count == 1:
			bonus = 0
		elif bonus_count == 2:
			bonus = 1
		elif bonus_count == 3:
			bonus = 2
		elif bonus_count == 4:
			bonus = 4
		return bonus
	familyBonus = bonusCountFunction("")
	return familyBonus

def GenerationsBonus():
	def bonusQuery1(query):
		query = db.session.query(Team.character1).filter_by(user_id=current_user.id).all()
		character1query = str(query)
		character1query = replaceFunction(character1query)
		g1query = db.session.query(Gamecharacters.generations).filter_by(character_name=character1query).all()
		g1query =str(g1query)
		g1query = replaceFunction(g1query)
		return g1query
	def bonusQuery2(query):
		query = db.session.query(Team.character2).filter_by(user_id=current_user.id).all()
		character2query = str(query)
		character2query = replaceFunction(character2query)
		g2query = db.session.query(Gamecharacters.generations).filter_by(character_name=character2query).all()
		g2query =str(g2query)
		g2query = replaceFunction(g2query)
		return g2query
	def bonusQuery3(query):
		query = db.session.query(Team.character3).filter_by(user_id=current_user.id).all()
		character3query = str(query)
		character3query = replaceFunction(character3query)
		g3query = db.session.query(Gamecharacters.generations).filter_by(character_name=character3query).all()
		g3query =str(g3query)
		g3query = replaceFunction(g3query)
		return g3query
	def bonusQuery4(query):
		query = db.session.query(Team.character4).filter_by(user_id=current_user.id).all()
		character4query = str(query)
		character4query = replaceFunction(character4query)
		g4query = db.session.query(Gamecharacters.generations).filter_by(character_name=character4query).all()
		g4query =str(g4query)
		g4query = replaceFunction(g4query)
		return g4query
	def bonusCountFunction(query):
		bonus = 0
		bonus_count = 0
		if bonusQuery1("") == 'True':
			bonus_count += 1
		if bonusQuery2("") == 'True':
			bonus_count += 1
		if bonusQuery3("") == 'True':
			bonus_count += 1
		if bonusQuery4("") == 'True':
			bonus_count += 1
		if bonus_count == 1:
			bonus = 0
		elif bonus_count == 2:
			bonus = 2
		elif bonus_count == 3:
			bonus = 4
		elif bonus_count == 4:
			bonus = 7
		return bonus
	generationsBonus = bonusCountFunction("")
	return generationsBonus

def HeavyMetalBonus():
	def bonusQuery1(query):
		query = db.session.query(Team.character1).filter_by(user_id=current_user.id).all()
		character1query = str(query)
		character1query = replaceFunction(character1query)
		g1query = db.session.query(Gamecharacters.heavy_metal).filter_by(character_name=character1query).all()
		g1query =str(g1query)
		g1query = replaceFunction(g1query)
		return g1query
	def bonusQuery2(query):
		query = db.session.query(Team.character2).filter_by(user_id=current_user.id).all()
		character2query = str(query)
		character2query = replaceFunction(character2query)
		g2query = db.session.query(Gamecharacters.heavy_metal).filter_by(character_name=character2query).all()
		g2query =str(g2query)
		g2query = replaceFunction(g2query)
		return g2query
	def bonusQuery3(query):
		query = db.session.query(Team.character3).filter_by(user_id=current_user.id).all()
		character3query = str(query)
		character3query = replaceFunction(character3query)
		g3query = db.session.query(Gamecharacters.heavy_metal).filter_by(character_name=character3query).all()
		g3query =str(g3query)
		g3query = replaceFunction(g3query)
		return g3query
	def bonusQuery4(query):
		query = db.session.query(Team.character4).filter_by(user_id=current_user.id).all()
		character4query = str(query)
		character4query = replaceFunction(character4query)
		g4query = db.session.query(Gamecharacters.heavy_metal).filter_by(character_name=character4query).all()
		g4query =str(g4query)
		g4query = replaceFunction(g4query)
		return g4query
	def bonusCountFunction(query):
		bonus = 0
		bonus_count = 0
		if bonusQuery1("") == 'True':
			bonus_count += 1
		if bonusQuery2("") == 'True':
			bonus_count += 1
		if bonusQuery3("") == 'True':
			bonus_count += 1
		if bonusQuery4("") == 'True':
			bonus_count += 1
		if bonus_count == 1:
			bonus = 0
		elif bonus_count == 2:
			bonus = 2
		elif bonus_count == 3:
			bonus = 4
		elif bonus_count == 4:
			bonus = 8
		return bonus
	metalBonus = bonusCountFunction("")
	return metalBonus

def NewAvengersBonus():
	def bonusQuery1(query):
		query = db.session.query(Team.character1).filter_by(user_id=current_user.id).all()
		character1query = str(query)
		character1query = replaceFunction(character1query)
		g1query = db.session.query(Gamecharacters.new_avengers).filter_by(character_name=character1query).all()
		g1query =str(g1query)
		g1query = replaceFunction(g1query)
		return g1query
	def bonusQuery2(query):
		query = db.session.query(Team.character2).filter_by(user_id=current_user.id).all()
		character2query = str(query)
		character2query = replaceFunction(character2query)
		g2query = db.session.query(Gamecharacters.new_avengers).filter_by(character_name=character2query).all()
		g2query =str(g2query)
		g2query = replaceFunction(g2query)
		return g2query
	def bonusQuery3(query):
		query = db.session.query(Team.character3).filter_by(user_id=current_user.id).all()
		character3query = str(query)
		character3query = replaceFunction(character3query)
		g3query = db.session.query(Gamecharacters.new_avengers).filter_by(character_name=character3query).all()
		g3query =str(g3query)
		g3query = replaceFunction(g3query)
		return g3query
	def bonusQuery4(query):
		query = db.session.query(Team.character4).filter_by(user_id=current_user.id).all()
		character4query = str(query)
		character4query = replaceFunction(character4query)
		g4query = db.session.query(Gamecharacters.new_avengers).filter_by(character_name=character4query).all()
		g4query =str(g4query)
		g4query = replaceFunction(g4query)
		return g4query
	def bonusCountFunction(query):
		bonus = 0
		bonus_count = 0
		if bonusQuery1("") == 'True':
			bonus_count += 1
		if bonusQuery2("") == 'True':
			bonus_count += 1
		if bonusQuery3("") == 'True':
			bonus_count += 1
		if bonusQuery4("") == 'True':
			bonus_count += 1
		if bonus_count == 1:
			bonus = 0
		elif bonus_count == 2:
			bonus = 2
		elif bonus_count == 3:
			bonus = 4
		elif bonus_count == 4:
			bonus = 7
		return bonus
	newAvBonus = bonusCountFunction("")
	return newAvBonus