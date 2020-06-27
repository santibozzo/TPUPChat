from flask import request
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import current_user
from Chat.models import User, get_user, create_user
from werkzeug.security import generate_password_hash

signup = Blueprint('signup', __name__)

@signup.route('/signup', methods=['GET'])
def signup_get():
	if current_user.is_authenticated:
		return render_template('index.html')
	return render_template('signup.html')

@signup.route('/signup', methods=['POST'])
def signup_post():
	username = request.form.get('username')
	password = request.form.get('password')
	repeatPassword = request.form.get('repeatPassword')
	user = get_user(username)
	if user:
		flash('Username already exists')
		return redirect(url_for('signup.signup_get'))
	if password != repeatPassword:
		flash('Passwords are different')
		return redirect(url_for('signup.signup_get'))
	new_user = User(
		username=username,
		password=generate_password_hash(password))
	create_user(new_user)

	return redirect(url_for('main.home'))
