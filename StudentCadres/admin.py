from django.contrib import admin
from .models import *

# Register your models here.


class ApplyFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'first', 'second', 'swap')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'q')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'ques')


admin.site.register(ApplyForm, ApplyFormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
