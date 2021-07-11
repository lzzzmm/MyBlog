
from django.urls import path
from mysource import views

urlpatterns = [
    path('Mysource/', views.Mysource, name='mysource'),
    path('Mysource_detail/', views.Mysource_detail, name='Mysource_detail'),
    path('Mysource_delete/<int:id>/', views.Mysource_delete, name='Mysource_delete'),
    path('Mysource_update/<int:id>/', views.Mysource_update, name='Mysource_update'),
]