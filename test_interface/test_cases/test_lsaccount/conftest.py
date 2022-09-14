"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: conftest.py
@Site:
@time: 2022.09.07
"""
import json

import pytest
import requests

glo_var = {}

HOST = 'https://lsaccount.im30.net'

@pytest.fixture()
def global_var():
    return glo_var


user = {'email': 'sh7440muod410@126.com',
        'pass': 'ZY199577'}


@pytest.fixture(scope='session', autouse=True)
def token():
    url = HOST + "/common/v1/login"
    response = requests.request("POST", url, data=user)

    assert json.loads(response.text)['code'] == 10000

    headers = {
        'Cookie': response.headers['Set-Cookie']
    }
    yield headers
    url = HOST + "/common/v1/logout"

    requests.request("POST", url, headers=headers)


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
