from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart
# Create your views here.

def store(request):

    if request.user.is_authenticated: 
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else: 
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items': 0
            }

        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems,
    }
    return render(request, 'store/store.html', context)

def cart(request):
    # if the user is authenticed 

    if request.user.is_authenticated: 
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else: 
        cookieData = cookieCart(request= request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        

    products = Product.objects.all()
    # 將 cookie 中的 cart tag 對應的 value 存在 context, 讓 html render 顯示總價與數量
    # (web server 存的數值於後端加工後再 render 到前端)
    context = {
        'products': products,
        'items': items,
        'order':  order,
        'cartItems': cartItems
    }
    return render(request, 'store/cart.html', context)

def checkout(request):

    if request.user.is_authenticated: 
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else: 
        cookieData = cookieCart(request= request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
        

    products = Product.objects.all()

    context = {
        'products': products,
        'items': items,
        'order':  order,
        'cartItems': cartItems
    }
    
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body) # 將 POST request 的 body 以 json 讀取
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id= productId)

    order, created = Order.objects.get_or_create(customer= customer, complete= False)
    # If multiple objects are found, get_or_create() raises MultipleObjectsReturned. If an object is not found, get_or_create() will instantiate and save a new object, returning a tuple of the new object and True
    
    orderItem, created = OrderItem.objects.get_or_create(order= order, product= product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + 1 
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)

    '''safe: If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed)'''

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        total = data['form']['total']
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True

        order.save()

        if total.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )
    
    else:
        print('user is not logged in')
    print('DATA:', request.body)
    return JsonResponse('Payment complete!!', safe= False)