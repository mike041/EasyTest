"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: testwebsocket
@Site:
@time: 2022.07.13
"""
import json
import threading
import time

from websocket import WebSocketApp

path = 'wss://premind.im30.net'
token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVSUQiOiI4cDV0dHdjeXUzZnN6Z2ppXzZmOHVvZ2JvaGpiZHprZjMiLCJQbGF0Zm9ybSI6IldlYiIsImV4cCI6MTk3NzM3NDg5OCwibmJmIjoxNjYyMDE0ODk4LCJpYXQiOjE2NjIwMTQ4OTh9.UncCYpH2IIi_O8ZypkttmgTiSgmHtokXQNtYDWpSFhg'
user_id = '8p5ttwcyu3fszgji_6f8uogbohjbdzkf3'
group_id = '1244418569'
receive_id = ''


class MindWebSocket(WebSocketApp):
    def on_message(ws, message):
        ms = json.loads(message)
        print('on_message------' + message)
        event = ms['event']
        errCode = ms['errCode']
        data = ms['data']
        if event == 'CreateTextMessage' and errCode == 0:
            send(ws, receive_id, group_id, data)

    def on_open(ws):
        th = threading.Thread(name='t1', target=auto_send_meaasge, args=(ws,))
        th.start()

    def on_error(ws, error):
        print(error)

    def on_close(ws, close_status_code, close_msg):
        print('已关闭')

    # 心跳检查,保持websocket链接状态
    def on_ping(ws, message):
        print("Got a Ping:")
        print(message)

    def on_pong(ws, message):
        print("Got a Pong:")
        print(message)

    def __init__(self, user_id, url, token=None, on_error=on_error, on_close=on_close, on_open=on_open,
                 on_message=on_message, on_ping=on_ping, on_pong=on_pong):
        self.user_id = user_id
        self.token = token
        super(MindWebSocket, self).__init__(url,
                                            header=None,
                                            on_open=on_open,
                                            on_message=on_message,
                                            on_error=on_error,
                                            on_close=on_close,
                                            on_ping=on_ping, on_pong=on_pong,
                                            on_cont_message=None,
                                            keep_running=True,
                                            get_mask_key=None,
                                            cookie=None,
                                            subprotocols=None,
                                            on_data=None,
                                            socket=None)


# 手动交互发消息
def create_message(ws):
    while True:
        time.sleep(1)
        message = structure_message(reqFuncName='CreateTextMessage', userID=ws.user_id, data=input('发送的消息是：'))
        ws.send(message)


# 自动发消息
def auto_send_meaasge(ws):
    for i in range(100):
        time.sleep(2)
        message = structure_message(reqFuncName='CreateTextMessage', userID=ws.user_id, data=i)
        print("auto_send_meaasge--------" + message)
        ws.send(message)


def structure_message(reqFuncName, userID, data):
    t = int(time.time())
    if isinstance(data, dict):

        data = json.dumps(data)
    _message = {"reqFuncName": reqFuncName,
                "operationID": "d8ln55b19t" + str(t) + userID,
                "userID": userID, "data": str(data)}
    print("structure_message--------" + json.dumps(_message))
    return json.dumps(_message)


def send(ws, recvID, groupID, message):
    data_json = {
        "recvID": recvID,
        "groupID": groupID,
        "offlinePushInfo": "{\"title\":\"你收到一条新消息\",\"desc\":\"\",\"ex\":\"\",\"iOSPushSound\":\"+1\",\"iOSBadgeCount\":true}",
        "message": message
    }

    _message = structure_message('SendMessage', user_id, json.dumps(data_json))
    print("send--------" + _message)
    ws.send(_message)


def dispatch(ws, type):
    if type == 'create_message':
        create_message(ws)
    elif type == 'auto_send_meaasge':
        auto_send_meaasge(ws)


if __name__ == '__main__':
    user = MindWebSocket(user_id, url=f'{path}/ws/web?sendID={user_id}&token={token}&platformID=5')
    user.run_forever()
