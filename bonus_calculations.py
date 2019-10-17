from application import db
from application.models import Gamecharacters, Team


strength_bonus = 0
durability_bonus = 0
resistance_bonus = 0
mastery_bonus = 0
vitality_bonus = 0
energy_bonus = 0

print(Team.query.filter_by(user_id=current_user.id).all())

def OverallTeamBonus ():
	pass

def StrengthBonus():
	pass

def DurabilityBonus():
	pass

def ResistanceBonus():
	pass

def MasteryBonus():
	pass

def VitalityBonus():
	pass

def EnergyBonus():
	pass

def AgileFightersBonus():
	




bonus = 0
lists = db.session.query(Team.character1).filter_by(user_id=current_user.id).all()
lists = str(lists)
def replace(lists):
	lists = lists.replace("[", "")
	lists = lists.replace("]", "")
	lists = lists.replace("(", "")
	lists = lists.replace(")", "")
	lists = lists.replace(",", "")
	lists = lists.replace("'", "")
	lists = lists.replace("'", "")
	return lists
newlist = replace(lists)
newlist = str(newlist)
print(newlist)
lists2 = db.session.query(Gamecharacters.id).filter_by(character_name=newlist).all()
print(lists2)