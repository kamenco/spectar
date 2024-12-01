from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:order_id>/', views.upload_completed_work, name='upload_completed_work'),
    path('all-orders/', views.view_all_orders, name='view_all_orders'),
]

