from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from article.models import ArticlePost
from myaccount.forms import ProfileForm
from myaccount.models import UserProfile

@login_required(login_url='../accounts/login/')
def profile(request):
    # 取出所有博客文章
    article_list = ArticlePost.objects.all()
    # 每页显示 1 篇文章
    paginator = Paginator(article_list, 6)

    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)

    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'account/profile.html', context)



# 编辑用户信息
@login_required(login_url='/login/')
def profile_edit(request, id):
    user = User.objects.get(id=id)
    # user_id 是 OneToOneField 自动生成的字段
    profile = UserProfile.objects.get(user_id=id)

    if request.method == 'POST':
        # 验证修改数据者，是否为用户本人
        if request.user != user:
            return HttpResponse("你没有权限修改此用户信息。")

        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            # 取得清洗后的合法数据
            profile_cd = profile_form.cleaned_data
            if 'avatar' in request.FILES:
                profile.avatar = profile_cd["avatar"]
            profile.phone = profile_cd['phone']
            profile.bio = profile_cd['bio']
            profile.save()
            # 带参数的 redirect()
            return redirect("edit", id=id)
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")

    elif request.method == 'GET':
        profile_form = ProfileForm()
        context = { 'profile_form': profile_form, 'profile': profile, 'user': user }
        return render(request, 'edit.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")

