from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    order_type = models.CharField(max_length=50)  # Example: "Logo", "Leaflet", etc.
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Example: 500.00 for $500
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order_type} - {self.user.username}"
