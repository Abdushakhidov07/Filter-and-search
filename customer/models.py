from django.db import models
from datetime import datetime


class Customer(models.Model):
    fullname=models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.TimeField(default=datetime.now())
