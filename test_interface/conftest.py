"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: conftest.py
@Site:
@time: 2022.09.07
"""
import logging

import pytest

res_list = []

logger = logging.getLogger()


@pytest.fixture()
def setup_function(cache, req):
    # todo 处理请求
    logger.info('setup' + str(req))
    yield req
    if res_list:
        cache.set('id', res_list[-1])

