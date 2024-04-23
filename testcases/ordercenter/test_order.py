import allure
import pytest
from core.ApiService import api_service
from utils.YamlUtil import yaml_util


@allure.feature("用户订单模块")
class TestOrder:
    @pytest.mark.parametrize("data", yaml_util.extract_case('order_center.yaml', 'order_list'))
    def test_order_list(self, data, login_token):
        api_service.handle_case(data, login_token)

    @pytest.mark.parametrize("data", yaml_util.extract_case('order_center.yaml', 'order_detail'))
    def test_order_detail(self, data, login_token):
        api_service.handle_case(data, login_token)

# 测试一次上传