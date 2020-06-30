from test_base import BaseTestClass
import unittest

class MainTestCase(BaseTestClass):

	def test_home_get(self):
		res = self.client.get('/home')
		self.assertEqual(200, res.status_code)

if __name__ == '__main__':
	unittest.main()
