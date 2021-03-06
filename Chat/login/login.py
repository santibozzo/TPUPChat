from flask import request
from flask import render_template
from flask import Blueprint
from flask import redirect
from flask import url_for
from flask import flash
from flask_login import current_user, login_user
from Chat import db
from Chat.models import User, get_user
from werkzeug.security import check_password_hash

login = Blueprint('login', __name__)

"""Gets login page"""
@login.route('/login', methods=['GET'])
def login_get():
	if current_user.is_authenticated:
		return redirect(url_for('chats.chats_get'))
	return render_template('login.html')

"""Logins user with given credentials"""
@login.route('/login', methods=['POST'])
def login_post():
	username = request.form.get('username')
	password = request.form.get('password')
	user = get_user(username)
	if user is not None and check_password_hash(user.password, password):
		login_user(user)
		return redirect(url_for('chats.chats_get'))
	else:
		flash('Wrong username or password')
		return redirect(url_for('login.login_get')), 303
