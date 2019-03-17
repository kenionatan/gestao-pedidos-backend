from django.db import models
from .user import User
from .client import Client
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    quantityItem = models.BigIntegerField(default=1)
    grand_total = models.FloatField(default=0)
    create_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    update_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.client.client_name
