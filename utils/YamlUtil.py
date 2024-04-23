import os
import random
import yaml
from faker import Faker  # 创造随机数据
from testcases.shoppingcenter.conftest import dbo
from utils.read_util import base_data

fake = Faker("zh_CN")  # 指定为中文


class YamlUtil:
    def __init__(self):
        self.yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data/")

    def read_extract_yaml(self):
        with open(self.yaml_path + "extract.yaml", mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            return value

    def read_case_yaml(self, yaml_name, key_name=None):
        with open(self.yaml_path + yaml_name, mode='r', encoding='utf8') as f:
            value = yaml.safe_load(f)
            if key_name:
                return value[key_name]
            return value

    def extract_case(self, yaml_name, key_name):
        case_value = self.read_case_yaml(yaml_name, key_name)[0]
        new_case = []
        for value in case_value['case_info']:
            new_case.append({"request_info": case_value["request_info"], "case_info": value})
        return new_case

    def write_extract_yaml(self, data):
        with open(self.yaml_path + "extract.yaml", mode='a', encoding='utf8') as f:
            old_value = self.read_extract_yaml()
            if old_value:
                for key, value in data.items():
                    old_value[key] = value
                self.clear_extract_yaml()
                yaml.dump(data=old_value, stream=f, allow_unicode=True, sort_keys=False)
            else:
                yaml.dump(data=data, stream=f, allow_unicode=True, sort_keys=False)
        # a 追加模式

    def clear_extract_yaml(self):
        with open(self.yaml_path + "extract.yaml", mode='w', encoding='utf8') as f:
            f.truncate()


yaml_util = YamlUtil()

if __name__ == '__main__':
    data = {'code2': 200, 'data': {'id': 87493333, 'address': '广东省广州市天河区车陂北街富力万科云启', 'signer_name': '江畔独步'}}
    yaml_util.write_extract_yaml(data)


