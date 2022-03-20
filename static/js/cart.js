let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i< updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(e) {
        e.preventDefault()
        let productId = this.dataset.product
        let action = this.dataset.action 
        console.log(productId, action) 
        renderCart(productId, action)
        // if(user === 'AnonymousUser'){
        //     addCookieItem(productId, action)
        // }else{
        //     updateUserOrder(productId, action)
        // }
    })

}

function addCookieItem(productId, action){
    // console.log('Not Logged in')

    if(action === 'add'){
        if(cart[productId] === undefined){
            cart[productId] = {
                'quantity': 1
            }
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if(action === 'remove'){
        cart[productId]['quantity'] -= 1

        if( cart[productId]['quantity'] <= 0){
            delete cart[productId]
        }
    }

    console.log('Cart:', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
    // location.reload();
}

async function updateUserOrder(productId, action) {
    let url = '/update_item/' // urls 對應的 view 會 handle request 

    await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action,
        })
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        console.log('updateUserOrder Success')
        // location.reload() // 刷新頁面 沒效率
    })
}

// var currentOrderId = null;
// getCurrentOrderId()

async function getCurrentOrderId(){
    let url = 'http://127.0.0.1:8000/api/order-current/'

    const currentOrderId = await fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        })
        .then((res) => {
            return res.json() // 需要 return 
        })
        .then((data) => {
            console.log('getCurrentOrder:', data)
            return data['id']
        })

    return currentOrderId
}


async function renderCart(productId, action){
    let cartTotal = document.getElementById('cart-total')
    const currentOrderId = await getCurrentOrderId()

    if (user === 'AnonymousUser'){

      await addCookieItem(productId, action)
      console.log('AnonymousUser')

    } else {

      // 等待更新 Order 資訊後才執行以下的程式
      await updateUserOrder(productId, action)

    
      // get 更新後的 order 總數，並更新 cart 的 innerText 
      let url = `/api/order-detail/${currentOrderId}`
      console.log(cartTotal)
      fetch(url, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrftoken,
        },
      })
      .then((res) => {
        return res.json()
      })
      .then((data) => {
        console.log('fetch order data success:', data)
        cartTotal.innerText = data['get_cart_items']
      })
    }
  }