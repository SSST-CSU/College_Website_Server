from UserManagement.models.User import User


def AuthenticateUser(user_id, user_pwd):
    """
    用户认证，根据用户id和密码验证
    :param user_id: 用户id（学号、工号）
    :param user_pwd: 密码
    :return: User对象，若验证失败则返回None
    """
    user = None
    try:
        user = User.objects.get(id=user_id)
        if user.pwd != user_pwd:
            user = None
    except:
        user = None
    print("AuthenticateUser: " + str(user.id))
    return user
