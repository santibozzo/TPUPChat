from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()

"""Factory that creates instance of the app"""
def create_app(testing=False):
	if not testing:
		load_dotenv()
	app = Flask(__name__)

	app.config.from_object(config['testing'] if testing else config[os.environ.get('PROFILE')])

	db.init_app(app)
	bootstrap.init_app(app)
	login_manager.init_app(app)

	from Chat.main.main import main
	app.register_blueprint(main)

	from Chat.signup.signup import signup
	app.register_blueprint(signup)

	from Chat.login.login import login
	app.register_blueprint(login)

	from Chat.chats.chats import chats
	app.register_blueprint(chats)

	from Chat.chat.chat import chat
	app.register_blueprint(chat)

	return app
