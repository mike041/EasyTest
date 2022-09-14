"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_mySellList
@Site:
@time: 2022.09.07
"""
import json

import requests


def test_all_mySellList(token):
    url = "https://lsaccount.im30.net/api/v1/mySellList"

    payload = {'searchType': '0',
               'page': '1'}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['code'] == 10000


def test_publicity_mySellList(token):
    url = "https://lsaccount.im30.net/api/v1/mySellList"
    payload = {'searchType': '1',
               'page': '1'}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['code'] == 10000


def test_selling_mySellList(token):
    url = "https://lsaccount.im30.net/api/v1/mySellList"
    payload = {'searchType': '2',
               'page': '1'}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['code'] == 10000


def test_besold_mySellList(token):
    url = "https://lsaccount.im30.net/api/v1/mySellList"
    payload = {'searchType': '3',
               'page': '1'}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['code'] == 10000
