import unittest
import requests
from api.login import LoginAPI
import json
import app
from parameterized import parameterized
# json 参数化
def build_data():
	test_data=[]
	file= app.BASE_DIR+"/data/aa.json"
	print(file)
	with open(file,encoding="utf-8") as f:
		json_data=json.load(f)
		for case in json_data:
			username=case.get("username")
			password = case.get("password")
			status_code=case.get("status code")
			status = case.get("status")
			msg = case.get("msg")
			test_data.append((username,password,status_code,status,msg))
	return test_data

# 创建测试类
class TestLogin(unittest.TestCase):
	# 前置处理
	def setUp(self):
		self.session=requests.Session()
		self.login_api=LoginAPI()
	
	# 后置处理
	def tearDown(self):
		if self.session:
			self.session.close()
	
	# 创建测试用例
	@parameterized.expand(build_data())
	def test01_login(self,username,password,status_code,status,msg):
		# 调用验证码接口进行断言
		response=self.login_api.get_verify_code(self.session)
		print(response.json())
		self.assertEqual(status_code,response.status_code)
		# 调用登录接口获取登录信息，并进行断言
		reponse=self.login_api.login(self.session,username,password,"8888")
		print(reponse.json())
		self.assertEqual(status_code,response.status_code)
		self.assertEqual(status,response.json().get("status"))
		self.assertIn(msg,response.json().get("msg"))
		


