from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import logout_user, current_user
from Chat.models import get_all_users

main = Blueprint('main', __name__)

"""Gets home page"""
@main.route('/')
@main.route('/home')
def home():
	if current_user.is_authenticated:
		return redirect(url_for('chats.chats_get'))
	return render_template('home.html')

"""Logs out current user"""
@main.route('/logout', methods=['POST'])
def logout():
	logout_user()
	return redirect(url_for('main.home'))
