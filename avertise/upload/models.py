from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order 
# Create your models here.

class CompletedWork(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='completed_work')
    file = models.FileField(upload_to='completed_work/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
