from django.apps import AppConfig


class MyaccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myaccount'
    verbose_name = "用户扩展信息"
