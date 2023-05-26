from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Categorys, Colors, Image, Products, Discounts, InventoryProduct

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

def product_view(request, pk):
    product = Products.objects.get_one(pk=pk)
    product_inventory = InventoryProduct.objects.filter(product_id = product.id)
    colors = []
    for p in product_inventory:
        color = Colors.objects.get(pk=p.color)
        colors.append(color)
    discount = Discounts.objects.get(products=product)
    if discount.type == 'CSH':
        price_after_discount = int(product.price) - discount.amount
    elif discount.type == 'PER':
        price_after_discount = int(product.price) * (1 - discount.amount)

    image = Image.objects.filter(product=product)
    content = render(request, 'detail.html', 
                     {
                        'product':product,
                        'product_inventory':product_inventory,
                        'colors':colors,
                        'discounted_price': price_after_discount,
                        'img':image
                    })
    return HttpResponse(content)