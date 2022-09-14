"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: dlocal_tax
@Site:
@time: 2022.06.23
"""
from demo.interface_config import domain
from utils import session

actual = {
    'VN': 10,
    'BR': 0.38,
    'CO': 0.4,
    'AR': 1.2,
}


def assert_dlocal_tax():
    url = domain + "/api/v1/merchant/config/country2currency"

    response = session.request("GET", url)
    country_list = response.json()['data']['data']
