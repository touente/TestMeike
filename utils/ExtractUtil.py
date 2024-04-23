import json
import time
from utils.AssertUtil import AssertUtil
from utils.YamlUtil import YamlUtil
from utils.log_util import logger


class ExtractUtil:
    def __init__(self):
        self.jsonpath_util = AssertUtil()
        self.yaml_util = YamlUtil()

    def extract_data(self, result, extract_data):
        """根据extract_data表达式获取接口内容并存入yaml"""
        if extract_data:
            for key, expression in extract_data.items():
                try:
                    value = self.jsonpath_util.extract_by_jsonpath(result, expression)
                    # 写
                    self.yaml_util.write_extract_yaml({key: value})
                except Exception as e:
                    logger.error(f"变量{key}写入extract.yaml文件失败！error = {e}")

    def get_extract_value(self, key):
        """从extract.yaml中获取内容"""
        try:
            data = self.yaml_util.read_extract_yaml()
            return data[key]
        except Exception as e:
            logger.error(f"从extract.yaml中根据{key}获取不到内容！error={e}")

    def extract_url(self, url):
        # / orders /${get_extract_value(order_id)} /
        if "${" and "}" in url:
            return self.process_data(url)
        else:
            return url

    def process_data(self, data):
        """处理函数"""
        for i in range(data.count("${")):  # data.count("a")找出现次数
            if "${" in data and "}" in data:
                start_index = data.index('$')
                end_index = data.index('}')
                func_full_name = data[start_index:end_index + 1]
                func_name = data[start_index + 2:data.index('(')]
                func_params = data[data.index('(') + 1:data.index(')')]
                # 处理函数的参数
                extract_data = getattr(self, func_name, None)
                if extract_data:
                    func_params = func_params.split(',') if func_params else []  # 拆分成列表
                    func_params = [int(param) if param.isdigit() else param for param in func_params]
                    extract_data = extract_data(*func_params)  # fun(a,*b)  *b是解包
                data = data.replace(func_full_name, str(extract_data))
        return data

    def extract_case(self, case_info):
        str_case_info = json.dumps(case_info)
        data = self.process_data(str_case_info)
        return json.loads(data)

    def get_time(self):
        return int(time.time())
