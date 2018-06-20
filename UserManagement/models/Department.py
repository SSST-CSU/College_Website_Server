from django.db import models


class DepartmentManager(models.Manager):
    pass


class Department(models.Model):
    name = models.CharField('部门', max_length=30)
    superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None, verbose_name='上级部门')
    objects = DepartmentManager()

    def __str__(self):
        return str(self.name)

    def get_superior_department(self):
        """
        返回上级部门
        :return: class<Department>
        """
        return self.superior

    def get_subordinate_department(self):
        """
        返回下级部门
        :return: queryset<Department>
        """
        return Department.objects.filter(superior=self)

    def get_root(self):
        """
        获取根节点
        :return: class<Departmrnt>
        """
        now = self
        while now.superior is not None:
            now = now.superior
        return now

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门列表'
        permissions = (
            ('view_dept', '可以查看部门'),
            ('create_dept', '可以创建部门'),
            ('update_dept', '可以修改部门'),
            ('delete_dept', '可以删除部门'),
        )
