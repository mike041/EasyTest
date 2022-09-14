"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: xsolla_country_tax
@Site:
@time: 2022.05.26
"""

from utils import MallSess
from django.db import connection
from demo.interface_config import domain


def assert_xsolla_tax():
    url = domain + "/api/v1/merchant/config/country2currency"
    session = MallSess().sess
    response = session.request("GET", url)
    country_list = response.json()['data']['data']
    actual_map = {}
    for country in country_list:
        tax = country['tax']
        currency_name = country['currency_name']
        actual_map[currency_name] = tax
    with connection.cursor() as cursor:
        # 执行sql语句
        cursor.execute("SELECT country,tax_rate FROM xsolla_country_tax")
        # 查出一条数据
        rows = cursor.fetchall()
        for row in rows:
            country = row[0]
            tax_rate = row[1]
            printme(actual_map, country, tax_rate)

        # 查出所有数据
        # row = cursor.fetchall()


def printme(actual_map, country, tax_rate):
    print("11")
    if country not in actual_map:
        print(country + "不存在")

    elif str(int(actual_map[country] * 100)) == tax_rate:
        pass
    else:
        print("国家:" + country + "实际税:" + str(actual_map[country] * 100) + "预期税:" + str(tax_rate))


if __name__ == '__main__':
    assert_xsolla_tax()
