from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from article.models import ArticlePost


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name='comments', verbose_name='文章')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',
                             null=True, verbose_name='登陆用户')
    body = RichTextField(verbose_name='评论')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('created', )
        verbose_name_plural = '评论'
        verbose_name = '评论'

    def __str__(self):
        return self.body[:20]