from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


# 文章分类
class ArticleColumn(models.Model):
    """
    栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# 博客文章数据模型
class ArticlePost(models.Model):
    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=100, verbose_name='文章标题')
    # 文章正文。保存大量文本使用 TextField
    body = models.TextField(verbose_name='文章正文')
    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    # 浏览量
    total_views = models.PositiveIntegerField(default=0, verbose_name='浏览量')

    # 文章栏目的 “一对多” 外键
    column = models.ForeignKey(ArticleColumn, null=True, blank=True, on_delete=models.SET_NULL, related_name='article')


    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
        verbose_name = "文章"
        verbose_name_plural = "文章管理"

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('article_detail', args=[self.id])


    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title


