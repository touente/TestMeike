import allure
from api.api import mk
from testcases.shoppingcenter.conftest import dbo
from utils.login import login
from utils.read_util import base_data
from utils.YamlUtil import yaml_util


@allure.feature("购物中心")
class TestUser:

    @allure.story("购物车")
    @allure.title("购物车添加商品-随机商品")
    def test_add_shopcarts(self, login_token):
        # 登录(使用fixture夹具)
        login_data = login_token
        # 获取加购物车参数,随机商品和数量
        data = base_data.read_data()['add_shopcarts']
        json_data = yaml_util(data)
        # 查询当前商品购物车内数量
        num1 = dbo.get_goods_num(login_data[1], json_data['goods'])
        result = mk.add_shopcarts(json_data, login_data[0])
        num2 = dbo.get_goods_num(login_data[1], json_data['goods'])

        assert result.success is True
        assert num1 + int(json_data['nums']) == num2
        assert num2 == result.body['nums']

    @allure.title("购物车添加商品-随机已加购物车的商品")
    def test_add_existed_goods(self):
        # 登录（使用自定义方法）每次都要调用，不太好
        login_data = login()
        # 获取购物车已有的随机商品和数量
        data = base_data.read_data()['add_shopcarts_existed']
        json_data = yaml_util(data)
        # 查询当前商品购物车内数量
        num1 = dbo.get_goods_num(login_data[0], json_data['goods'])
        result = mk.add_shopcarts(json_data, login_data[1])
        num2 = dbo.get_goods_num(login_data[0], json_data['goods'])

        assert result.success is True
        assert num1 + int(json_data['nums']) == num2
        assert num2 == result.body['nums']

