from application.models import Game_Characters
from application import db

with open("character_attributes.txt", "r") as file:
	lines = file.read().splitlines()

data = []
for i in lines:
	data.append(i.split(", "))

for line in range(38):
	characters = Game_Characters(id=data[line][0], character=data[line][1], all_new_xmen=data[line][2], agents_of_shield=data[line][3]
		, agile_fighters=data[line][4], anti_heroes=data[line][5], avengers=data[line][6], back_in_black=data[line][7]
		, big_brains=data[line][8], the_crew=data[line][9], cutting_edge=data[line][10], defenders=data[line][11]
		, family_values=data[line][12], femme_fatale=data[line][13], forces_of_nature=data[line][14], generations=data[line][15]
		, gods_and_demons=data[line][16], guardians=data[line][17], heavy_hitters=data[line][18], heavy_metal=data[line][19]
		, martial_artists=data[line][20], marvel_royalty=data[line][21], midnight_sons=data[line][22], new_avengers=data[line][23]
		, original_avengers=data[line][24], partners=data[line][25], sharpshooters=data[line][26], team_leaders=data[line][27]
		, ultimate_alliance_3=data[line][28], villains=data[line][29], web_warriors=data[line][30], wise_cracking=data[line][31]
		, women_of_marvel=data[line][32], x_force=data[line][33], x_men=data[line][34])


	db.session.add(characters)

db.session.commit()