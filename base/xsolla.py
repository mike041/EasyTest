"""
@version: python 3.6.3
@author: xiaomai
@software: PyCharm
@file: xsolla
@Site:
@time: 2022.05.11
"""
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse


# Create your views here.


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
