import allure
import pytest
from api.api import mk
from core.ApiService import api_service
from testcases.usercenter.conftest import dbo
from utils.YamlUtil import yaml_util
from utils.read_util import base_data


@allure.feature("用户中心模块")
class TestUser:
    @pytest.mark.parametrize("data", yaml_util.extract_case('user_center.yaml', 'user_login'))
    def test_user(self, data):
        r = api_service.handle_case(data)
        print(r)

# @allure.feature("用户中心")
# class TestUser:
#     @allure.story("用户注册")
#     @allure.title("获取验证码")
#     @pytest.mark.parametrize("json_data", base_data.read_data()['register'])
#     def test_send_code(self, json_data):
#         result = mk.send_code(json_data)
#
#         assert result.success is True
#         mobile = result.body['mobile']
#         db_code = dbo.get_bd_code(mobile)
#         assert db_code is not None
#         assert mobile == json_data['mobile']
#
#     @allure.story("用户注册")
#     @allure.title("手机号注册-创建账户")
#     def test_register(self):
#         json_data = base_data.read_data()['register']
#         mk.send_code(json_data)  # 发送验证码
#         mobile = json_data['mobile']
#         db_code = dbo.get_bd_code(mobile)
#         result_register = mk.register(mobile, db_code)  # 注册
#
#         assert result_register.success is True
#         assert result_register.body['username']
#         assert result_register.body['mobile']
#         assert 'token' in result_register.body
#         db_user = dbo.get_db_user(mobile)
#         assert db_user is not None
#         dbo.delete_db_user(mobile)
#
#     @allure.story("用户登录")
#     @allure.title("手机号密码登录")
#     def test_login(self):
#         json_data = base_data.read_data()['login']
#         result = mk.login(json_data)
#
#         assert result.success is True
#         assert result.body['token'] is not None
#
