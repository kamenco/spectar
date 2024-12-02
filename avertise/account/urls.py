# account/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'  # Register the namespace

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/account_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
]
