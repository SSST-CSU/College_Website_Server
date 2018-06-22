from django.shortcuts import render
from UserManagement.Authentication import AuthenticateUser
from Pages.models import *
from ArticleManagement.models import ArchivalArticles, Article, ArticleStat


def article_page(request, id):
    """
    文章页
    :param request:
    :param id:
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

    # 文章
    article = None
    try:
        article = Article.objects.get(id=id)
    except:
        pass

    # 导航路径

    return render(request, 'htmls/articles.html', {
        "user": user,
        "navbar": navbar,
        "article": article,
    })
