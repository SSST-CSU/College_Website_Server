from django.contrib import admin
from .models import *


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']


class RoomBorrowingApplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'apply_time', 'start_time', 'end_time', 'stat']


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomBorrowingApply, RoomBorrowingApplyAdmin)