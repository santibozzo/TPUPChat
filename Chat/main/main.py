from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask_login import logout_user
from Chat.models import get_all_users

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	users = get_all_users()
	print(users)
	return render_template('index.html', username=users[0].password)

@main.route('/logout', methods=['POST'])
def logout():
	logout_user()
	return redirect(url_for('main.home'))
