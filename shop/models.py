from django.db import models
from core.models import BaseModel
from user.models import User
# Create your models here.
class Categorys(BaseModel):
    name = models.CharField(max_length=255) 

class Brands(BaseModel):
    name = models.CharField(max_length=255)

class Products(BaseModel):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    info = models.TextField(max_length=255)
    detail = models.JSONField(max_length=255)
    discount = models.CharField(max_length=255)
    category = models.ManyToManyField(Categorys)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

class Colors(BaseModel):
    name = models.CharField(max_length=255)

class InventoryProduct(BaseModel):
    SIZE_CHOICES = [
        ('xs', 'xsmall'),
        ('s', 'small'),
        ('m', 'medium'),
        ('l', 'large'),
        ('xl', 'xlarge')
    ]
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Comments(BaseModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class ShoppingSession(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()

class CartItems(BaseModel):
    session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Payments(BaseModel):
    amount = models.IntegerField()
    status = models.CharField(max_length=10)


class OrderDetails(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    total = models.IntegerField()

class OrderItems(BaseModel):
    order = models.ForeignKey(OrderDetails, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
