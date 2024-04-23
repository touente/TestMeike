from api.api import mk
from utils.read_util import base_data


def login():
    json_data = base_data.read_data()['login']
    result = mk.login(json_data)
    return json_data['username'], result.body['token']
