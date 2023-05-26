from .views import index, product_view
from django.urls import path

urlpatterns = [
    path('index/', index, name='index'),
    path('product-detail/<int:pk>', product_view, name='product-detail')
]