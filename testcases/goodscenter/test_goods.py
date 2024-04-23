import allure
import pytest

from api.api import mk
from core.ApiService import api_service
from testcases.goodscenter.conftest import dbo
from utils.YamlUtil import yaml_util


@allure.feature("商品中心")
class TestUser:

    @allure.story("首页展示内容")
    @allure.title("banners")
    def test_banners(self):
        result = mk.get_banners()
        assert result.success is True
        num = dbo.get_banner_count()
        assert len(result.body) == num

    @pytest.mark.parametrize("data", yaml_util.extract_case('goods_center.yaml', 'get_banner'))
    def test_banner(self,data):
        api_service.handle_case(data)
      # 这里的验证数量没有从数据库取，后面自己看看
