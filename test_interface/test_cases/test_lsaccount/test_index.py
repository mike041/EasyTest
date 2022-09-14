"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_index
@Site:
@time: 2022.09.07
"""
import json

import requests


def test_login_index(token):
    url = "https://lsaccount.im30.net/common/v1/index"

    payload = {}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['data']['islogin'] is True


def test_notlogin_index():
    url = "https://lsaccount.im30.net/common/v1/index"

    payload = {}

    response = requests.request("POST", url, data=payload)

    assert json.loads(response.text)['data']['islogin'] is False
