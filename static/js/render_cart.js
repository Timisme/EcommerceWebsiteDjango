// 1. 監聽所有購物車商品的 input 變動
// 2. 如有變動，先得到目前的 order id 
// 3. api 將該變動商品更新數量
// 4. 得到更新後的商品數量和 order 變化
// 5. DOM 動態更新 SUBTOTAL, ORDER TOTAL

cartInputBtns = document.getElementsByClassName('update-cart')

for (let i= 0; i < cartInputBtns.length; i++){
    let cartInputBtn = cartInputBtns[i]
    cartInputBtn.addEventListener('change', async function(e){
        e.preventDefault();
        let orderId = await getCurrentOrderId();
        let productId = cartInputBtn.dataset.product ;
        let itemId = cartInputBtn.dataset.item;
        let quantity = cartInputBtn.value;

        if(user === 'AnonymousUser'){
            console.log('please log in first')
            // cart = await AnonymousUpdateCart(productId, quantity)
            // console.log('cart data:', cart)
            // subtotal = cart[productId]['price'] * cart[productId]['quantity']
            // await renderOrderItem(productId, subtotal)
            // await AnonymousRenderCart()

        } else {
            let data = await updateOrderItem(productId, itemId, orderId, quantity);
            console.log('data from updateorderitem:', data)
            await renderOrderItem(productId, data['get_total']);
            await renderOrder(orderId);
        }
        
    })
}

// restapi 修改 orderitem 資料，並回傳更新後資料。
async function updateOrderItem(productId, itemId, orderId, quantity){
    url = `http://127.0.0.1:8000/api/orderItem/${itemId}`

    res = await fetch(url, {
        method: "PATCH",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'product': productId,
            'order': orderId,
            'quantity': quantity,
        }),
    })
    .then(
        (response) => {
            return response.json()
        })
    .then((data) => {
        console.log("item has been updated!")
        console.log("data: ", data)
        return data
    })

    return res 
}

async function renderOrderItem(productId, subtotal){
    elements = document.getElementsByClassName('subtotal')
    element = Array.from(elements).filter(element => element.dataset.product === productId)
    element[0].innerText = subtotal
}

// 給定 order id 將 html 動態修改
async function renderOrder(currentOrderId){
    let url = `http://127.0.0.1:8000/api/order/${currentOrderId}`
    let cartTotal = document.getElementById('cart-total')
    let cartTotalFinal = document.getElementById('cart-total-final')

    await fetch(url, {
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
    cartTotal.innerText = `$ ${data['get_cart_total']}`
    cartTotalFinal.innerHTML = `<strong>$ ${data['get_cart_total_final']}</strong>`
    console.log('cart total has been rerendered:', data['get_cart_total'])
    })
}

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

// 匿名 User 

// async function AnonymousUpdateCart(productId, quantity){
//     const url = "/update_item/"
    
//     let cart = await fetch(url, {
//         method: 'POST', 
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({
//             'productId': productId,
//             'action': false,
//             'quantity': quantity,
//         }),
//     })
//     .then(res => {res.json()})
//     .then(data => {
//         return data
//     })

//     return cart 
// }

// async function AnonymousRenderCart(cart){
//     let cartTotal = document.getElementById('cart-total')
//     let cart_total = 0

//     for (const element of cart){
//         element
//     }  
//     cartTotal.innerText = `$ ${data['get_cart_total']}`
// }