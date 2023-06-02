from django.urls import path
from . import views

# namespace for this app
app_name = 'item'

urlpatterns = [
    # 检查是否 primary key 是有效的
    path('', views.browse, name='browse'),
    path('new/', views.new, name='new'),
    path( '<int:primaryKey>/', views.detail, name='detail'),
    path( '<int:primaryKey>/delete/', views.delete, name='delete'),
    path( '<int:primaryKey>/edit/', views.edit, name='edit'),
]
