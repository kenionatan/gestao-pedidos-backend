from rest_framework import viewsets
from app_pedidos.models.client import Client
from app_pedidos.models.user import User
from .serializers import ClientSerializer, UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
