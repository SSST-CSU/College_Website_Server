from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from UserManagement.Authentication import AuthenticateUser
from Pages.models import *
from ArticleManagement.models import *


def user_center_articles_edit(request):
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
    return render(request, 'htmls/user_center/articles/user_center_articles_edit.html', {
        "user": user,
    })


def user_center_articles_edit_id(request, id):
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

    # 获取文章
    article = None
    try:
        article = Article.objects.get(id=id)
    except:
        pass

    return render(request, 'htmls/user_center/articles/user_center_articles_edit.html', {
        "user": user,
        "article": article,
    })
