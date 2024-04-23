import allure
from api.api import mk
from utils.read_util import base_data


@allure.feature("用户中心")
class TestMessage:
    @allure.story("留言中心")
    @allure.title("发表留言-上传文件")
    def test_add_message(self, login_token):
        headers = login_token[0]
        data = base_data.read_data()['add_message']
        files = base_data.read_file()
        result = mk.add_message(data, files, headers)
        assert result.success is True
        assert result.body['subject'] == data['subject']
        assert result.body['message'] == data['message']
        assert result.body['file'] is not None
        assert result.body['add_time'] is not None
