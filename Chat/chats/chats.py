from flask import request
from flask import flash
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import current_user
from Chat.models import Chat, get_user_chats, get_chat_by_participants, create_chat, get_user

chats = Blueprint('chats', __name__)

"""Gets chats page. Here all chats from current user are shown"""
@chats.route('/chats', methods=['GET'])
def chats_get():
	if not current_user.is_authenticated:
		return redirect(url_for('main.home'))
	chats_list = get_user_chats(current_user.username)
	return render_template('chats.html', chats_list=chats_list)

"""Creates new chat with given user"""
@chats.route('/chats', methods=['POST'])
def chats_post():
	username = request.form.get('username')
	user = get_user(username)
	if user is None:
		flash('No user found with that username')
		return redirect(url_for('chats.chats_get')), 303

	chat = get_chat_by_participants(current_user.username, username)
	if chat:
		flash('There is already a chat with that user')
		return redirect(url_for('chats.chats_get')), 303

	new_chat = Chat(
		user1=current_user.username,
		user2=username
	)
	create_chat(new_chat)
	return redirect(url_for('chats.chats_get'))

