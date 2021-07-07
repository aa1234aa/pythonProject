"""
api  ----封装项目接口
data  ----存放数据参数化
report ---存放html报告的路径
scripts---编写测试脚本目录
tools ---存放第三方工具包
app.py ---存放配置信息
run_suite----测试套件的入口
util---自己编写工具类
"""
import json
import app
def build_data():
	test_data=[]
	file= app.BASE_DIR+"/data/car.json"
	print(file)
	with open(file,encoding="utf-8") as f:
		json_data=json.load(f)
		for case in json_data:
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
			test_data.append((ownerName,unitName,jobPost,jobNumber,telPhone,address,email,cardType
			,cardNo,frontCardImgId,backCardImgId,faceCardImgId,unitId))
			print(test_data)
	return test_data
	
