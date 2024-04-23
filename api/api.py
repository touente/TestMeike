from core.api_util import api_util
from utils.response_util import process_response


class Meike:
    # user api
    def send_code(self, json_data):
        """
        获取短信验证码
        一分钟之内发送次数过多会发送失败。
        一天发送次数过多会发送失败。
        :param json_data:
        :return:
        """
        result = api_util.get_send_code(json=json_data)
        result2 = process_response(result)
        return result2

    def register(self, mobile, code):
        """
        手机号注册
        :param mobile:
        :param code:
        :return:
        """
        json_data = {
            "code": str(code),
            "password": "123456",
            "username": str(mobile)
        }
        result = api_util.mobile_register(json=json_data)
        result2 = process_response(result)
        return result2

    def login(self, json_data):
        """
        登录
        :param json_data:
        :return:
        """
        result = api_util.user_login(json=json_data)
        result2 = process_response(result)
        return result2

    # goods api
    def get_banners(self):
        """
        首页banners展示
        :return:
        """
        result = api_util.banners()
        result2 = process_response(result)
        return result2

    # shopping api
    def add_shopcarts(self, json_data, headers):
        result = api_util.shopcarts(json=json_data, headers=headers)
        result2 = process_response(result)
        return result2

    def add_message(self, data, files, headers):
        result = api_util.message(data=data, files=files, headers=headers)
        result2 = process_response(result)
        return result2


mk = Meike()
