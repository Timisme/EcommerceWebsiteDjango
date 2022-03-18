import json 
from .models import * 

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    # 每次在 cart page 的 request handling 都會先創建預設的 order
    order = {
        'get_cart_total': 0,
        'get_cart_items': 0,
        'shipping': False,
        }
    cartItems = order['get_cart_items']

    # 針對 cart 中每個 Product, 對 order 和 items 內容進行修改
    for i in cart:
        cartItems += cart[i]["quantity"]

        try: 
            # 有可能 user cookie 有存已經刪除的 product 
            product = Product.objects.get(id= i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total 
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product':{
                    'id': product.id,
                    'name': product.name, 
                    'price': product.price,
                    'imageURL': product.imageURL
                },

                'quantity': cart[i]['quantity'],
                'get_total': total, 
            }

            items.append(item)

            if product.digital == False:
                order['shipping'] = True 
        except:
            pass
    return {
        'cartItems': cartItems,
        'order': order,
        'items': items,
    }

def cartData(request):

    if request.user.is_authenticated: 
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer= customer, complete= False)
        items = order.orderitem_set.all()
    else: 
        cookieData = cookieCart(request= request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {
        'items': items,
        'order':  order,
        'cartItems': cartItems
    }

def guessOrder(request, data):

    print('user is not logged in')
    print('COOKIES:', request.COOKIES)

    # 如果 user 未登入，則取得其填寫的名稱與電郵
    name = data['form']['name']
    email = data['form']['email']

    # 取得 user cookie 儲存的 cart 資訊
    cookieData = cookieCart(request)
    items = cookieData['items']

    # 取得該 user 的customer instance
    customer, created = Customer.objects.get_or_create(
        email = email,
    )

    # 修改 email 對應的 name
    customer.name = name
    customer.save()

    # 取得該 customer 對應的 order 
    order = Order.objects.create(
        customer= customer,
        complete= False,
    )

    for item in items:
        product = Product.objects.get(id= item['product']['id'])
        orderItem = OrderItem.objects.create(
            product= product,
            order= order,
            quantity= item['quantity'],
        )
    return customer, order