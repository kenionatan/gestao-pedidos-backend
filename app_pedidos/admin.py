from django.contrib import admin
from app_pedidos.models import (Product, Client,
                                Order, OrderItem, User)


admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(User)
