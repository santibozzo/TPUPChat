
def signup(client):
	res = client.post(
		'/signup',
		data={
			'username': 'test_user_1',
			'password': 'pass1',
			'repeatPassword': 'pass1'
		}
	)

def login(client):
	res = client.post(
		'/login',
		data={
			'username': 'test_user_1',
			'password': 'pass1'
		}
	)

def create_chat(client):
	res = client.post(
		'/chats',
		data={
			'username': 'test_user_1'
		}
	)
