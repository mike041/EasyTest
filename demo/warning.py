"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: warning
@Site:
@time: 2022.06.23
"""
import time

import requests
import hashlib
import base64
import hmac


def warning(content):
    def gen_sign(_timestamp, secret):
        # 拼接_timestamp和secret
        string_to_sign = '{}\n{}'.format(_timestamp, secret)
        hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()

        # 对结果进行base64处理
        sign = base64.b64encode(hmac_code).decode('utf-8')
        return sign

    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/288c496c-d8d7-46a9-9159-3ba9d8f0a80a'
    key = 'gut4LhMtPZHa0p8KY9xeO'
    timestamp = int(time.mktime(time.localtime(time.time())))

    body = {
        "timestamp": timestamp,
        "sign": gen_sign(timestamp, key),
        "msg_type": "text",
        "content": {
            "text": content
        }
    }
    requests.post(url=url, json=body)


if __name__ == '__main__':
    content = {
        'code': -10000,
        'message': '报警了'
    }
    warning(str(content))
