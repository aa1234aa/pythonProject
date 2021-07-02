import unittest
import requests
from api.login import LoginAPI
import json
import app
from parameterized import parameterized
from tools.dbutil import DBUtil

def build_data():
	test_data = []
	sql="select * from t_login"
	db_data=DBUtil.exe_sql(sql)
	for case in db_data:
			username = case[2]
			password = case[3]
			status_code = case[5]
			status = case[7]
			msg = case[8]
			test_data.append((username, password, status_code, status, msg))
	print(test_data)
	return test_data


# 创建测试类
class TestLogin(unittest.TestCase):
	# 前置处理
	def setUp(self):
		self.session = requests.Session()
		self.login_api = LoginAPI()
	
	# 后置处理
	def tearDown(self):
		if self.session:
			self.session.close()
	
	# 创建测试用例
	@parameterized.expand(build_data())
	def test01_login(self, username, password, status_code, status, msg):
		# 调用验证码接口进行断言
		response = self.login_api.get_verify_code(self.session)
		print(response.json())
		self.assertEqual(status_code, response.status_code)
		# 调用登录接口获取登录信息，并进行断言
		reponse = self.login_api.login(self.session, username, password, "8888")
		print(reponse.json())
		self.assertEqual(status_code, response.status_code)
		self.assertEqual(status, response.json().get("status"))
		self.assertIn(msg, response.json().get("msg"))



