from django.test import TestCase
from .models import CartItems, Categorys, Colors, Comments, Image, InventoryProduct, Payments, Products, OrderDetails, ShoppingSession, Discounts, Brands
from user.models import User, Address
# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='Test',
            password='1234',
            first_name='test',
            last_name='test',
            email='test@gmail.com',
            phone='9029999825',
        )
        
        