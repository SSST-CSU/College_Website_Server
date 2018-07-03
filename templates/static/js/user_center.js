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
$("ul.nav-sidebar > li").click(function (e) {
    e.preventDefault();
    $(this).tab('show');
    var h = $(this)[0].children[0].href;
    $("#right_page").attr("src", h.toString());
});
window.onload = function (ev) {
    $("#home").click();
    var winheight = window.innerHeight;
    var navheight = document.getElementById("menu-nav").offsetHeight;
    var winwidth = window.innerWidth;
    if(winwidth > 768) {
        document.getElementById("right_page").height = winheight - navheight - 24;
        var leftwidth = document.getElementById("left").offsetWidth;
        document.getElementById("right_page").width = winwidth * 5 / 6 - 20;
    } else {
        document.getElementById("right_page").width = winwidth - 40;
        document.getElementById("right_page").height = document.getElementById("right_page").contentWindow.document.body.scrollHeight;
    }
};
window.onresize = function () {
    var winheight = window.innerHeight;
    var navheight = document.getElementById("menu-nav").offsetHeight;
    var winwidth = window.innerWidth;
    if(winwidth > 768) {
        document.getElementById("right_page").height = winheight - navheight - 24;
        var leftwidth = document.getElementById("left").offsetWidth;
        document.getElementById("right_page").width = winwidth * 5 / 6 - 20;
    } else {
        document.getElementById("right_page").width = winwidth - 40;
        document.getElementById("right_page").height = document.getElementById("right_page").contentWindow.document.body.scrollHeight;
    }
};
