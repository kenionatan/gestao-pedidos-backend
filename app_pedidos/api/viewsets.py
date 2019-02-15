from rest_framework import viewsets
from app_pedidos.models.client import Client
from app_pedidos.models.user import User
from app_pedidos.models.product import Product
from app_pedidos.models.order import Order
from app_pedidos.models.order_item import OrderItem
from .serializers import (ClientSerializer, UserSerializer,
                          ProductSerializer, OrderSerializer, OrderItemSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
