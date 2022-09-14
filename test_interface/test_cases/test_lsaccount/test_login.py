"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_login
@Site:
@time: 2022.09.07
"""
import json
import logging
import os
import sys

import pytest
import requests

logger = logging.getLogger()


def test_right_login():
    url = "https://lsaccount.im30.net/common/v1/login"

    payload = {'email': 'sh7440muod410@126.com',
               'pass': 'ZY199577'}

    response = requests.request("POST", url, data=payload)
    assert json.loads(response.text)['code'] == 10000


def test_no_password_login():
    url = "https://lsaccount.im30.net/common/v1/login"

    payload = {'email': 'sh7440muod410@126.com', }
    files = [

    ]

    response = requests.request("POST", url, data=payload, files=files)

    assert json.loads(response.text)['code'] != 10000


def test_no_email_login():
    url = "https://lsaccount.im30.net/common/v1/login"

    payload = {'pass': 'ZY199577'}

    response = requests.request("POST", url, data=payload)

    assert json.loads(response.text)['code'] != 10000


def test_wrong_password_login():
    url = "https://lsaccount.im30.net/common/v1/login"

    payload = {'email': 'sh7440muod410@126.com',
               'pass': 'ZY1995'}

    response = requests.request("POST", url, data=payload)

    assert json.loads(response.text)['code'] != 10000


def params():
    names = 'email,passw'
    parmas_list = [('sh7440muod410@126.com', 'ZY1995'), ('sh7440muod410@126.com', ''), ('', 'ZY1995'),
                   pytest.param('sh7440muod410@126.com', 'ZY199577', marks=pytest.mark.xfail)]
    return names, parmas_list


@pytest.mark.parametrize(*params())
def test_params_login(email, passw):
    url = "https://lsaccount.im30.net/common/v1/login"

    payload = {'email': email,
               'pass': passw}
    logger.info(payload)
    response = requests.request("POST", url, data=payload)
    logger.info(response.text)
    assert json.loads(response.text)['code'] != 10000


class MockResponse:
    def get_json(self):
        return {'code': 10000}


def test_mock(monkeypatch):
    def mock_request():
        return MockResponse()

    monkeypatch.setattr(requests, 'request', mock_request)

    response = requests.request()
    assert response.get_json()['code'] == 10000


def test_set_glo_var(global_var):
    global_var['key'] = 100


def test_glo_var(global_var):
    assert global_var['key'] == 100


if __name__ == '__main__':
    pass
