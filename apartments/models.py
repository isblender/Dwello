from django.db import models
from users.models import User

class Apartment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    number_of_rooms = models.IntegerField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)
    available_from = models.DateField()
    available_until = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
