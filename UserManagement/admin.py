from django.contrib import admin
from .models.Department import Department
from .models.Duty_Department import Duty_Department
from .models.Student import Major
from .models.Student import Undergraduate_Student
from .models.Student import Graduate_Student
from .models.Student import Student_Class
from .models.Student import Student_Grade
from .models.Teacher import Teacher
from .models.User import User
from .models.User_Duty import User_Duty


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'stat', 'creator']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'is_external_unit']


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']


class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ['name', 'major']


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'headmaster', 'instructor']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_class', 'birthday', 'instructor']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'superior']


class DutyDepartmentAdmin(admin.ModelAdmin):
    list_display = ['duty', 'department']


class UserDutyAdmin(admin.ModelAdmin):
    list_display = ['user', 'duty']


admin.site.register(User, UserAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(Student_Grade, StudentGradeAdmin)
admin.site.register(Student_Class, StudentClassAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Duty_Department, DutyDepartmentAdmin)
admin.site.register(User_Duty, UserDutyAdmin)
