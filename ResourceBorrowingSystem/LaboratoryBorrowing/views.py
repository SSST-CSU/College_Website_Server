from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from .serializers import *
import json

# Create your views here.


class LaboratoryViewSet(ModelViewSet):
    serializer_class = LaboratorySerializer
    queryset = Laboratory.objects.all()


class LaboratoryApplyReasonViewSet(ModelViewSet):
    serializer_class = LaboratoryApplyReasonSerializer
    queryset = LaboratoryApplyReason.objects.all()


# class LaboratoryBorrowingApplyViewSet(ModelViewSet):
#     serializer_class = LaboratoryBorrowingApply
#     queryset = LaboratoryBorrowingApply.objects.all()

def apply_lab(request):
    if request.method == "POST":
        # 登录
        try:
            user_id = request.session['user_id']
            user_pwd = request.session['user_pwd']
            from UserManagement.Authentication import AuthenticateUser
            user = AuthenticateUser(user_id, user_pwd)
        except:
            ret = {
                "msg": 0
            }
            return HttpResponse(json.dumps(ret))

        import time
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        apply_id = None
        apply_time = None
        try:
            apply_id = request.POST['apply_id']
            if apply_id is None or apply_id == "":
                apply_id = str(int(time.time()))
        except:
            apply_id = str(int(time.time()))

        room = request.POST['room']
        try:
            # 若已提交过，查询是否有相应ID
            apply = LaboratoryBorrowingApply.objects.get(apply_id=apply_id)
            apply_time = apply.apply_time
        except:
            # 未提交过
            apply_time = now
        update_time = now
        reason_type = request.POST['reason_type']
        reason = request.POST['reason']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        action = request.POST['action']
        try:
            stat = request.POST['stat']
        except:
            if action == "submit":
                stat = "已提交"
            elif action == "save":
                stat = "已保存"
        try:
            proof_document = request.FILES['proof_document']
        except:
            proof_document = None
        if proof_document == "":
            proof_document = None

        try:
            x = LaboratoryBorrowingApply.objects.create(apply_id=apply_id,
                                                    user=user,
                                                    room=room,
                                                    apply_time=apply_time,
                                                    update_time=update_time,
                                                    reason_type=reason_type,
                                                    reason=reason,
                                                    start_time=start_time,
                                                    end_time=end_time,
                                                    stat=stat,
                                                    proof_document=proof_document)
            ret = {
                "msg": 1,
                "id": apply_id,
                "apply_time": str(x.apply_time),
                "stat": stat,
            }
        except Exception as e:
            print(e)
            ret = {
                "msg": str(e)
            }
        return HttpResponse(json.dumps(ret))

    if request.method == "GET":
        id = request.GET["id"]
        apply_queryset = LaboratoryBorrowingApply.objects.get_apply_by_id(id)
        print(apply_queryset)
        ret = {}
        i = 1
        fields = ['apply_id', 'user', 'room', 'apply_time', 'update_time', 'reason_type', 'reason', 'start_time',
                  'end_time', 'stat', 'proof_document', 'seat_number', 'content']
        for apply in apply_queryset:
            ret[str(i)] = {}
            for f in fields:
                ret[str(i)][f] = str(getattr(apply, f))
            i += 1

        return HttpResponse(json.dumps(ret))


def update_lab(request):
    if request.method == "POST":
        # 登录
        try:
            user_id = request.session['user_id']
            user_pwd = request.session['user_pwd']
            from UserManagement.Authentication import AuthenticateUser
            user = AuthenticateUser(user_id, user_pwd)
        except:
            ret = {
                "msg": 0
            }
            return HttpResponse(json.dumps(ret))

        apply_id = request.POST['apply_id']
        print(apply_id)
        stat = request.POST['stat']
        seat_number = request.POST['seat_number']
        content = request.POST['content']
        registration_number = request.POST['registration_number']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        apply = LaboratoryBorrowingApply.objects.get_apply_by_id(apply_id)[0]
        print(apply)
        apply.stat = stat
        if seat_number == "":
            apply.seat_number = None
        else:
            apply.seat_number = seat_number
        if content == "":
            apply.content = None
        else:
            apply.content = content
        if registration_number == "":
            apply.registration_number = None
        else:
            apply.registration_number = registration_number
        apply.start_time = start_time
        apply.end_time = end_time
        import time
        apply.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # LaboratoryBorrowingApply.objects.create(apply)
        LaboratoryBorrowingApply.objects.create(
            apply_id=apply.apply_id,
            user=apply.user,
            room=apply.room,
            apply_time=apply.apply_time,
            update_time=apply.update_time,
            reason_type=apply.reason_type,
            reason=apply.reason,
            start_time=apply.start_time,
            end_time=apply.end_time,
            stat=apply.stat,
            proof_document=apply.proof_document,
            seat_number=apply.seat_number,
            content=apply.content,
            registration_number=apply.registration_number
        )

        ret = {
            "msg": 1
        }
        # except:
        #     ret = {
        #         "msg": 0
        #     }
        return HttpResponse(json.dumps(ret))
