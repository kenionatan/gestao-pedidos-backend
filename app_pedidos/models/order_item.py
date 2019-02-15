from django.db import models
from .order import Order
from .product import Product


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    quantityProduct = models.BigIntegerField(default=1)

    def __str__(self):
        return self.product
