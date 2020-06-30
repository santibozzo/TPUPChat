from test_base import BaseTestClass
import unittest
from test_utils import signup, login

class ChatsTestCase(BaseTestClass):

	def test_chats_get(self):
		signup(self.client)
		login(self.client)
		res = self.client.get('/chats')
		self.assertEqual(200, res.status_code)

	def test_chats_post(self):
		signup(self.client)
		login(self.client)
		res = self.client.post(
			'/chats',
			data={
				'username': 'test_user_1'
			}
		)
		self.assertEqual(302, res.status_code)

if __name__ == '__main__':
	unittest.main()
