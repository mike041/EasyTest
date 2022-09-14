"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: Dynamically_generate_cases
@Site:
@time: 2022.06.24
"""
import json
import logging

import pytest
import requests

import utils

import logging

log = logging.getLogger(__name__)

data = [['get', 'https://www.baidu.com', True], ['get', 'https://www.sohu.com', False], ]

extract_dict = {}
step_json = []

original_requests = []


@pytest.fixture(params=data, scope='session')
def cases(request):
    return request.param


def test(cases):
    res = requests.request(method=cases[0], url=cases[1])
    if cases[2]:
        pytest.skip("设置为skip")
    assert res.status_code == 200


if __name__ == '__main__':
    extract_dict = {"id": "343843008998", "email": "roe@roe.com", "name": "Wonder-FARM7579_89981570",
                    "document": "57637464148"}
    replace('{"id":$id,"email":$email,"name":$name,"document":$document}',
            extract_dict)
    pass
