from django.db import models


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_multiple = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.product_title
