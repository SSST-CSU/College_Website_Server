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
                // 需要填写个人信息
                if(msg === 2) {
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
function gotoArticle(id) {
    window.location.href = "/article/id/" + id.toString();
}
function gotoColumn(id) {
    window.location.href = "/column/id/" + id.toString();
}

function getUserData() {
    var user_id = USER_ID;
    $.ajax({
        url: "/user/user/" + user_id.trim(),
        type: "GET",
        data: {

        },
        success:function(callback){
            var callback_dict = $.parseJSON(callback);
            document.getElementById('modal_name').innerText = callback_dict.name;
            document.getElementById('modal_name_used_before').innerText = callback_dict.name_used_before;
        }
    });
}