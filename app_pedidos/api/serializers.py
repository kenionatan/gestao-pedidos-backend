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

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantityProduct')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

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

    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.quantityItem = validated_data.get('quantityItem', instance.quantityItem)
        instance.grand_total = validated_data.get('grand_total', instance.grand_total)
        instance.profitability = validated_data.get('profitability', instance.profitability)
        items_data = validated_data.pop('items')
        product_items_dict = dict((i.id, i) for i in instance.items.all())
        for item_data in items_data:
            if 'id' not in item_data:
                OrderItem.objects.create(order=instance, **item_data)
        if len(product_items_dict) > 0:
            for item in product_items_dict.values():
                item.delete()
        instance.save()
        return instance
