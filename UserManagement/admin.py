from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd']


class PermitionAdmin(admin.ModelAdmin):
    list_display = ['name']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'superior']


class DutyAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']


class DutyPermitionAdmin(admin.ModelAdmin):
    list_display = ['permition', 'duty']


class UserDutyAdmin(admin.ModelAdmin):
    list_display = ['user', 'duty']


admin.site.register(User, UserAdmin)
admin.site.register(Permition, PermitionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Duty_Permition, DutyPermitionAdmin)
admin.site.register(User_Duty, UserDutyAdmin)
