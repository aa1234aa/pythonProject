
class LoginAPI:
	def __init__(self):
		self.url_versify="http://10.11.1.22:6060/api/v1/login/randCode"
		self.url_login="http://10.11.1.22:6060/login"
	
	# 获取验证码
	def get_verify_code(self,session):
		return session.get(self.url_versify)
	
	# 登录
	def login(self,session,username,password,verify_code):
		login_data={
			"username": username,
			"password": password,
			"verify_code": verify_code
		}
		session.post(url=self.url_login,data=login_data)