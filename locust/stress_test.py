import queue

from locust import HttpUser, task, between, TaskSet
from user_config import user_ids

host = 'http://10.0.2.30:8088'
url = "/gameservice/getserverbyname.php"
querystring = {"name": "", "lang": "zh_Hans"}
querystrin2 = {"name": "", "code": "888888", "captcha": "4af3ddf",
               "id": "ac540598-f127-404d-8d0f-749eba5e9d23",
               "lang": "en"}

headers = {
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Connection': "keep-alive",
    'Cookie': "PHPSESSID=3kjtfaahukdrvh99t1j933gu83",
    'Referer': "http://10.0.2.30:8088/",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    'X-Requested-With': "XMLHttpRequest",
    'cache-control': "no-cache",
    'Postman-Token': "086b29a6-ecf9-493e-a5d3-aba99eaf43a4"
}


class Task(TaskSet):
    def on_start(self):
        self.i = 0
        try:
            self.data = self.user.user_data.get()
            querystring['name'] = self.data
            querystrin2['name'] = self.data
            print(querystring)
        except queue.Empty:
            print('no data exist')
            exit(0)

    @task(1)
    def get_gift(self):
        # with self.client.get(url,
        #                      name="角色校验", params=querystring, headers=headers, catch_response=True) as response:
        #     assert_http(response)
        #     print(response.status_code)

        with self.client.get("http://10.0.2.30:8088/gameservice/code.php",
                             name="角色校验", params=querystrin2, headers=headers, catch_response=True) as response:
            assert_http(response)
            print(response.text)

        self.i += 1


def assert_http(response):
    """断言"""
    if response.status_code == 200:
        response.success()
    else:
        response.failure(f'status_code:{response.status_code} != 200')


class User(HttpUser):
    wait_time = between(1, 2.5)
    min_wait = 3000
    max_wait = 6000
    host = host
    tasks = [Task]
    user_data = queue.Queue()

    for id in user_ids:
        user_data.put_nowait(id)
