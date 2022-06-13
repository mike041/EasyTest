"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: dlocal_pay_page
@Site:
@time: 2022.05.16
"""
import requests
import xlrd

li = [
    {'pay_type': 'CARD', 'country': 'BR'},
    {'pay_type': 'BANK_TRANSFER', 'country': 'BR'},
    {'pay_type': 'TICKET', 'country': 'BR'},
]


def parse_excel():
    path = 'E:\config.xls'
    data = xlrd.open_workbook(path)
    sheet = data.sheet_by_name('Sheet1')
    rows = list(sheet.get_rows())[1:]
    return rows


def pay_page(row):
    country = row[1].value
    pay_type = row[2].value
    name = bool(row[3].value)
    phone = bool(row[4].value)
    document = bool(row[5].value)
    city = bool(row[6].value)
    street = bool(row[7].value)
    number = bool(row[8].value)
    state = bool(row[9].value)
    zipcode = bool(row[10].value)
    document_name = row[11].value
    print(pay_type + country + "结果")
    url = "https://sandbox-xp.im30.net/api/v1/api_merchant/pay_center/payment_page_config?payment_method_type={}&country={}".format(
        pay_type, country)

    payload = {}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://kop.im30.net',
        'Referer': 'https://kop.im30.net/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    js = response.json()
    assert js['message'] == '成功'
    data = js['data']
    config = data['config']
    address = config['address']
    if not name == config['name']:
        print(name)
    if not phone == config['phone']:
        print('phone')
    if not document == config['document']:
        print('document')
    if not document_name == config['document_name']:
        print('document_name')
    if not city == address['city']:
        print('city')
    if not street == address['street']:
        print('street')
    if not number == address['number']:
        print('number')
    if not state == address['state']:
        print('state')
    if not zipcode == address['zipcode']:
        print('zipcode')



    print("==================================================================")


if __name__ == '__main__':
    for row in parse_excel():
        pay_page(row)
