import unittest
from api.login1 import LoginAPI

class TestLogin(unittest.TestCase):
	
	# 前置处理
	def setUp(self):
		self.login_api = LoginAPI()
		
	# 后置处理
	def tearDown(self):
		pass
	
	# 定义测试用例
	def test01_case001(self):
		response=self.login_api.login({"mobile":"1111","password":"123456"})
		print(response.json())
		# 断言
		self.assertEqual(200,response.status_code)
	