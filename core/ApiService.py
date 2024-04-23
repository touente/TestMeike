import allure
from core.rest_client import RestClient
from utils.AssertUtil import assert_util
from utils.ExtractUtil import ExtractUtil
from utils.YamlUtil import yaml_util


class ApiService:
    def __init__(self):
        self.session = RestClient()
        self.extract = ExtractUtil()

    def handle_case(self, test_data, login_token=None):
        # 获取 url、method、headers、case_info、validate
        url = self.extract.extract_url(test_data['request_info']['url'])
        method = test_data['request_info']['method']
        headers = test_data['request_info']['headers']
        if login_token:
            headers.update(login_token)  # update()两个字典相加
        # 获取allure_story
        allure_story = test_data['request_info']['case_story']
        allure.dynamic.story(allure_story)
        # 获取case_info、validate
        case_info = test_data['case_info']
        allure_title = case_info.pop("case_title", None)
        allure.dynamic.title(allure_title)
        validate = case_info.pop("validate", None)  # pop()移除指定键值对
        extract = case_info.pop("extract_data", None)
        case_info = self.extract.extract_case(case_info)
        # 执行接口请求
        result = self.session.do_request(url=url, method=method, headers=headers, **case_info)
        self.extract.extract_data(result, extract)
        # 断言逻辑
        assert_util.validate_response(result, validate)
        return result


api_service = ApiService()
