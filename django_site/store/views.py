from socket import timeout
from django.shortcuts import render
from django.conf import settings
from django.core import serializers
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache # default cache = caches['default'].
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json
from datetime import datetime
from .models import *
from .forms import ContactForm
from .utils import cookieCart, cartData, guessOrder

# Create your views here.

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# @login_required(login_url= 'login')
# @cache_page(timemout= CACHE_TTL, cache= None, key_prefix= None)
def home(request):

    data = cartData(request)

    if cache.get('featured_products'):
        featured_products = cache.get('featured_products')
    else:
        featured_products = Product.objects.filter(is_featured = True)
        cache.set('featured_products', featured_products, timeout= 30)
    
    data['products'] = featured_products
    return render(request, 'home.html', context= data)

def shop(request):

    # Set up pagination 
    p = Paginator(Product.objects.all(), 6) # 6 products per page to show 
    page = request.GET.get('page') # keep track of the page
    products = p.get_page(page) # get products for the specific page

    data = cartData(request)
    data['products'] = products 

    return render(request, 'shop.html', context= data)

@cache_page(timeout= CACHE_TTL, cache= None, key_prefix= None)
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('FORM POST ERROR')
    else:
        form = ContactForm
        
    return render(request, 'contact.html', context= {'form': form})

def product_detail(request, pk):

    data = cartData(request)
    product = Product.objects.get(id= pk)
    data['product'] = product
    # print('serialized product:', serializers.serialize('json', [product, ]))

    # session part 
    request.session.set_expiry(0) # value = 0 means the user session cookie will expire when the user's web brower is closed

    if request.session.get('viewed', None):
        # request.session.flush()
        product_id_list = request.session['viewed']
        if pk in product_id_list:
            print('product id already exists in session backend')
            pass
        else:
            product_id_list.append(pk)
            request.session['viewed'] = product_id_list
            request.session.modified = True
    else:
        print('create viewd session key')
        request.session['viewed'] = [pk, ]

    return render(request, 'product_detail.html', context= data)

def showCategory(request, pk):

    data = cartData(request)

    products = Product.objects.filter(category__exact = pk)
    data['products'] = products

    return render(request, 'shop.html', context= data)

def cart(request):

    data = cartData(request)

    viewed_products_ids= request.session.get('viewed', None)

    if viewed_products_ids:
        data['products'] = Product.objects.filter(pk__in = viewed_products_ids)
    else:
        data['products'] = None

    # 將 cookie 中的 cart tag 對應的 value 存在 context, 讓 html render 顯示總價與數量
    # (web server 存的數值於後端加工後再 render 到前端)
    return render(request, 'cart.html', context= data)

def checkout(request):
    
    data = cartData(request)
    
    return render(request, 'checkout.html', context= data)

def myaccount(request):
    return render(request, 'myaccount.html')

def validateCoupon(request):
    input_code = json.loads(request.body)['code']
    # .values() -> obj to json as queryset
    coupon = Coupon.objects.filter(is_enabled = True, code= input_code).values('discount', 'discount_type')
    print(f'coupon: {list(coupon)}') # 

    if coupon:
        return JsonResponse(list(coupon)[0])
    else:
        return JsonResponse({})

def updateItem(request):

    data = json.loads(request.body) # 將 POST request 的 body 以 json 讀取
    productId = data['productId']
    action = data['action']
    quantity = int(data['quantity'])

    if request.user.is_authenticated:

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
        
    else:
        print('user not logged in')
        return JsonResponse('user not logged in!', safe= False)
        # cart = request.session.get('cart', {})
        # product = Product.objects.get(id= productId)

        # if productId not in cart.keys():
        #     cart[productId] = {
        #         'quantity': 0
        #     }

        # if action == 'add':
        #     cart[productId]['quantity'] += quantity
            
        # elif action == 'remove':
        #     cart[productId]['quantity'] -= quantity

        #     if cart[productId]['quantity'] <= 0:
        #         del cart[productId] 

        # elif action == False:
        #     cart[productId]['quantity'] = quantity

        # # 僅儲存 productId, quantity
        # request.session['cart'] = cart 
        # request.session.modified = True 

        # # return cart 包含 product price
        # cart[productId]['price'] = float(product.price) 
        # print('cart:', cart)

        # return JsonResponse(cart)
    

    '''safe: If it’s set to False, any object can be passed for serialization (otherwise only dict instances are allowed)'''

def processOrder(request):
    transaction_id = datetime.now().timestamp()
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