from django.test import TestCase
from app_pedidos.models import Product, Order, Client
from rest_framework.test import APIClient, RequestsClient


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(id=1, product_title="Millenium​ ​Falcon",
                               product_multiple=0, product_price=550000)
        Product.objects.create(id=2, product_title="X-Wing",
                               product_multiple=1, product_price=60000)

        client1 = Client.objects.create(id=1, client_name="Darth Vader")
        client2 = Client.objects.create(id=2, client_name="Obi-Wan Kenobi")

        Order.objects.create(id=1, client=client1)
        Order.objects.create(id=2, client=client2)

    def test_verify_product(self):
        assert Product.objects.all().count() == 2
        assert Client.objects.all().count() == 2
        assert Order.objects.all().count() == 2

    def test_api(self):
        client = APIClient()
        response = client.post('http://127.0.0.1:8000/product/', {
            'product_title': 'product name',
            'product_price': 10,
            'product_multiple': 2}, format='json')
        self.assertEqual(201, response.status_code)

    def test_validate_api(self):
        #Product.objects.create(id=4, product_title="Millenium ​Falcon",
                               #product_price=440000.00, product_multiple=2)
        #client1 = Client.objects.create(id=1, client_name="Darth Vader")
        #Order.objects.create(id=1, client=client1)
        client = APIClient()
        response = client.post('http://127.0.0.1:8000/order-item/', json={
            'order': 1,
            'product': 1,
            'price': 550000.00,
            'quantity': 1,
            'profitability': 'Rentabilidade Boa'
        })
        resp = response.json()
        print(resp)
        assert response.status_code == 201
