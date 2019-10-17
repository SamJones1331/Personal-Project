from flask import render_template , redirect, url_for, request, flash
from application import app, db, bcrypt
from application.models import Users, Gamecharacters, Team
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, TeamForm, UpdateTeamForm
from flask_login import login_user, current_user, logout_user, login_required, LoginManager

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')
@app.route('/about')
def about():
	return render_template('about.html', title='About')
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)
@app.route('/logout')
def logout ():
	logout_user()
	return redirect(url_for('login'))
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data)
		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			email=form.email.data, 
			password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('account'))
	return render_template('register.html', title='Register', form=form)
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)

@app.route('/team', methods=['GET', 'POST'])
@login_required
def team():
	form = TeamForm()
	if form.submit.data:
		teamData = Team(
						character1=form.character1.data,
						character2=form.character2.data,
						character3=form.character3.data,
						character4=form.character4.data,
						author=current_user
			)
		db.session.add(teamData)
		db.session.commit()
		return redirect(url_for('userteam'))
	else:
		print(form.errors)
	return render_template ('team.html', title='Team', form=form)
@app.route('/userteam')
@login_required
def userteam():
	term = Team.query.filter_by(user_id=current_user.id).all()
	return render_template ('userteam.html', title="Your Team", teams=term)

@app.route('/updateteam', methods=["GET", "POST"])
@login_required
def updateteam():
	form = UpdateTeamForm()
	if form.submit.data:
		team = Team.query.filter_by(user_id=current_user.id).first()
		team.character1=form.character1.data
		team.character2=form.character2.data
		team.character3=form.character3.data
		team.character4=form.character4.data
		db.session.commit()
		return redirect(url_for('userteam'))
	else:
		print(form.errors)
	return render_template ('updateteam.html', title='Update Team', form=form)