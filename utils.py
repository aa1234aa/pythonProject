# 公共断言方法
def common_assert_success(case, response, status_code=200, message="新增成功"):
    case.assertEqual(status_code, response.json().get("code"))
    case.assertIn(message, "新增成功", response.json().get("data"))
