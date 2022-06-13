"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: xsolla
@Site:
@time: 2022.05.11
"""
import json
import time

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create your views here.

count = 0


def xsolla(request):
    notification_type = request.POST['notification_type']
    user = request.POST['user']
    user_id = user['id']

    if notification_type == 'user_validation':
        if user_id == '888688008998':
            body = {"data": {}, "http_status_code": 200, "message": "OK"}
        else:
            body = {"data": {}, "error": {"code": "INVALID_USER", "message": "INVALID_USER"}, "http_status_code": 400,
                    "message": "INVALID_USER"}
    elif notification_type == 'payment':
        body = {"data": {}, "http_status_code": 200, "message": "OK"}
    return JsonResponse(status=400, data=body)


def mode(request):
    notification_type = json.loads(request.body).get('notification_type')
    if notification_type == 'user_validation':

        body = {"code": 1, "data": {
            "user": {"id": "399669008998", "level": 25, "merchant_id": 50, "name": "Zeybek787159_89985272",
                     "project_id": 123, "server": "8998"}}, "message": "success"}

        return JsonResponse(status=200, data=body)
    elif notification_type == 'payment':
        print("++++++++++++++++++++++++"+time.ctime())
        global count
        count += 1
        if count > 4:
            body = {
                'http_status_code': 200,
                'data': {'count': count},
                'message': 'success'
            }
        else:
            body = {
                'http_status_code': 500,
                'data': {'count': count},
                'message': 'false'
            }
        return JsonResponse(status=200, data=body)

    return HttpResponse(status=502)
