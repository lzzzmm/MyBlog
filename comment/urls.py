from django.conf.urls import url
from django.urls import path, include

from comment import views

urlpatterns = [
    path('post_comment/<int:article_id>/', views.post_comment, name='post_comment'),
]