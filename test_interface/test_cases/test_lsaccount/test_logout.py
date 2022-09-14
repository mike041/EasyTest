"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_logut
@Site:
@time: 2022.09.07
"""
import json

import pytest
import requests


def test_right_logut(token):
    url = "http://10.0.2.30:8039/common/v1/logout"

    payload = {}
    headers = token

    response = requests.request("POST", url, headers=headers, data=payload)

    assert json.loads(response.text)['code'] == 10000


if __name__ == '__main__':
    pytest.main()
