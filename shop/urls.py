from .views import index, product_view, category_view, _cart_id, add_cartitem, remove_cart, cart
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('product-detail/<int:pk>', product_view, name='product-detail'),
    path('category/<int:pk>', category_view, name='category'),
    path('cart/', _cart_id, name='cart'),
    path('add-cart/<int:product_id>', add_cartitem, name='add-cart'),
    path('remove-cart/<int:cart_id>', remove_cart, name='remove-cart'),
    path('cart/<int:cart_id>', cart, name='cart'),
]