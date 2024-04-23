import pytest
from core.ApiService import api_service
from utils.YamlUtil import yaml_util


@pytest.fixture(scope='session')
def login_token():
    data = yaml_util.extract_case('user_center.yaml', 'user_login')
    result = api_service.handle_case(data[0])
    headers = {
        "Authorization": "JWT " + result['token']
    }
    return headers

