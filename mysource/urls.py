
from django.urls import path
from mysource import views

urlpatterns = [
    path('Mysource/', views.Mysource, name='mysource'),
    path('Mysource_detail/<int:id>/', views.Mysource_detail, name='Mysource_detail'),
    path('Mysource_delete/<int:id>/', views.Mysource_delete, name='Mysource_delete'),
    path('Mysource_update/<int:id>/', views.Mysource_update, name='Mysource_update'),
    path('Mysource_detail/<int:id>/<int:pk>/', views.Mysource_detail_update, name='Mysource_detail_update'),
    path('Mysource_detail_delete/<int:id>/<int:pk>/', views.Mysource_detail_delete, name='detail_delete'),
    path('Mysource_detail_add/<int:id>/', views.Mysource_detail_add, name='Mysource_detail_add')
]