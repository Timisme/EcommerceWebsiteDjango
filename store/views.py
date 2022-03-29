from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guessOrder
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url= 'login')
def home(request):

    data = cartData(request)

    products = Product.objects.all()
    data['products'] = products 
    
    return render(request, 'home.html', context= data)

def shop(request):

    data = cartData(request)

    products = Product.objects.all()
    data['products'] = products 
    return render(request, 'shop.html', context= data)

def contact(request):

    data = cartData(request)

    products = Product.objects.all()
    data['products'] = products 
    return render(request, 'contact.html', context= data)

def product_detail(request, pk):

    data = cartData(request)
    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']

    product = Product.objects.get(id= pk)

    data['product'] = product

    return render(request, 'product_detail.html', context= data)

def showCategory(request, pk):

    data = cartData(request)

    products = Product.objects.filter(category__exact = pk)
    data['products'] = products

    return render(request, 'shop.html', context= data)

def cart(request):
    # if the user is authenticed 

    data = cartData(request)

    # products = Product.objects.all()
    # 將 cookie 中的 cart tag 對應的 value 存在 context, 讓 html render 顯示總價與數量
    # (web server 存的數值於後端加工後再 render 到前端)
    return render(request, 'cart.html', context= data)

def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
        
    products = Product.objects.all()

    context = {
        'products': products,
        'items': items,
        'order':  order,
        'cartItems': cartItems
    }
    
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body) # 將 POST request 的 body 以 json 讀取
    
    productId = data['productId']
    action = data['action']
    quantity = int(data['quantity'])

    customer = request.user.customer
    product = Product.objects.get(id= productId)

    order, created = Order.objects.get_or_create(customer= customer, complete= False)
    # If multiple objects are found, get_or_create() raises MultipleObjectsReturned. 
    # If an object is not found, get_or_create() will instantiate and save a new object, 
    # returning a tuple of the new object and True
    # save() is not needed 
    
    orderItem, created = OrderItem.objects.get_or_create(order= order, product= product)

    if action == 'add':
        orderItem.quantity = orderItem.quantity + quantity
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - quantity

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item quantity was updated!', safe= False)

    '''safe: If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed)'''

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    # 如果 user 有登入，則找出該user的 order(未完成), 沒有的話創建一個 Order  
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
    
    else:
        customer, order = guessOrder(request= request, data= data)
    
    total = data['form']['total']
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True

    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )

    print('DATA:', request.body)
    return JsonResponse('Payment complete!!', safe= False)