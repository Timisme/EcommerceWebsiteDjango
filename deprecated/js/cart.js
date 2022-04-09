// let updateBtns = document.getElementsByClassName('update-cart-old')

// for (let i = 0; i< updateBtns.length; i++) {
//     updateBtns[i].addEventListener('click', async function(e) {
//         e.preventDefault()
//         let productId = this.dataset.product
//         let action = this.dataset.action 
//         // console.log(productId, action) 
//         await renderCart(productId, action) // 更新 db  && 更新購物車數量 

//         if (updateBtns[i].classList.contains('update-item')){

//             await renderItem(productId); // 更新 cart.html 頁面資訊 && 知道是點哪個 product 

//         }
//     })

// }

// function addCookieItem(productId, action){
//     // console.log('Not Logged in')

//     if(action === 'add'){
//         if(cart[productId] === undefined){
//             cart[productId] = {
//                 'quantity': 1
//             }
//         } else {
//             cart[productId]['quantity'] += 1
//         }
//     }

//     if(action === 'remove'){
//         cart[productId]['quantity'] -= 1

//         if( cart[productId]['quantity'] <= 0){
//             delete cart[productId]
//         }
//     }

//     console.log('Cart:', cart);
//     document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
//     // location.reload();
// }

async function updateUserOrder(productId, action, quantity) {
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
            'quantity': quantity,
        }),
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
    let url = 'http://127.0.0.1:8000/api/order/'

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
            return Array.from(data).filter(order => order.complete == false)[0]['id']
        })

    return currentOrderId
}


// async function renderCart(productId, action){
//     let cartTotal = document.getElementById('cart-total');
//     let cartItems = document.getElementsByClassName('cart-items');
//     const currentOrderId = await getCurrentOrderId()

//     if (user === 'AnonymousUser'){

//       await addCookieItem(productId, action)
//       console.log('AnonymousUser')

//     } else {

//       // 等待更新 Order 資訊後才執行以下的程式
//       await updateUserOrder(productId, action)

    
//       // get 更新後的 order 總數，並更新 cart 的 innerText 
//       let url = `/api/order-detail/${currentOrderId}`
//       console.log(cartTotal)
//       await fetch(url, {
//         method: 'GET',
//         headers: {
//           'Content-Type': 'application/json',
//           'X-CSRFToken': csrftoken,
//         },
//       })
//       .then((res) => {
//         return res.json()
//       })
//       .then((data) => {
//         // console.log('fetch order data success:', data)
//         cartTotal.innerText = data['get_cart_items']
//         cartItems.innerText = data['get_cart_items']
//       })
//     }
//   }