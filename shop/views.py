from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .models import Categorys, Colors, Image, Products, Discounts, InventoryProduct, CartItems, ShoppingSession

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
            elif discount.type == 'PER':
                price_after_discount = int(product.price) * (1 - discount.amount)
                a = (product, price_after_discount)
        # image = (Image.objects.filter(product=product))
        # a += image
        price_list.append(a)

    content = render(request, 'index.html', {'categorys':categorys, 'price':price_list})
    return HttpResponse(content)

def product_view(request, pk):
    categorys = Categorys.objects.get_product_number()
    product = Products.objects.get_one(pk=pk)
    product_inventory = InventoryProduct.objects.filter(product_id = product.id)
    colors = []
    for p in product_inventory:
        color = Colors.objects.get(pk=p.color)
        colors.append(color)
    if product.discount:    
        discount = Discounts.objects.get(products=product)
        if discount.type == 'CSH':
            price_after_discount = int(product.price) - discount.amount
        elif discount.type == 'PER':
            price_after_discount = int(product.price) * (1 - discount.amount)
    else:
        price_after_discount = None

    image = Image.objects.filter(product=product)
    content = render(request, 'detail.html', 
                     {
                        'product':product,
                        'product_inventory':product_inventory,
                        'colors':colors,
                        'discounted_price': price_after_discount,
                        'img':image,
                        'categorys':categorys
                    })
    return HttpResponse(content)

def category_view(request, pk):
    categorys = Categorys.objects.get_product_number()
    category = Categorys.objects.get_one(pk=pk)
    products = Products.objects.filter(category=category)
    product_list = []
    for product in products:
        img = Image.objects.filter(product=product)[:1]
        if product.discount:
            discount = Discounts.objects.get(products=product)
            if discount.type == 'CSH':
                price_after_discount = int(product.price) - discount.amount
                a = (product, price_after_discount, img)
            elif discount.type == 'PER':
                price_after_discount = int(product.price) * (1 - discount.amount)
                a = (product, price_after_discount, img)
        else:
            a = (product , img)
        product_list.append(a)
    content = render(request, 'shop.html', {
        'products':product_list,
        'categorys':categorys,

    })
    return HttpResponse(content)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cartitem(request, product_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            size = request.POST.get('size')[0]
            quantity = request.POST.get('quantity')
            colors = request.POST.get('color')
            color = Colors.objects.get(name=colors)
            product = Products.objects.get(id=product_id)
            in_pro = InventoryProduct.objects.get(product=product, color=color, size=size)
            if ShoppingSession.objects.filter(user=user, total=0).exists():
                cart = ShoppingSession.objects.get(user=user, total=0)
                cart_item = CartItems.objects.create(session=cart, product=in_pro, quantity=quantity)
                cart.total+=1
                cart_item.save()
                cart.save()
            else:
                cart = ShoppingSession.objects.create(user=user, total=0)
                cart_item = CartItems.objects.create(session=cart, product=in_pro, quantity=quantity)
                cart.total+=1
                cart_item.save()
                cart.save()
        return redirect(f'http://127.0.0.1:8000/shop/product-detail/{product.id}')
    return HttpResponse('shit')

def remove_cart(request, cart_id):
    cart = ShoppingSession.objects.get(id=cart_id)
    cart.delete()

def cart(request, cart_id):
    cart = ShoppingSession.objects.get(id=cart_id)
    cart_items = CartItems.objects.filter(session=cart)
    return render(request, 'cart.html', {'cart_items':cart_items})