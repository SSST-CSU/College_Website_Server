from django.shortcuts import render
from UserManagement.Authentication import AuthenticateUser
from Pages.models import *


def index(request):
    """
    主页
    :param request:
    :return:
    """
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

    # 登录
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        request.session['user_name'] = None

    # 轮播图片

    # 展示栏目
    displaycolumn = DisplayColumn.objects.filter(page__name='index').order_by('serial_number')
    col_len = displaycolumn.count()
    col_md = None
    if col_len == 0:
        displaycolumn = None
    elif col_len == 1:
        col_md = "col-md-12"
    elif col_len % 3 == 0:
        col_md = "col-md-4"
    elif col_len % 2 == 0:
        col_md = "col-md-6"
    elif col_len == 5 or col_len == 7:
        col_md = "col-md-12"

    return render(request, 'htmls/index.html', {
        "user": user,
        "navbar": navbar,
        "column": displaycolumn,
        "col_md": col_md,
    })
