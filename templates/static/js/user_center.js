function back() {
    history.back()
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

function article() {

}
