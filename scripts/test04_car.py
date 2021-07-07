import unittest
from api.car import Car
import app
import json
from utils import common_assert_success
from parameterized import parameterized
# json 参数化

def build_data():
	test_data=[]
	file= app.BASE_DIR+"/data/car.json"
	print(file)
	with open(file,encoding="utf-8") as f:
		json_data=json.load(f)
		for case in json_data:
			print(case)
			ownerName=case.get("ownerName")
			unitName = case.get("unitName")
			jobPost = case.get("jobPost")
			jobNumber = case.get("jobNumber")
			telPhone = case.get("telPhone")
			address = case.get("address")
			email = case.get("email")
			cardType = case.get("cardType")
			cardNo = case.get("cardNo")
			frontCardImgId = case.get("frontCardImgId")
			backCardImgId = case.get("backCardImgId")
			faceCardImgId = case.get("faceCardImgId")
			unitId = case.get("unitId")
			test_data.append((ownerName,unitName,jobPost,jobNumber,telPhone,address,email,cardType,cardNo,frontCardImgId,backCardImgId,faceCardImgId,unitId))
			print(test_data)
	return test_data
	


class TestCar(unittest.TestCase):
	
	def setUp(self):
		self.car = Car()
		
	# 获取响应结果
	@parameterized.expand(build_data())
	def test01_add_car(self,ownerName,unitName,jobPost,jobNumber,telPhone,address,email,cardType,cardNo,frontCardImgId,backCardImgId,faceCardImgId,unitId):
		add_sub={
			"ownerName":ownerName,
			"unitName":unitName,
			"jobPost":jobPost,
			"jobNumber":jobNumber,
			"telPhone":telPhone,
			"address":address,
			"email":email,
			"cardType":cardType,
			"cardNo":cardNo,
			"frontCardImgId":frontCardImgId,
			"backCardImgId":backCardImgId,
			"faceCardImgId":faceCardImgId,
			"unitId":unitId}
		response = self.car.add_sub(add_sub_data=add_sub)
		common_assert_success(self, response)

