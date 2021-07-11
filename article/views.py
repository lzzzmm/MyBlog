import markdown
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from article.forms import ArticlePostForm
from article.models import ArticlePost, ArticleColumn

# 文章列表
from comment.models import Comment


def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 需要传递给模板（templates）的对象
    context = { 'articles': articles }
    # render函数：载入模板，并返回context对象
    return render(request, 'list.html', context)

'''

# 文章详情
def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    # 需要传递给模板的对象
    context = { 'article': article}
    # 载入模板，并返回context对象
    return render(request, 'detail.html', context)
    
'''


# 文章详情
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    # 浏览量 +1
    article.total_views += 1
    article.save(update_fields=['total_views'])

    # 取出文章评论
    comments = Comment.objects.filter(article=id)

    context = {'article': article, 'comments': comments}
    return render(request, 'detail.html', context)


# 写文章的视图
def article_create(request):
    # 判断用户是否提交数据
    userid = request.user.id
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=userid)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("profile")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'create.html', context)


# 删文章
def article_delete(request, id):
    # 根据 id 获取需要删除的文章
    article = ArticlePost.objects.get(id=id)
    # 调用.delete()方法删除文章
    article.delete()
    # 完成删除后返回文章列表
    return redirect("profile")



# 更新文章
def article_update(request, id):
    # 获取需要修改的具体文章对象
    article = ArticlePost.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'update.html', context)

# 文章分类
def article_classification(request):
    if request.method == "POST":
        title = request.POST['title']
        aritcle_column = ArticleColumn(title=title)
        aritcle_column.save()
        return redirect('classification')
    else:
        titles = ArticleColumn.objects.all()
        return render(request, 'classification.html', {'titles': titles})



# 分类后的文章
def classification_detail(request):
    title = request.POST['title']
    column_id = ArticleColumn.objects.get(title=title)
    articles = ArticlePost.objects.filter(column_id=column_id)
    return render(request, 'classification_detail.html', {'articles': articles})
