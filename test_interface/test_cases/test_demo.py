"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_demo
@Site:
@time: 2022.08.30
"""
import json
import logging
import os
import sys

import pytest

from test_interface import utils

logger = logging.getLogger()

data = [1, 2, 3]


#
# @pytest.fixture(params=['你好啊', '哈哈哈哈'])
# def fix(request):
#     return request.param
#
#
# @pytest.fixture()
# def setup_function(request):
#     return request.param
#
#
# @pytest.mark.parametrize('setup_function', ['lala'], indirect=True)
# def test_1(cache, setup_function):
#     cache.set("new", 'dsd')
#     logger.info(setup_function)


@pytest.fixture(params=utils.generate_data_from_excel('test_2'))
def req(request):
    logger.info(request.param)
    return request.param


def test_2(setup_function):
    logger.info('test_2' + str(setup_function))
    pass


@pytest.fixture
def fixt(request):
    marker = request.node.get_closest_marker("fixt_data")
    if marker is None:
        # Handle missing marker in some way...
        data = None
    else:
        data = marker.args[0]

    # Do something with the data
    return data


@pytest.mark.fixt_data(42)
def test_1(fixt):
    print(fixt)
    pass


if __name__ == '__main__':
    pytest.main(['-k', 'demo'])
    # path = os.path.join(os.getcwd(), 'test_demo.py')
    # os.system(f'pytest {path} --cache-clear')
