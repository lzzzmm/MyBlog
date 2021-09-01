from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User

from myaccount.models import User_img, UserProfile



# 定义一个行内 admin
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

# 将 Profile 关联到 User 中
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)



# admin.site.register(User_img)
# 重新注册 User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.site_header = "lzz_zmm博客管理后台"
admin.site.site_title = "lzz_zmm博客管理后台"