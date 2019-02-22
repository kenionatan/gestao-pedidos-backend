from django.db import models
from .order import Order
from .product import Product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantityProduct = models.BigIntegerField(default=1)
    profitability = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.product
