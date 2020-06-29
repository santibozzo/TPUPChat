from test_base import BaseTestClass
import unittest

class SignupTestCase(BaseTestClass):

	def test_signup_get(self):
		res = self.client.get('/signup')
		self.assertEqual(200, res.status_code)

	def test_signup_post(self):
		res = self.client.post(
			'/signup',
			data={
				'username': 'test_user_1',
				'password': 'pass1',
				'repeatPassword': 'pass1'
			}
		)
		self.assertEqual(302, res.status_code)

if __name__ == '__main__':
	unittest.main()
