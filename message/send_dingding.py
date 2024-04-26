import os

import requests
from jenkins import Jenkins

Jenkins_url = "http://192.168.0.124:8080/"
server = Jenkins(Jenkins_url, username='root', password='taowanting')
job_name = "job/TestMeike"
job_url = server.get_info(job_name)['url']
job_last_number = server.get_info(job_name)['lastBuild']['number']
report_url = job_url + str(job_last_number) + '/allure'


def push_message():
    content = {}
    file_path = os.path.dirname(os.getcwd())
    file_path = file_path.replace("\\", "/") + '/allure-report/export/prometheusData.txt'
    f = open(file_path)
    for line in f.readlines():
        launch_name = line.strip('\n').split(' ')[0]
        num = line.strip('\n').split(' ')[1]
        content.update({launch_name: num})
    f.close()
    passed_num = content['launch_status_passed']
    failed_num = content['launch_status_failed']
    broken_num = content['launch_status_broken']
    skipped_num = content['launch_status_skipped']
    case_num = content['launch_retries_run']

    # 钉钉消息发送
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=759a0e968564350ceed4c9d9eee5c74fbf5a50d9bf92eb46afd9a825e83fa68c"
    content = {
        "msgtype": "text",
        "text": {
            "content": "接口自动化脚本执行结果：\n运行总数" + case_num
                       + "\n通过数量：" + passed_num
                       + "\n失败数量：" + failed_num
                       + "\n阻塞数量：" + broken_num
                       + "\n跳过数量：" + skipped_num
                       + "\n构建地址：\n" + job_url
                       + "\n报告地址：\n" + report_url
        }
    }
    requests.post(url=webhook, json=content, verify=False)


if __name__ == '__main__':
    push_message()
