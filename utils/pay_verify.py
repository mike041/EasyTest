import im30.pay_verify
import json
from im30.util import decimal_two
import jsonpickle
from im30 import session

tax_rate_config = {
    'VN': 0.1,
    'BR': 0.0038,
    'CO': 0.0040,
    'AR': 0.012
}

platform_handling_fee_config = {
    'BR_CARD': [0.035, 0.00],
    'BR_BANK_TRANSFER': [0.025, 0.2],
    'BR_TICKET': [0.024, 0.2],
    'BR_Wallet': [0.00, 0.00],
    'BR_OTHER': [0.00, 0.00],
    'ID_CARD': [0.035, 0.15],
    'ID_BANK_TRANSFER': [0.025, 0.00],
    'ID_TICKET': [0.021, 0.35],
    'ID_Wallet': [0.039, 0.00],
    'ID_OTHER': [0.00, 0.00],
    'IN_CARD': [0.033, 0.00],
    'IN_BANK_TRANSFER': [0.030, 0.00],
    'IN_TICKET': [0.00, 0.00],
    'IN_Wallet': [0.030, 0.00],
    'IN_OTHER': [0.025, 0.00],
    'PH_CARD': [0.035, 0.15],
    'PH_BANK_TRANSFER': [0.025, 0.25],
    'PH_TICKET': [0.028, 0.25],
    'PH_Wallet': [0.034, 0.00],
    'PH_OTHER': [0.00, 0.00],
    'MX_CARD': [0.030, 0.10],
    'MX_BANK_TRANSFER': [0.028, 0.20],
    'MX_TICKET': [0.037, 0.00],
    'MX_Wallet': [0.00, 0.00],
    'MX_OTHER': [0.00, 0.00],
    'CL_CARD': [0.035, 0.00],
    'CL_BANK_TRANSFER': [0.030, 0.00],
    'CL_TICKET': [0.030, 0.00],
    'CL_Wallet': [0.00, 0.00],
    'CL_OTHER': [0.00, 0.00],
    'CO_CARD': [0.030, 0.00],
    'CO_BANK_TRANSFER': [0.028, 0.20],
    'CO_TICKET': [0.035, 0.00],
    'CO_Wallet': [0.00, 0.00],
    'CO_OTHER': [0.00, 0.00], }


class Payment:
    def __init__(self, payment_id=None, order_id=None, country=None, exchange_rate=None, amount=None,
                 final_merchant_amount=None,
                 im30pay_handling_fee=None, platform_handling_fee=None, taxes_value=None,
                 us_amount=None, us_final_merchant_amount=None, us_dlocal_handling_fee=None,
                 us_im30pay_handling_fee=None,
                 us_platform_handling_fee=None, us_taxes_value=None, payment_method_type=None, with_tax=0,
                 platform_type='Dlocal'):
        self.payment_id = payment_id
        self.order_id = order_id
        self.country = country
        self.exchange_rate = exchange_rate
        self.amount = amount
        self.final_merchant_amount = final_merchant_amount
        self.im30pay_handling_fee = im30pay_handling_fee
        self.platform_handling_fee = platform_handling_fee
        self.taxes_value = taxes_value
        self.us_amount = us_amount
        self.us_final_merchant_amount = us_final_merchant_amount
        self.us_dlocal_handling_fee = us_dlocal_handling_fee
        self.us_im30pay_handling_fee = us_im30pay_handling_fee
        self.us_platform_handling_fee = us_platform_handling_fee
        self.us_taxes_value = us_taxes_value
        self.payment_method_type = payment_method_type
        self.with_tax = with_tax
        self.platform_type = platform_type

    def assert_payment(self):
        self.judge_tax()
        self.judge_platform()
        self.judge_final_merchant_amount()

    def judge_final_merchant_amount(self):
        expect = decimal_two(self.amount - self.platform_handling_fee - self.taxes_value)
        try:
            assert expect == self.final_merchant_amount
        except AssertionError as e:
            print(str(self.payment_id) + "=====final_merchant_amount===" + str(e))

    def judge_platform(self):
        assert self.us_platform_handling_fee == self.us_dlocal_handling_fee + self.us_im30pay_handling_fee

        key = platform_handling_fee_config.get(self.country + '_' + self.payment_method_type)
        if not key:
            print('支付方式不存在')
        rate = key[0]
        base = key[1]
        tax = decimal_two(self.amount * rate + base * self.exchange_rate)

        try:
            assert tax == self.platform_handling_fee
        except AssertionError as e:
            print(str(self.payment_id) + "=====platform_handling_fee===" + str(e))

    def judge_tax(self):
        def __get_tax(amount, _rate):
            if self.with_tax:
                tax = amount / (1 + _rate) * _rate
            else:
                tax = amount * _rate
            return decimal_two(tax)

        if tax_rate_config.get(self.country):
            rate = tax_rate_config.get(self.country)
        else:
            rate = 0.00
        expect_tax = __get_tax(self.amount, rate)
        try:
            assert expect_tax == self.taxes_value
        except AssertionError as e:
            print(str(self.payment_id) + "=====taxes_value===" + str(e))


def query_payment(payment_id):
    url = 'https://pre_xp.im30.net/api/v1/merchant/pay/payment-intent/{}'.format(payment_id)
    response = session.request("GET", url)
    js = response.json()
    data = js['data']
    data["py/object"] = f'{Payment.__module__}.{Payment.__name__}'
    data['payment_id'] = payment_id
    data['with_tax'] = 0
    data['platform_type'] = 'Dlocal'

    result = json.dumps(data)
    return jsonpickle.decode(result, safe=True)


def exchange(amount, exchange_rate):
    return decimal_two(float(amount) / float(exchange_rate))


def query_payments():
    url = "https://pre_xp.im30.net/api/v1/merchant/pay/payment-intents"

    querystring = {"pageNo": "1", "payment_id": "",
                   "local_tz": "-480", "pageSize": "50"}
    res = session.request('GET', url, params=querystring)
    result_list = [i.get('_id') for i in res.json()['data']['data']]
    return result_list


if __name__ == '__main__':
    pay = query_payment('62652ac1934bec242a370ea8')
    pay.assert_payment()
# list = query_payments()
# for i in list:
#     create_payment(i).assert_payment()
