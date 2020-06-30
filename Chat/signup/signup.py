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

"""Gets signup page"""
@signup.route('/signup', methods=['GET'])
def signup_get():
	if current_user.is_authenticated:
		return redirect(url_for('chats.chats_get'))
	return render_template('signup.html')

"""Creates new user"""
@signup.route('/signup', methods=['POST'])
def signup_post():
	username = request.form.get('username')
	password = request.form.get('password')
	repeatPassword = request.form.get('repeatPassword')
	user = get_user(username)
	if user:
		flash('Username already exists')
		return redirect(url_for('signup.signup_get')), 303
	if len(username) > 150:
		flash('Username must be shorter than 150 characters')
		return redirect(url_for('signup.signup_get')), 303
	if len(password) > 100:
		flash('Password must be shorter than 100 characters')
		return redirect(url_for('signup.signup_get')), 303
	if password != repeatPassword:
		flash('Passwords are different')
		return redirect(url_for('signup.signup_get')), 303
	new_user = User(
		username=username,
		password=generate_password_hash(password))
	create_user(new_user)

	return redirect(url_for('main.home'))
