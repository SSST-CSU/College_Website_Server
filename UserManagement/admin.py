from django.contrib import admin
from .models.Department import Department
from .models.Duty_Department import Duty_Department
from .models.Student import Major, Student_Grade, Student_Class, Undergraduate_Student, Graduate_Student
from .models.Teacher import Teacher
from .models.User import User
from .models.User_Duty import User_Duty


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'stat']


admin.site.register(User, UserAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'stat', 'title']


admin.site.register(Teacher, TeacherAdmin)


class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Major, MajorAdmin)


class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ['name', 'major']


admin.site.register(Student_Grade, StudentGradeAdmin)


class StudentClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade', 'headmaster', 'instructor']


admin.site.register(Student_Class, StudentClassAdmin)


class UndergraduateStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'stat', 'student_class']


admin.site.register(Undergraduate_Student, UndergraduateStudentAdmin)


class GraduateStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'stat', 'student_class', 'instructor']


admin.site.register(Graduate_Student, GraduateStudentAdmin)


class DutyDepartmentAdmin(admin.ModelAdmin):
    list_display = ['duty', 'department']


admin.site.register(Duty_Department, DutyDepartmentAdmin)


class UserDutyAdmin(admin.ModelAdmin):
    list_display = ['user', 'duty']


admin.site.register(User_Duty, UserDutyAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'superior']


admin.site.register(Department, DepartmentAdmin)
