from django.contrib import admin
from .models import *


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Laboratory, LaboratoryAdmin)


class LaboratoryApplyReasonAdmin(admin.ModelAdmin):
    list_display = ['reason']


admin.site.register(LaboratoryApplyReason, LaboratoryApplyReasonAdmin)


class LaboratoryBorrowingApplyAdmin(admin.ModelAdmin):
    list_display = ['apply_id', 'user', 'room', 'apply_time', 'update_time', 'reason_type', 'reason', 'start_time', 'end_time', 'stat']


admin.site.register(LaboratoryBorrowingApply, LaboratoryBorrowingApplyAdmin)


class AdminUserAdmin(admin.ModelAdmin):
    list_display = ['duty', 'laboratory']


admin.site.register(AdminUser, AdminUserAdmin)


class ApplyUserGradeAdmin(admin.ModelAdmin):
    list_display = ['grade']


admin.site.register(ApplyUserGrade, ApplyUserGradeAdmin)
