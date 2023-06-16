from .models import ShoppingSession, CartItems
from rest_framework import serializers

class CartItemSerializer(serializers.ModelSerializer):
    sub_total = serializers.ReadOnlyField()

    class Meta:
        model = CartItems
        fields = ['product', 'quantity', 'total']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingSession
        fields = ['user', 'total']