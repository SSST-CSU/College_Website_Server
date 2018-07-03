from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from UserManagement.Authentication import AuthenticateUser
from Pages.models import *


def user_center(request):
    # 登录
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        return HttpResponseRedirect('/')
    # 未登录
    if user is None:
        return HttpResponseRedirect('/login')

    # 导航栏
    navbarobj = NavbarObject.objects.filter(page__name='index').order_by('serial_number')
    navbar = []
    num = 0
    for nav in navbarobj:
        if nav.serial_number - int(nav.serial_number) == 0:
            navbar.append({
                "len": 1,
                "val": [nav],
            })
            num += 1
        else:
            num -= 1
            try:

                navbar[num]["val"].append(nav)
                navbar[num]["len"] += 1
            except:
                navbar.append({
                    "len": 0,
                    "val": [],
                })
                navbar[num]["val"].append(nav)
                navbar[num]["len"] += 1
            num += 1

    return render(request, 'htmls/user_center/user_center.html', {
        "user": user,
        "navbar": navbar,
    })


def user_center_articles(request):
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        return HttpResponseRedirect('/')
    # 未登录
    if user is None:
        return HttpResponseRedirect('/login')
    return render(request, 'htmls/user_center/user_center_articles.html', {
        "user": user,
    })


def user_center_home(request):
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        return HttpResponseRedirect('/')
    # 未登录
    if user is None:
        return HttpResponseRedirect('/login')
    return render(request, 'htmls/user_center/user_center_home.html', {
        "user": user,
    })


def user_center_pages(request):
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        return HttpResponseRedirect('/')
    # 未登录
    if user is None:
        return HttpResponseRedirect('/login')
    return render(request, 'htmls/user_center/user_center_pages.html', {
        "user": user,
    })


def user_center_users(request):
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        return HttpResponseRedirect('/')
    # 未登录
    if user is None:
        return HttpResponseRedirect('/login')
    return render(request, 'htmls/user_center/user_center_users.html', {
        "user": user,
    })


def user_center_meetingroom(request):
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        return HttpResponseRedirect('/')
    # 未登录
    if user is None:
        return HttpResponseRedirect('/login')
    return render(request, 'htmls/user_center/user_center_meetingroom.html', {
        "user": user,
    })