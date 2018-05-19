from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'stat']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']


class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ['name', 'major']


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'headmaster', 'instructor']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_class', 'birthday', 'instructor']


class PermitionAdmin(admin.ModelAdmin):
    list_display = ['name', 'superior']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'superior']


class DutyAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']


class DutyPermitionAdmin(admin.ModelAdmin):
    list_display = ['permition', 'duty']


class UserDutyAdmin(admin.ModelAdmin):
    list_display = ['user', 'duty', 'level']


admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Student_Grade, StudentGradeAdmin)
admin.site.register(Student_Class, StudentClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Permition, PermitionAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(Duty_Permition, DutyPermitionAdmin)
admin.site.register(User_Duty, UserDutyAdmin)
