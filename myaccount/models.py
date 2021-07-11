from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from registration.forms import User


class UserProfile(models.Model):
    # 与 User 模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 电话号码字段
    phone = models.CharField(max_length=20, blank=True)
    # 头像
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 个人简介
    bio = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = '用户扩展信息',
        verbose_name_plural = '用户扩展信息'

    def __str__(self):
        return "{}".format(self.user.__str__())


# 信号接收函数，每当新建 User 实例时自动调用
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# 信号接收函数，每当更新 User 实例时自动调用
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()






class User_img(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    img = models.ImageField(upload_to='images/', blank=True, verbose_name='头像',default="../static/images/default_img.jpg")

    class Meta:
        verbose_name = "用户头像"
        verbose_name_plural = "用户头像"

    def __str__(self):
        return self.user.username
