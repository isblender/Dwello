from django.db import models
from apartments.models import Apartment

class Listing(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    available_until = models.DateField()
    status = models.CharField(max_length=20, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
