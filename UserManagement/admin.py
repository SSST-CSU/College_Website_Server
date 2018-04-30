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


admin.site.register(User, UserAdmin)
admin.site.register(Permition, PermitionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Duty, DutyAdmin)
