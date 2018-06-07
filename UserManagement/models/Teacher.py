from django.db import models
from .User import *


class Teacher(models.Model):
    user = models.ForeignKey(User, verbose_name='教师用户', on_delete=models.CASCADE, primary_key=True)
    title_choice = (
        ('教授', '教授'),
        ('副教授', '副教授'),
        ('讲师', '讲师'),
        ('助教', '助教'),
        ('中专高级讲师', '中专高级讲师'),
        ('中专讲师', '中专讲师'),
        ('中专助理讲师', '中专助理讲师'),
        ('高级主教练', '高级主教练'),
        ('中教高级', '中教高级'),
        ('中教一级', '中教一级'),
        ('中教二级', '中教二级'),
        ('研究员', '研究员'),
        ('副研究员', '副研究员'),
        ('助理研究员', '助理研究员'),
        ('高级实验师', '高级实验师'),
        ('实验师', '实验师'),
        ('助理实验师', '助理实验师'),
        ('实验员', '实验员'),
        ('高级工程师', '高级工程师'),
        ('工程师', '工程师'),
        ('助理工程师', '助理工程师'),
        ('技术员', '技术员'),
        ('高级经济师', '高级经济师'),
        ('经济师', '经济师'),
        ('助理经济师', '助理经济师'),
        ('经济员', '经济员'),
        ('高级审计师', '高级审计师'),
        ('审计师', '审计师'),
        ('小教高级', '小教高级'),
        ('幼教高级', '幼教高级'),
        ('主任技师', '主任技师'),
        ('副主任技师', '副主任技师'),
        ('高级政工师', '高级政工师'),
        ('政工师', '政工师'),
        ('助理政工师', '助理政工师'),
        ('政工员', '政工员'),
        ('工人', '工人'),
        ('中级工', '中级工'),
        ('高级工', '高级工'),
        ('院士', '院士'),
    )
    title = models.CharField(verbose_name='职称', max_length=10, choices=title_choice)
    is_external_unit = models.BooleanField(verbose_name='是否外聘', default=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = '教师列表'
        permissions = (
            ('view_teacher', '可以查看老师'),
            ('create_teacher', '可以增加老师'),
            ('update_teacher', '可以修改老师'),
            ('delete_teacher', '可以删除老师'),
        )
