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