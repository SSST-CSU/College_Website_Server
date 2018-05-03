from django.contrib import admin
from .models import *


class NavbarObjectAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'serial_number', 'name', 'herf', 'superior']


class DisplayImageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'serial_number', 'name', 'herf']


class DisplayColumnAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'serial_number', 'column']


class PageTypeAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'type']


admin.site.register(NavbarObject, NavbarObjectAdmin)
admin.site.register(DisplayImage, DisplayImageAdmin)
admin.site.register(DisplayColumn, DisplayColumnAdmin)
admin.site.register(Page_Type, PageTypeAdmin)
admin.site.site_header = '中南大学软件学院后台管理系统'
admin.site.site_title = '中南大学软件学院'
