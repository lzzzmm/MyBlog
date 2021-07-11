from django.contrib import admin
from django.urls import path, include

from myaccount import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('edit/<int:id>/', views.profile_edit, name='edit'),
]