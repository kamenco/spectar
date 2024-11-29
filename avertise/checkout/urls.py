from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/', views.success, name='checkout_success'),
    path('profile/', views.profile, name='profile'),  # Profile page
]


