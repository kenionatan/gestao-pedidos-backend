from rest_framework import serializers
from app_pedidos.models.client import Client
from app_pedidos.models.user import User


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'client_name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'user_email', 'user_password')
