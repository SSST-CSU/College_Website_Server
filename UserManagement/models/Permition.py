from django.db import models


class Permition_Manager(models.Manager):
    def get_root_permition(self):
        """
        获取权限树根节点，若有多棵树则返回多个节点
        :return: 所有的根节点
        """
        root = []
        for permition in self:
            if permition.superior is None:
                root.append(permition)
            elif not self.exists(permition.superior):
                root.append(permition)
        return root

    def get_sub_permition(self):
        """
        返回节点的所有子节点，若存在多个根节点，则存放在list中返回
        :return: 根节点的子节点
        """
        root = self.get_root_permition()
        sub_permitions = []
        for permition in root:
            sub_permitions.append(self.filter(superior=permition))
        return sub_permitions


class Permition(models.Model):
    name = models.CharField('权限名称', primary_key=True, max_length=30)
    superior = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级权限')
    object = Permition_Manager()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = '权限列表'
