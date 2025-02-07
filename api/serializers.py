from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'code', 'name', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'order_time']
        read_only_fields = ['id', 'order_time']