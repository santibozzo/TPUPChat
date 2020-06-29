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

"""Gets chat page"""
@chat.route('/chat', methods=['GET'])
def chat_get():
	if not current_user.is_authenticated:
		return redirect(url_for('main.home'))
	chat_id = request.args.get('id')
	chat = get_chat(chat_id)
	if chat:
		other_user = chat.user1 if chat.user1 != current_user.username else chat.user2
		messages = get_chat_messages(chat_id)
		return render_template('chat.html', messages=messages, chat=chat)
	return redirect(url_for('chats.chats_get'))

"""Creates new message in actual chat"""
@chat.route('/chat', methods=['POST'])
def chat_post():
	chat_id = request.args.get('id')
	message = request.form.get('message')
	if len(message) > 500:
		flash('Message must be shorter than 500 characters')
		return redirect(url_for('chat.chat_get', id=chat_id))
	new_message = Message(
		chat=chat_id,
		from_user=current_user.username,
		message=message,
		date=datetime.now()
	)
	create_message(new_message)
	return redirect(url_for('chat.chat_get', id=chat_id))
