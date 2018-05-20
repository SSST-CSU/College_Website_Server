from django.contrib import admin
from .models.Department import Department
from .models.Duty import Duty
from .models.Duty_Permition import Duty_Permition
from .models.Major import Major
from .models.Permition import Permition
from .models.Student import Student
from .models.Student_Class import Student_Class
from .models.Student_Grade import Student_Grade
from .models.Teacher import Teacher
from .models.User import User
from .models.User_Duty import User_Duty


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
