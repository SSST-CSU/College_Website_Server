function back() {
    history.back()
}
function login() {
    var user_id = $("#user_id").val();
    var user_pwd = $("#user_pwd").val();
    $.ajax({
        url: "/user/login/",
        type: "POST",
        data: {
            user_id:user_id,
            user_pwd:user_pwd,
            csrfmiddlewaretoken: CSRF_TOKEN
        },
        success:function(callback){
            var callback_dict = $.parseJSON(callback);
            var msg = callback_dict.msg;
            if(msg === -1) {
                document.getElementById("LoginMsg").innerText = "用户名错误";
            } else if(msg === 1) {
                document.getElementById("LoginMsg").innerText = "密码错误";
            } else {
                // 需要填写个人信息
                if(msg === 10) {
                    $('#UpdateModal').modal('show');
                    USER_ID = user_id;
                    getUserData();
                }
                else {
                    // 登陆成功
                    location.reload();
                }
            }
        }
    });
}
function logout() {
    var user_id = USER_ID;
    $.ajax({
        url: "/user/logout/",
        type: "POST",
        data: {
            user_id:user_id,
            csrfmiddlewaretoken: CSRF_TOKEN
        },
        success:function(callback){
            var callback_dict = $.parseJSON(callback);
            var msg = callback_dict.msg;
            if(msg === 0) {
                alert("登出失败");
            } else {
                // 登出成功
                location.reload();
            }
        }
    });
}
function logout2() {
    var user_id = USER_ID;
    $.ajax({
        url: "/user/logout/",
        type: "POST",
        data: {
            user_id:user_id,
            csrfmiddlewaretoken: CSRF_TOKEN
        },
        success:function(callback){
            var callback_dict = $.parseJSON(callback);
            var msg = callback_dict.msg;
            if(msg === 0) {
                alert("登录失败");
                location.reload();
            }
        }
    });
}
function gotoArticle(id) {
    window.location.href = "/article/id/" + id.toString();
}
function gotoColumn(id) {
    window.location.href = "/column/id/" + id.toString();
}

function getUserData() {
    var user_id = USER_ID;
    $.ajax({
        url: "/user/user/" + user_id.trim() + '/',
        type: "GET",
        data: {

        },
        success:function(callback){
            USER = callback;
            $('#modal_name').val(USER.name);
            $('#modal_id').val(USER.id);
            $('#modal_pwd').val("");
            $('#modal_name_used_before').val(USER.name_used_before);
            $('#modal_sex').val(USER.sex);
            $('#modal_phone_number').val(USER.phone_number);
            $('#modal_qq').val(USER.qq);
            $('#modal_email').val(USER.email);
            logout2();
        }
    });
}
function update() {
    var name = $('#modal_name').val();
    var id = $('#modal_id').val();
    var pwd = $('#modal_pwd').val();
    if(pwd === "") {
        alert("请修改密码！");
        return;
    }
    if(pwd.length < 8) {
        alert("为了您的账户安全，密码应该至少由8位字符或数字组成！");
        return;
    }
    var name_used_before = $('#modal_name_used_before').val();
    var sex = $('#modal_sex').val();
    var phone_number = $('#modal_phone_number').val();
    if(phone_number === "") {
        alert("请填写常用的电话！");
        return;
    }
    var qq = $('#modal_qq').val();
    if(qq === "") {
        alert("为了能够更好的使用网站的各种功能，请填写QQ号！");
        return;
    }
    var email = $('#modal_email').val();
    if(email === "") {
        alert("为了能够更好的使用网站的各种功能，请填写邮箱地址！");
        return;
    }
    $.ajax({
        url: "/user/user/" + id.trim() + '/',
        type: "PUT",
        data: {
            id: id,
            name: name,
            stat: USER.stat,
            name_used_before: name_used_before,
            sex: sex,
            birthday: USER.birthday,
            qq: qq,
            email: email,
            political: USER.political,
            native_place: USER.native_place,
            id_number: USER.id_number,
            phone_number: phone_number,
            country_and_region: USER.country_and_region,
            creator: USER.creator
        },
        success: function(callback){
            $('#UpdateModal').modal('hide');
        },
        fail: function(xhr, textStatus, errorThrown){
            alert('修改失败，请稍后再试。');
        }
    })
}