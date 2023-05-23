from django.db import models
from core.models import BaseModel, NameModel
from user.models import User
# Create your models here.

class Discounts(NameModel):
    TYPE = [('CSH', 'cash'), ('PER', 'percent')]
    type = models.CharField(max_length=3, choices=TYPE)
    code = models.CharField(max_length=255, null=True, blank=True)


class Categorys(NameModel):
    discount = models.ForeignKey(Discounts, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class Brands(NameModel):
    discount = models.ForeignKey(Discounts, on_delete=models.CASCADE, null=True, blank=True)

class Products(NameModel):
    price = models.CharField(max_length=255)
    info = models.TextField(max_length=255)
    detail = models.JSONField(blank=True, null=True)
    discount = models.CharField(max_length=255)
    category = models.ManyToManyField(Categorys)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discounts, on_delete=models.CASCADE, null=True, blank=True)


class Image(BaseModel):
    image_address = models.CharField(max_length=255)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)


class Colors(NameModel):
    ...

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
    product = models.ForeignKey(InventoryProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Payments(BaseModel):
    amount = models.IntegerField()
    status = models.CharField(max_length=10)


class OrderDetails(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    session = session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    total = models.IntegerField()



