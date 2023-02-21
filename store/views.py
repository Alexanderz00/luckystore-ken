from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import json
import datetime

from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.utils.translation import get_language

lang = get_language()
print('**** lang:', lang)

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.order_by('name')
    # products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page') #* 'page' no.
    paged_products = paginator.get_page(page)

    context = {'products':paged_products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']

    products = Product.objects.order_by('name')
    # products = Product.objects.all()
    paginator = Paginator(products, 6)
    page = request.GET.get('page') #* 'page' no.
    paged_products = paginator.get_page(page)

    context = {'products':paged_products, 'cartItems':cartItems}
    return render(request, 'store/contact.html', context)

def store_obsolete(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order': order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)
    try: #! added by flou
        customer = request.user.customer
    except:
        customer = None
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
             customer=customer,
             order=order,
             address=data['shipping']['address'],
             city=data['shipping']['city'],
             state=data['shipping']['state'],
             zipcode=data['shipping']['zipcode'],
        )
    return JsonResponse('Payment complete!', safe=False)



def index(request):
    context = {
    }
    return render(request, 'store/index.html', context)

def about(request):
    context = {
    }
    return render(request, 'store/about.html', context)

