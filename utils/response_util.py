import json
from core.ResultBase import ResultResponse
from utils.log_util import logger


def process_response(response):
    if response.status_code == 200 or response.status_code == 201:
        ResultResponse.success = True
        ResultResponse.body = response.json()
    else:
        logger.info("接口返回状态码不是2开头，请检查")
    logger.info("接口返回参数>>>\n{}".format(json.dumps(response.json(), ensure_ascii=False, indent=2)))
    return ResultResponse
