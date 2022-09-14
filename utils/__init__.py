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
import xlrd
import xlwings

from utils.session import MerchantSess, MallSess


# 在response中提取参数, 并放到列表中
def get_extract(extract_dict, res):
    for key, value in extract_dict.items():
        key_value = get_param(key, res)
        extract_dict[key] = key_value


# 替换内容中的变量, 返回字符串型
def replace_var(content, var_name, var_value):
    if not isinstance(content, str):
        content = json.dumps(content)
    var_name = "$" + var_name
    content = content.replace(str(var_name), str(var_value))
    return content


# 从内容中提取所有变量名, 变量格式为$variable,返回变量名list
def extract_variables(content):
    variable_regexp = r"\$([\w_]+)"
    if not isinstance(content, str):
        content = str(content)
    try:
        return re.findall(variable_regexp, content)
    except TypeError:
        return []


# 在内容中获取某一参数的值
def get_param(param, content):
    param_val = None
    if isinstance(content, str):
        # content = json.loads(content)
        try:
            content = json.loads(content)
        except:
            content = ""
    if isinstance(content, dict):
        param_val = get_param_reponse(param, content)
    if isinstance(content, list):
        dict_data = {}
        for i in range(len(content)):
            try:
                dict_data[str(i)] = eval(content[i])
            except:
                dict_data[str(i)] = content[i]
        param_val = get_param_reponse(param, dict_data)
    if param_val is None:
        return param_val
    else:
        if "$" + param == param_val:
            param_val = None
        return param_val


def get_param_reponse(param_name, dict_data, default=None):
    for k, v in dict_data.items():
        if k == param_name:
            return v
        else:
            if isinstance(v, dict):
                ret = get_param_reponse(param_name, v)
                if ret is not default:
                    return ret
            if isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        ret = get_param_reponse(param_name, i)
                        if ret is not default:
                            return ret
                    else:
                        pass
    return default


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


def parse_excel(path, sheet_index_name=0):
    data = xlrd.open_workbook(path)

    if isinstance(sheet_index_name, int):
        sheet = data.sheet_by_index(sheet_index_name)
    else:
        sheet = data.sheet_by_name(sheet_index_name)
    rows = list(sheet.get_rows())[1:]
    return rows
