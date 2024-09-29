from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.
class Auction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    bid_end_time = models.DateTimeField()
    highest_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        return timezone.now() < self.bid_end_time
    
    def __str__(self):
        return f"Auction for {self.product.name}"