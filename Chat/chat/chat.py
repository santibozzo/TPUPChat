from flask import request
from flask import flash
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import current_user
from Chat.models import get_chat, Message, get_chat_messages, create_message
from datetime import datetime

chat = Blueprint('chat', __name__)

@chat.route('/chat', methods=['GET'])
def chat_get():
	if not current_user.is_authenticated:
		return redirect(url_for('main.home'))
	other_user = request.args.get('user')
	chat = get_chat(current_user.username, other_user)
	if chat:
		messages = get_chat_messages(current_user.username, other_user)
		return render_template('chat.html', messages=messages, other_user=other_user)
	return redirect(url_for('chats.chats_get'))

@chat.route('/chat', methods=['POST'])
def chat_post():
	other_user = request.args.get('to')
	message = request.form.get('message')
	if len(message) > 500:
		flash('Message must be shorter than 500 characters')
		return redirect(url_for('chat.chat_get', user=other_user))
	new_message = Message(
		from_user=current_user.username,
		to_user=other_user,
		message=message,
		date=datetime.now()
	)
	create_message(new_message)
	return redirect(url_for('chat.chat_get', user=other_user))
