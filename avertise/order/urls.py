from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_home, name='order_home'),  # Add this line to create a URL named 'order'
    path('submit/', views.submit_order, name='submit_order'),
    path('redirect-to-checkout/', views.redirect_to_checkout, name='redirect_to_checkout'),
]
