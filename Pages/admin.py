from django.contrib import admin
from .models import *


class PageAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']


class NavbarObjectAdmin(admin.ModelAdmin):
    list_display = ['page', 'serial_number', 'name', 'herf', 'superior']


class DisplayImageAdmin(admin.ModelAdmin):
    list_display = ['page', 'serial_number', 'name', 'herf']


class DisplayColumnAdmin(admin.ModelAdmin):
    list_display = ['page', 'serial_number', 'column']


admin.site.register(Page, PageAdmin)
admin.site.register(NavbarObject, NavbarObjectAdmin)
admin.site.register(DisplayImage, DisplayImageAdmin)
admin.site.register(DisplayColumn, DisplayColumnAdmin)
admin.site.site_header = '中南大学软件学院后台管理系统'
admin.site.site_title = '中南大学软件学院'
