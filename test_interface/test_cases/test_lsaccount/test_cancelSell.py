"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_cancelSell
@Site:
@time: 2022.09.07
"""
import json

import allure
import requests

def test_noGoodsNo_cancelSell(token):
    url = "https://lsaccount.im30.net/api/v1/cancelSell"

    payload = {}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['data'] == 'need post goodsNo'


def test_wrongGoodsNo_cancelSell(token):
    url = "https://lsaccount.im30.net/api/v1/cancelSell"

    payload = {'goodsNo': '48555098'}

    response = requests.request("POST", url, headers=token, data=payload)

    assert json.loads(response.text)['msg'] == 'Item not found'


# todo 缺少可取消的商品
# def test_GoodsNo_cancelSell(token):
#     url = "https://lsaccount.im30.net/api/v1/cancelSell"
#
#     payload = {'goodsNo': '48555098'}
#
#     response = requests.request("POST", url, headers=token, data=payload)
#
#     assert json.loads(response.text)['msg'] == 'Item not found'
