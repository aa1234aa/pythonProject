import app
import requests


class Car():
	# 初始化
	def __init__(self):
		self.add_peopl_url=app.BASE_URL + "/api/v1/sys/ownerPeople"
		
	# 添加联系人
	def add_sub(self,add_sub_data):
		aa= requests.post(url=self.add_peopl_url,json=add_sub_data,headers=app.headers)
		return aa
	
	# 修改
	def update_car(self,sub_id,update_dta):
		pass
	
	#  查询
	def get_employee(self):
		pass
	
	# 删除
	def delete_employee(self):
		pass