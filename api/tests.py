from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Customer, Order
from unittest.mock import patch

class CustomerTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # Setup authentication here
        
    def test_create_customer(self):
        url = reverse('customer-list')
        data = {
            'code': 'CUST001',
            'name': 'John Doe',
            'phone': '+254700000000'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'John Doe')

class OrderTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            code='CUST001',
            name='John Doe',
            phone='+254700000000'
        )
        # Setup authentication here

    @patch('api.services.sms.send_order_notification')
    def test_create_order(self, mock_send_notification):
        url = reverse('order-list')
        data = {
            'customer': self.customer.id,
            'item': 'Test Item',
            'amount': '99.99'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        mock_send_notification.assert_called_once()