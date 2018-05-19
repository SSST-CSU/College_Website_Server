from django.shortcuts import render
from UserManagement.Authentication import AuthenticateUser


def index(request):
    user = None
    try:
        user_id = request.session['user_id']
        user_pwd = request.session['user_pwd']
        user = AuthenticateUser(user_id, user_pwd)
    except:
        request.session['user_name'] = None

    return render(request, 'htmls/index.html', {
        "user": user
    })
