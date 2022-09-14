"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: sql
@Site:
@time: 2022.06.23
"""


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
