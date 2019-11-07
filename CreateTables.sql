CREATE TABLE users (
id INT  NOT NULL,
email VARCHAR(150) NOT NULL UNIQUE,
password VARCHAR(128) NOT NULL,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE gamecharacters (
id INT NOT NULL,
character_name VARCHAR(30) NOT NULL,
all_new_xmen VARCHAR(30) NOT NULL,
agents_of_shield VARCHAR(30) NOT NULL,
agile_fighters VARCHAR(30) NOT NULL,
anti_heroes VARCHAR(30) NOT NULL,
avengers VARCHAR(30) NOT NULL,
back_in_black VARCHAR(30) NOT NULL,
big_brains VARCHAR(30) NOT NULL,
the_crew VARCHAR(30) NOT NULL,
cutting_edge VARCHAR(30) NOT NULL,
defenders VARCHAR(30) NOT NULL,
family_values VARCHAR(30) NOT NULL,
femme_fatales VARCHAR(30) NOT NULL,
forces_of_nature VARCHAR(30) NOT NULL,
generations VARCHAR(30) NOT NULL,
gods_and_demons VARCHAR(30) NOT NULL,
guardians VARCHAR(30) NOT NULL,
heavy_hitters VARCHAR(30) NOT NULL,
heavy_metal VARCHAR(30) NOT NULL,
martial_rtists VARCHAR(30) NOT NULL,
marvel_royalty VARCHAR(30) NOT NULL,
midnight_sons VARCHAR(30) NOT NULL,
new_avengers VARCHAR(30) NOT NULL,
original_avengers VARCHAR(30) NOT NULL,
partners VARCHAR(30) NOT NULL,
sharpshooters VARCHAR(30) NOT NULL,
team_leaders VARCHAR(30) NOT NULL,
ultimate_alliance_3 VARCHAR(30) NOT NULL,
villains VARCHAR(30) NOT NULL,
web_warriors VARCHAR(30) NOT NULL,
wise_cracking VARCHAR(30) NOT NULL,
women_of_marvel VARCHAR(30) NOT NULL,
x_force VARCHAR(30) NOT NULL,
x_men VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
);

CREATE TABLE team (
id INT NOT NULL,
character1 VARCHAR(150) NOT NULL,
character2 VARCHAR(150) NOT NULL,
character3 VARCHAR(150) NOT NULL,
character4 VARCHAR(150) NOT NULL,
user_id INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (user_id) REFERENCES Users(id)
);
