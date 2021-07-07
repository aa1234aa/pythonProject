import requests


# 创建接口类
class LoginAPI:
	# 初始化
	def __init__(self):
		self.url=""
		
	# 定义接口调用办法
	def login(self,login_data):
		return requests.post(url=self.url,json=login_data)