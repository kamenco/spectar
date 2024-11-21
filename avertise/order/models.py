from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class GraphicOrder(models.Model):
    TYPE_CHOICES = [
        ('icon', 'Icon'),
        ('logo', 'Logo'),
        ('poster', 'Poster'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    size = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    quote = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} order by {self.user.username}"
