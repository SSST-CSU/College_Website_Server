from django.urls import path
from rest_framework.routers import DefaultRouter

from UserManagement.views import user_view, teacher_view, student_view, department_view


router = DefaultRouter()
router.register('user', user_view.UserViewSet)

router.register('major', student_view.MajorViewSet)
router.register('student_grade', student_view.StudentGradeViewSet)
router.register('student_class', student_view.StudentClassViewSet)
router.register('undergraduate_student', student_view.UndergraduateStudentViewSet)
router.register('graduate_student', student_view.GraduateStudentViewSet)

router.register('teacher', teacher_view.TeacherViewSet)

router.register('duty_department', department_view.DutyDepartmentViewSet)
router.register('user_duty', department_view.UserDutyViewSet)
router.register('department', department_view.DepartmentViewSet)


app_name = 'UserManagement'

urlpatterns = [
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),
]

urlpatterns += router.urls
