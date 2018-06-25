from django.http import HttpResponseRedirect
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
        return HttpResponseRedirect('/')

    # 导航路径
    path = None
    if article is not None:
        path = article.get_article_route()

    return render(request, 'htmls/articles.html', {
        "user": user,
        "navbar": navbar,
        "article": article,
        "path": path,
    })


def columns_page(request, id):
    """
    栏目页
    :param request:
    :param name:
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

    # 栏目
    column = None
    try:
        column = Column.objects.get(id=id)
    except:
        return HttpResponseRedirect('/')

    # 栏目路径
    path = None
    if column is not None:
        path = column.get_column_route()

    # 获取子栏目
    sub_column = column.get_sub_column()
    if len(sub_column) == 0:
        sub_column = None

    # 获取栏目文章
    articles = ArchivalArticles.objects.filter(column=column)
    if len(articles) == 0:
        articles = None


    return render(request, 'htmls/columns.html', {
        "user": user,
        "navbar": navbar,
        "column": column,
        "path": path,
        "sub_column": sub_column,
        "articles": articles,
    })