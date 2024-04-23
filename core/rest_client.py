import json
import requests
from utils.log_util import logger
from utils.read_util import base_data

api_url = base_data.read_ini()['host']['api_url']


class RestClient:
    def __init__(self):
        self.api_url = api_url
        self.session = requests.Session()

    def do_request(self, url, method, **kwargs):
        response = self.request(url, method, **kwargs).json()
        logger.info("接口返回内容为>>>\n{}".format(json.dumps(response, ensure_ascii=False, indent=2)))
        return response

    def request(self, url, method, **kwargs):
        self.request_log(url, method, **kwargs)
        if method == "GET":
            return requests.get(self.api_url + url, **kwargs)
        if method == "POST":
            return requests.post(self.api_url + url, **kwargs)
        if method == "PUT":
            return requests.put(self.api_url + url, **kwargs)
        if method == "DELETE":
            return requests.delete(self.api_url + url, **kwargs)

    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        logger.info("接口请求的地址>>>{}".format(self.api_url + url))
        logger.info("接口请求的方法>>>{}".format(method))
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))
