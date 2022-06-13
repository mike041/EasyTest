"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: __init__.py
@Site:
@time: 2022.05.26
"""
import json
import re
from decimal import Decimal

import requests
import xlwings as xlwings

from requests import Session

from utils.interface_config import domin, merchant_id, merchant_name, merchant_password


def my_sql():
    from django.db import connection
    cursor = connection.cursor()
    # 执行sql语句
    cursor.execute("SELECT tax_rate FROM xsolla_canada_tax")
    # 查出一条数据
    row = cursor.fetchall()
    print(row)
    # 查出所有数据
    # row = cursor.fetchall()


# 获取国家缩写表并保存
def get_country_comparison_table():
    app = xlwings.App(visible=False, add_book=False)
    book = app.books.add()
    sht = book.sheets.active
    h = requests.get('https://yumingsuoxie.bmcx.com/').text
    reg = re.compile('<tr>(.*?)</tr>', re.S)
    li = re.findall(reg, h)
    for i in range(len(li)):
        reg = re.compile('<td>(.*?)</td>')
        tds = re.findall(reg, li[i])
        sht.range((i + 1, 1)).value = tds
    book.save('test_excel.xlsx')
    app.quit()


def decimal_two(num):
    return Decimal(num).quantize(Decimal('0.00')).__float__()


def json_parse(js: dict, key: str = None):
    _js = js
    if not key:
        return _js
    keys = key.split('.')
    for k in keys:
        if k.isdigit():
            k = int(k)
        _js = _js[k]
    return _js


class Sess:
    def __init__(self):
        self.sess = Session()
        url = domin + "/api/v1/merchant/user/login"

        payload = {"email": merchant_name, "password": merchant_password, "rememberMe": False}
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': domin,
            'Referer': domin + '/login',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }

        response = self.sess.request("POST", url, headers=headers, data=json.dumps(payload))
        js = response.json()
        if js['code'] == 1:
            authorization = response.headers['Authorization']
            self.sess.headers['Authorization'] = authorization
            self.sess.headers['Cookie'] = 'im30-pay-token=' + authorization


session = Sess().sess
