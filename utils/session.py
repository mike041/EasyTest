"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: session
@Site:
@time: 2022.06.23
"""
import json

from requests import Session

from demo.interface_config import domain, site_id, merchant_name, merchant_password, mall_domain, mall_name, \
    mall_password


class MerchantSess:
    def __init__(self):
        self.sess = Session()
        url = domain + "/api/v1/merchant/user/login"

        payload = {"email": merchant_name, "password": merchant_password, "rememberMe": False}
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': domain,
            'Referer': domain + '/login',
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


class MallSess():
    def __init__(self):
        self.sess = Session()
        url = mall_domain + "/api/v1/api_customer/login"

        payload = {"email": mall_name, "password": mall_password, 'site_id': site_id}
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': mall_domain,
            'Referer': mall_domain + '/preview/roe',
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

# session = MerchantSess()
# mall_session = MallSess()
