"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: page
@Site:
@time: 2022.05.14
"""


class BasePage:
    pass


# 官网
class OfficialPage(BasePage):
    experience_now = '立即体验'


class LoginPage(BasePage):
    name = '//*[@id="__layout"]/div/div/div[1]/div/div/form/div[1]/div/div/span/div/div/input'
    password = '//*[@id="__layout"]/div/div/div[1]/div/div/form/div[2]/div/div/span/div/div/span/input'
    login = '//*[@id="__layout"]/div/div/div[1]/div/div/form/div[4]/div/div/span/button'


class SignUpPage(BasePage):
    mail = '//*[@id="__layout"]/div/div/div[1]/div/div/form/div[1]/div[2]/div/span/input'
    password = '//*[@id="__layout"]/div/div/div[1]/div/div/form/div[2]/div[2]/div/span/span/input'
    password_confirm = '//*[@id="__layout"]/div/div/div[1]/div/div/form/div[3]/div[2]/div/span/span/input'
    sign_up = '创建账户'


class roe(BasePage):
    url = 'https://pre_sitebuilder.im30.net/preview/roe'
    avatar = '//*[@id="site-body"]/div[1]/div[1]/div/div[3]/div[4]/div[3]'
    email = '//*[@id="__layout"]/div/div[1]/div/div[2]/div/div[3]/div/form/div[2]/div/div/input'
    password = '//*[@id="__layout"]/div/div[1]/div/div[2]/div/div[3]/div/form/div[3]/div/div/input'
    login = '//*[@id="__layout"]/div/div[1]/div/div[2]/div/div[3]/div/form/div[4]/div/button'


class PaymentMethodsPage(BasePage):
    pay_list = 'pay-content'
