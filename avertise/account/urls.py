from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/account-login.html'), name='account_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/account-logout.html'), name='account_logout'),
    path('signup/', views.signup, name='account_signup'),
    path('profile/', views.profile, name='profile'),
]



