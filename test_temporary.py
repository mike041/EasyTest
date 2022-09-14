"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: test_temporary
@Site:
@time: 2022.06.29
"""
import requests

url = "https://premind.im30.net/api/doc/create"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': 'Hm_lvt_0e5ab9a0b378a78b7969a1abcf6bf68c=1656471748; docSessionID=s.c18d81b1da32b4dc2845b776795e2302; token=t.2dq7vyFcsZk10dGdfA8C; prefs={%22showLineNumbers%22:false%2C%22comments%22:true}; Hm_lpvt_0e5ab9a0b378a78b7969a1abcf6bf68c=1656474817; MINDTOKEN=m5r2SQVQs_L-6cNi8lYHYGZ226KckR281xLj4yMZ-2yt4z5svRIeNXNGl9V-BiLb; MINDTEAMID=13; MINDUSERID=8p5ttwcyu3fszgji; home_mind_token=m5r2SQVQs_L-6cNi8lYHYGZ226KckR281xLj4yMZ-2yt4z5svRIeNXNGl9V-BiLb; sessionid=91cax7bgutnitfdrmq5ji613oy; user_mind_name=xiaomai; MINDIMTOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiI4cDV0dHdjeXUzZnN6Z2ppXzZmOHVvZ2JvaGpiZHprZjMiLCJQbGF0Zm9ybSI6IldlYiIsImV4cCI6MTk3MTgzNDgzMCwibmJmIjoxNjU2NDc0ODMwLCJpYXQiOjE2NTY0NzQ4MzB9.ywa-REAeql4fGl4uNTB6FSBXxsFtcsRhTTI9Jyjramw; MINDIMUSERID=8p5ttwcyu3fszgji_6f8uogbohjbdzkf3; MINDTOKEN=3nDOewSOMEYfdxi1aO131K6qwrnoOFtQ4Mwyd3c4bBz_eYZrbkXTvpWO4beEk6qi; MINDTEAMID=5; MINDUSERID=ahorzam3ypfa9xyw; home_mind_token=3nDOewSOMEYfdxi1aO131K6qwrnoOFtQ4Mwyd3c4bBz_eYZrbkXTvpWO4beEk6qi; sessionid=hdkrw7doipdg3cfbkysztfgw5o; user_mind_name=%E5%B0%8F%E9%BA%A6; MINDIMTOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiJhaG9yemFtM3lwZmE5eHl3X2dpOTRjbnM0YjM4d3RjejUiLCJQbGF0Zm9ybSI6IldlYiIsImV4cCI6MTk3MTg0NTQ1OCwibmJmIjoxNjU2NDg1NDU4LCJpYXQiOjE2NTY0ODU0NTh9.EkBuocEvyoIF-jnOE4Z-pfpXhhoSdMmtZh9xbhKuP0g; MINDIMUSERID=ahorzam3ypfa9xyw_gi94cns4b38wtcz5',
    'Origin': 'https://premind.im30.net',
    'Referer': 'https://premind.im30.net/drive/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'team-id': '13',
    'x-token': 'm5r2SQVQs_L-6cNi8lYHYGZ226KckR281xLj4yMZ-2yt4z5svRIeNXNGl9V-BiLb'
}

if __name__ == '__main__':
    for i in range(15, 30):
        title = 'test' + str(i)

        payload = "{\"title\":\"" + title + "\"}"

        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
