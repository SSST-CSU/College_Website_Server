from django.http import HttpResponse
from django.shortcuts import render
from UserManagement.models import User
import json


def login(request):
    id = request.POST['user_id']
    pwd = request.POST['user_pwd']
    msg = 0
    try:
        user = User.objects.get(id=id)
        if pwd == user.pwd:
            msg = 2
            request.session['user_id'] = user.id
            request.session['user_pwd'] = user.pwd
        else:
            msg = 1
    except:
        msg = -1
    ret = {
        "msg": msg
    }
    return HttpResponse(json.dumps(ret))


def logout(request):
    id = request.POST['user_id']
    msg = 0
    try:
        user = User.objects.get(id=id)
        request.session['user_id'] = None
        request.session['user_pwd'] = None
        msg = 1
    except:
        pass
    ret = {
        "msg": msg
    }
    return HttpResponse(json.dumps(ret))
