from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from UserManagement.views import user_view, teacher_view, student_view, department_view


router = DefaultRouter()
router.register(prefix='user', viewset=user_view.UserViewSet, base_name='user')

router.register(prefix='major', viewset=student_view.MajorViewSet, base_name='major')
router.register(prefix='student_grade', viewset=student_view.StudentGradeViewSet, base_name='student_grade')
router.register(prefix='student_class', viewset=student_view.StudentClassViewSet, base_name='student_class')
router.register(prefix='undergraduate_student', viewset=student_view.UndergraduateStudentViewSet, base_name='undergraduate_student')
router.register(prefix='graduate_student', viewset=student_view.GraduateStudentViewSet, base_name='graduate_student')

router.register(prefix='teacher', viewset=teacher_view.TeacherViewSet, base_name='teacher')

router.register(prefix='duty_department', viewset=department_view.DutyDepartmentViewSet, base_name='duty_department')
router.register(prefix='user_duty', viewset=department_view.UserDutyViewSet, base_name='user_duty')
router.register(prefix='department', viewset=department_view.DepartmentViewSet, base_name='department')


app_name = 'UserManagement'

urlpatterns = [
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),
]

urlpatterns += router.urls
