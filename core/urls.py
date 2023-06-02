from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

# namespace for this app
app_name = 'core'

urlpatterns = [
    # 检查是否 primary key 是有效的
    path( '', views.index, name='index'),
    path( 'contact/', views.contact, name='contact'),
    path( 'signup/', views.signup, name='signup'),
    path( 'login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
