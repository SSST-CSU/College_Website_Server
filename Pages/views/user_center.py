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


def user_center_laboratory(request):
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

    # 获取所有申请记录
    from ResourceBorrowingSystem.models import LaboratoryBorrowingApply, AdminUser
    apply_record = LaboratoryBorrowingApply.objects.get_all_apply_by_user(user)

    # 查询是否有管理员权限
    from UserManagement.models.User_Duty import User_Duty
    duties = User_Duty.objects.filter(user=user).values_list('duty')
    admin_queryset = AdminUser.objects.none()
    for duty in duties:
        admin_queryset = admin_queryset | AdminUser.objects.filter(duty=duty)
    if admin_queryset.count() == 0:
        lab = None
    else:
        lab = admin_queryset.values_list('laboratory')

    # 查询是否是相应的年级
    from ResourceBorrowingSystem.models import ApplyUserGrade
    # todo: grade
    grade = True
    student = user.to_student()
    try:
        if ApplyUserGrade.objects.filter(grade=student.student_class.grade).count() != 0:
            grade = True
    except:
        pass

    return render(request, 'htmls/user_center/user_center_laboratory.html', {
        "user": user,
        "apply_record": apply_record,
        "lab": lab,
        "grade": grade,
    })