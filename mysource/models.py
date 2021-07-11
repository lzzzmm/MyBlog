

from django.db import models

# Create your models here.
from django.utils import timezone


class My_Source(models.Model):
    mysource = models.CharField(max_length=225, verbose_name='栏目名称')
    note = models.CharField(max_length=225, verbose_name='备注', null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '链接分类'
        verbose_name_plural = '链接分类'

    def __str__(self):
        return self.mysource


class My_source_detail(models.Model):
    mysource_id = models.ForeignKey(My_Source, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='关联分类')
    name = models.CharField(max_length=225, verbose_name='链接名称')
    link_address = models.CharField(max_length=225, verbose_name='链接地址')
    note = models.CharField(max_length=225, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name_plural = '链接'
        verbose_name = '链接'

    def __str__(self):
        return self.name