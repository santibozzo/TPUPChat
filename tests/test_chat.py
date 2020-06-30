from test_base import BaseTestClass
import unittest
from test_utils import signup, login, create_chat
from datetime import datetime

class ChatTestCase(BaseTestClass):

	def test_chat_get(self):
		signup(self.client)
		login(self.client)
		create_chat(self.client)
		res = self.client.get('/chat?id=1')
		self.assertEqual(200, res.status_code)

	def test_chat_post(self):
		signup(self.client)
		login(self.client)
		create_chat(self.client)
		res = self.client.post(
			'/chat',
			data={
				'chat': 1,
				'from_user': 'test_user_1',
				'message': 'Hi!',
				'date': datetime.now()
			}
		)
		self.assertEqual(302, res.status_code)

if __name__ == '__main__':
	unittest.main()
