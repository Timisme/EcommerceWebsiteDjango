// 1. 監聽所有購物車商品的 input 變動
// 2. 如有變動，先得到目前的 order id 
// 3. api 將該變動商品更新數量
// 4. 得到更新後的商品數量和 order 變化
// 5. DOM 動態更新 SUBTOTAL, ORDER TOTAL

cartInputBtns = document.getElementsByClassName('update-cart')

for (let i= 0; i < cartInputBtns.length; i++){
    let cartInputBtn = cartInputBtns[i]
    cartInputBtn.addEventListener('change', async function(e){
        e.preventDefault()
        orderId = await getCurrentOrderId()
        productId = cartInputBtn.dataset.product 
        itemId = cartInputBtn.dataset.item
        console.log('item id:', itemId)
        quantity = cartInputBtn.value
        data = await updateOrderItem(productId, itemId, orderId, quantity)
        console.log('data from updateorderitem:', data)
        await renderOrderItem(productId, data['get_total'])
        await renderOrder(orderId)
    })
}

// restapi 修改 orderitem 資料，並回傳更新後資料。
async function updateOrderItem(productId, itemId, orderId, quantity){
    url = `http://127.0.0.1:8000/api/orderItem-update/${itemId}`

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
    let url = `http://127.0.0.1:8000/api/order-detail/${currentOrderId}`
    let cartTotal = document.getElementById('cart-total')

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
    // console.log('fetch order data success:', data)
    cartTotal.innerText = `$ ${data['get_cart_total']}`
    console.log('cart total has been rerendered:', data['get_cart_total'])
    // cartItems.innerText = data['get_cart_items']
    })
}