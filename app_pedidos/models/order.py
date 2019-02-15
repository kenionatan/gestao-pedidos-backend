from django.db import models
from .user import User
from .client import Client
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    quantityItem = models.BigIntegerField(default=1)
    price = models.FloatField(default=0)
    profitability = models.CharField(max_length=50)
    create_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.create_date
