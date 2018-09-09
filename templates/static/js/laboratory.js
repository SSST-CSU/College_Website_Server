let callback_dict;
function apply_list_item_click(id) {
    $("#detail_table  tr:not(:first)").empty("");
    $.ajax({
        url: "/borrow/laboratory/apply_lab/",
        type: "GET",
        data: {
            id: id
        },
        success:function(callback){
            callback_dict = $.parseJSON(callback);

            $("#detail_room").val(callback_dict[1].room);
            $("#detail_reason_type").val(callback_dict[1].reason_type);
            $("#detail_reason").val(callback_dict[1].reason);
            $("#detail_start_time").val(callback_dict[1].start_time.substr(0,10));
            $('#detail_end_time').val(callback_dict[1].end_time.substr(0,10));
            $('#detail_submit_time').val(callback_dict[1].apply_time.substr(0,19));
            $('#detail').modal('show');
            // let len = callback_dict.__proto__.constructor.length;
            for(let i in callback_dict) {
                let row = document.getElementById("detail_table").insertRow(1);
                let col = new Array(4);
                let update_time = callback_dict[i].update_time;
                let stat = callback_dict[i].stat;
                let seat = callback_dict[i].seat_number;
                if(seat === "None") {
                    seat = "";
                }
                let content = callback_dict[i].content;
                if(content === "None") {
                    content = "";
                }
                for(let j = 0; j < 4; j++) {
                    col[j] = row.insertCell(j)
                }
                col[0].innerHTML = update_time.substr(0,19);
                col[1].innerHTML = stat;
                col[2].innerHTML = seat;
                col[3].innerHTML = content;
                console.log(col)
            }
        }
    });
    
}

function newApply() {
    $.ajax({
        url: "/borrow/laboratory/laboratory/",
        type: "GET",
        success:function(callback){
            for(room of callback.results) {
                document.getElementById("room").options.add(new Option(room.name, room.name));
            }
            document.getElementById("room").selectedIndex = -1;
        }
    });
    $.ajax({
        url: "/borrow/laboratory/laboratory_apply_reason/",
        type: "GET",
        success:function(callback){
            for(reason of callback.results) {
                document.getElementById("reason_type").options.add(new Option(reason.reason, reason.reason));
            }
            document.getElementById("reason_type").selectedIndex = -1;
        }
    });
    $('#newApply').modal('show');
}

function submitApply(action) {
    if(!document.getElementById("ck").checked) {
        alert("请阅读《软件学院本科生开放实验室管理方案》");
        return;
    }
    let formData = new FormData();

    let room = document.getElementById("room");
    if(room.value === "") {
        alert("请选择实验室");
        return;
    }
    let reason_type = document.getElementById("reason_type");
    if(reason_type.value === "") {
        alert("请选择申请理由类别");
        return;
    }
    let reason = document.getElementById("reason");
    let start_time = document.getElementById("start_time");
    let end_time = document.getElementById("end_time");
    if(start_time.value === "" || end_time.value === "") {
        alert("请选择注册的时间段");
        return;
    }
    if(document.getElementById("proof_document").value === "") {
        formData.append('proof_document', "");
    } else {
        let proof_document = document.getElementById("proof_document");
        formData.append('proof_document', proof_document.files[0]);
    }

    formData.append('action', action);
    formData.append('reason', reason.value);
    formData.append('room', room.value);
    formData.append('reason_type', reason_type.value);
    formData.append('start_time', start_time.value);
    formData.append('end_time', end_time.value);
    formData.append('csrfmiddlewaretoken', CSRF_TOKEN);

    $.ajax({
        url: "/borrow/laboratory/apply_lab/",
        type: "POST",
        processData: false,
        contentType: false,
        data: formData,
        success:function(callback){
            let callback_dict = $.parseJSON(callback);
            if(callback_dict.msg === 1) {
                let row = document.getElementById("apply_table").insertRow(1);
                let col = new Array(5);
                let id = callback_dict.id;
                let stat = callback_dict.stat;
                let apply_time = callback_dict.apply_time;
                for(let i = 0; i < 5; i++) {
                    col[i] = row.insertCell(i)
                }
                col[0].innerHTML = id.trim();
                col[1].innerHTML = room.value;
                col[2].innerHTML = apply_time.trim();
                col[3].innerHTML = reason_type.value;
                col[4].innerHTML = stat.trim();

                $('#newApply').modal('hide');
                location.reload();
            } else if(callback_dict.msg === 0) {
                alert("申请发送失败，请稍后重试");
            } else {
                alert(callback_dict.msg)
            }
        }
    });
}

function adminCK(apply_id) {
    let stat = $('#ck_stat_' + apply_id).val();
    let seat_number = $('#ck_seat_number_' + apply_id).val();
    let content = $('#ck_content_' + apply_id).val();
    let registration_number = $('#ck_registration_number_' + apply_id).val();
    let reg = /(\d{4})\年(\d{1,2})\月(\d{1,2})\日 (\d{1,2}):(\d{2})/;
    let start_time = $('#ck_start_time_' + apply_id).val().replace(reg, "$1-$2-$3 $4:$5");
    let end_time = $('#ck_end_time_' + apply_id).val().replace(reg, "$1-$2-$3 $4:$5");
    $.ajax({
        url: "/borrow/laboratory/update_lab/",
        type: "POST",
        data: {
            csrfmiddlewaretoken: CSRF_TOKEN,
            apply_id: apply_id,
            stat: stat,
            content: content,
            seat_number: seat_number,
            registration_number: registration_number,
            start_time: start_time,
            end_time: end_time
        },
        success:function(callback){
            let callback_dict = $.parseJSON(callback);
            if(callback_dict.msg === 1) {
                location.reload();
            } else {
                alert("操作失败！");
            }
        }
    });
}
