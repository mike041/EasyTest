"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_userinfo
@Site:
@time: 2022.09.07
"""
import json

import requests


def test_userinfo(token, user):
    url = "https://lsaccount.im30.net/api/v1/userinfo"

    payload = {}
    files = {}

    response = requests.request("POST", url, headers=token, data=payload, files=files)

    assert json.loads(response.text)['data']['email'] == user['email']
