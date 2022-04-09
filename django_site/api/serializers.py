from rest_framework import serializers
from store.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    get_cart_items = serializers.ReadOnlyField()
    get_cart_total = serializers.ReadOnlyField()
    get_cart_total_final = serializers.ReadOnlyField()
    class Meta: 
        model = Order
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    get_total = serializers.ReadOnlyField()
    class Meta: 
        model = OrderItem
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ShippingAddress
        fields = '__all__'

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['email']
