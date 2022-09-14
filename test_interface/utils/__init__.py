"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: __init__.py
@Site:
@time: 2022.09.13
"""
import logging
import os


def generate_data_from_excel(file_name):
    path = os.path.join(os.curdir, file_name)
    req = Req()
    req.url = 'www.baidu.com'
    req.method = 'get'
    return [req, req, ]
    pass


def generate_data_from_database():
    pass


def generate_data():
    pass


class Req:
    def __init__(
            self,
            method=None,
            url=None,
            headers=None,
            files=None,
            data=None,
            params=None,
            auth=None,
            cookies=None,
            hooks=None,
            json=None,
            url_data=None,
            body_data=None,
            excepted=None,
            extract_variables=None):
        data = [] if data is None else data
        files = [] if files is None else files
        headers = {} if headers is None else headers
        params = {} if params is None else params
        url_data = {} if url_data is None else url_data
        body_data = {} if body_data is None else body_data
        excepted = {} if excepted is None else excepted
        extract_variables = {} if extract_variables is None else extract_variables
        # hooks = {} if hooks is None else hooks
        self.method = method
        self.url = url
        self.headers = headers
        self.files = files
        self.data = data
        self.json = json
        self.params = params
        self.auth = auth
        self.cookies = cookies
        self.url_datas = url_data
        self.body_datas = body_data

        pass
