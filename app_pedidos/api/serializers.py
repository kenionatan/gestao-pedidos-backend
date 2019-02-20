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


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantityProduct')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'client', 'quantityItem', 'grand_total',
                  'items', 'profitability', 'create_date', 'update_date')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        item = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=item, **item_data)
        return item
