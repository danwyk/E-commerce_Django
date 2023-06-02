from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# namespace for this app
app_name = 'dashboard'

urlpatterns = [
    # 检查是否 primary key 是有效的
    path( '', views.index, name='index'),
]
