from Chat import db
from Chat import login_manager
from flask_login import UserMixin


### USER ###

@login_manager.user_loader
def load_user(user_username):
	return User.query.get(user_username)

"""User database entity"""
class User(db.Model, UserMixin):

	__tablename__ = 'users'

	username = db.Column(db.String(150), primary_key=True, unique=True)
	password = db.Column(db.String(100))

	def get_id(self):
		return self.username

	def __repr__(self):
		return f"<User {self.username}>"

"""Gets all users"""
def get_all_users():
	return User.query.all()

"""Gets user filter by given username"""
def get_user(username):
	return User.query.filter_by(username=username).first()

"""Creates new user"""
def create_user(new_user):
	db.session.add(new_user)
	db.session.commit()

### CHAT ###

"""Chat database entity"""
class Chat(db.Model):

	__tablename__ = 'chats'

	id = db.Column(db.Integer, primary_key=True, unique=True)
	user1 = db.Column(db.String(150))
	user2 = db.Column(db.String(150))

	def __repr__(self):
		return f"<Chat {self.id}>"

"""Gets all chats where given username is in"""
def get_user_chats(username):
	return Chat.query.filter((Chat.user1 == username) | (Chat.user2 == username)).all()

"""Gets chat filter by id"""
def get_chat(chat_id):
	return Chat.query.filter_by(id=chat_id).first()

"""Gets chat where the participants are given usernames"""
def get_chat_by_participants(username1, username2):
	chat = Chat.query.filter_by(user1=username1, user2=username2).first()
	if chat:
		return chat
	return Chat.query.filter_by(user1=username2, user2=username1).first()

"""Creates new chat"""
def create_chat(new_chat):
	db.session.add(new_chat)
	db.session.commit()


### MESSAGE ###

"""Message database entity"""
class Message(db.Model):

	__tablename__ = 'messages'

	id = db.Column(db.Integer, primary_key=True, unique=True)
	chat = db.Column(db.Integer)
	from_user = db.Column(db.String(150))
	date = db.Column(db.DateTime)
	message = db.Column(db.String(500))

"""Gets all messages from given chat id"""
def get_chat_messages(chat_id):
	return Message.query.filter_by(chat=chat_id).order_by(Message.date.desc()).all()

"""Creates new message"""
def create_message(message):
	db.session.add(message)
	db.session.commit()
