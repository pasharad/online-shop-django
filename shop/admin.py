from django.contrib import admin
from .models import Categorys, Products, Payments, CartItems, Colors, Comments, Brands, InventoryProduct, ShoppingSession, OrderDetails, OrderItems 
# Register your models here.

admin.site.register(Categorys)
admin.site.register(Products)
admin.site.register(Payments)
admin.site.register(CartItems)
admin.site.register(Colors)
admin.site.register(Comments)
admin.site.register(Brands)
admin.site.register(InventoryProduct)
admin.site.register(ShoppingSession)
admin.site.register(OrderDetails)
admin.site.register(OrderItems)