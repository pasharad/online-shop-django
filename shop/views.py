from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Categorys, Products, Discounts

# Create your views here.



def index(request):
    categorys = Categorys.objects.get_product_number()
    product_with_discount = Products.objects.discounted_product()
    price_list = []
    for product in product_with_discount:
        if product.discount:
            discount = Discounts.objects.get(products=product)
            if discount.type == 'CSH':
                price_after_discount = int(product.price) - discount.amount
                a = (product, price_after_discount)
                price_list.append(a)
            elif discount.type == 'PER':
                price_after_discount = int(product.price) * (1 - discount.amount)
                a = (product, price_after_discount)
                price_list.append(a)

    content = render(request, 'index.html', {'categorys':categorys, 'price':price_list})
    return HttpResponse(content)