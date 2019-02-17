from rest_framework import serializers
from app_pedidos.models.client import Client
from app_pedidos.models.user import User
from app_pedidos.models.product import Product
from app_pedidos.models.order import Order
from app_pedidos.models.order_item import OrderItem


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client_name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'user_email', 'user_password')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_title', 'product_price', 'product_multiple')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'quantityItem', 'grand_total',
                  'profitability', 'create_date', 'update_date')


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantityProduct')
