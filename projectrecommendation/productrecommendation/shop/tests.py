from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product, Order

class ShopTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product1 = Product.objects.create(name='Laptop', price=1000.00, description='A laptop')
        self.product2 = Product.objects.create(name='Phone', price=500.00, description='A smartphone')

    def test_create_product(self):
        response = self.client.post('/shop/products/', {
            "name": "Tablet",
            "price": "300.00",
            "description": "A tablet device"
        }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_create_order(self):
        response = self.client.post('/shop/orders/', {
            "product_id": self.product1.id,
            "quantity": 2
        }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['quantity'], 2)

    def test_order_listing(self):
        Order.objects.create(product=self.product1, quantity=1)
        response = self.client.get('/shop/orders/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)
