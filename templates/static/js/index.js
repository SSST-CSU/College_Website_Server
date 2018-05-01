function login() {
    var user_id = $("#user_id").val();
    var user_pwd = $("#user_pwd").val();
    $.ajax({
        url: "/user/login/",
        type: "POST",
        data: {
            user_id:user_id,
            user_pwd:user_pwd
        },
        success:function(callback){
            var callback_dict = $.parseJSON(callback);
            var msg = callback_dict.msg;
            if(msg === -1) {
                document.getElementById("LoginMsg").innerText = "用户名错误";
            } else if(msg === 1) {
                document.getElementById("LoginMsg").innerText = "密码错误";
            } else {
                // 登陆成功
                location.reload();
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
            user_id:user_id
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

function back() {
    history.back()
}
