from test_base import BaseTestClass
import unittest
from test_utils import signup

class LoginTestCase(BaseTestClass):

	def test_login_get(self):
		res = self.client.get('/login')
		self.assertEqual(200, res.status_code)

	def test_login_post(self):
		signup(self.client)
		res = self.client.post(
			'/login',
			data={
				'username': 'test_user_1',
				'password': 'pass1'
			}
		)
		self.assertEqual(302, res.status_code)

if __name__ == '__main__':
	unittest.main()
