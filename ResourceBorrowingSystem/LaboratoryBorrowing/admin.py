from django.contrib import admin
from .models import *


class LaboratoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Laboratory, LaboratoryAdmin)


class ApplyReasonAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(ApplyReason, ApplyReasonAdmin)


class LaboratoryBorrowingApplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'apply_time', 'update_time', 'reason_type', 'reason', 'start_time', 'end_time', 'stat']


admin.site.register(LaboratoryBorrowingApply, LaboratoryBorrowingApplyAdmin)
