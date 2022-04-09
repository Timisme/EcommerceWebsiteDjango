// 1. get user order
// 2. get orderitems of an order
// 3. event listen clicked -> update div 

// document.getElementsByClassName('update-item')

// async function getOrderItems(){
//     let url = 'http://127.0.0.1:8000/api/orderItem-list/' 
    
//     let items = await fetch(url, {
//         method: 'GET',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken,
//         },
//         })
//         .then((res) => {
//             return res.json() // 需要 return 
//         })
//         .then((data) => {
//             // console.log('getOrderItem List:', data)
//             return data
//         })

//     return items
//     }

// async function renderItem(productId){
//     let items = await getOrderItems()
//     let item = items.filter(element => element['product'] == productId)[0]

//     if (item === undefined) {
//         // html 上有 prodcut id 的 cart-row, 但資料庫沒有 => 該 product 已經沒有在 cart 中
//         // 移除 該 product 的 cart-row 
//         cart_row = Array.from(document.querySelectorAll(`.cart-row`)).filter(element => element.dataset.product == productId)[0]
//         console.log('cart_row:', cart_row) // should not be empty 
//         cart_row.remove()
//     } else {
//         let item_quantity = item['quantity']
//         let item_total = item['get_total']
    
//         let qty_elements = document.getElementsByClassName('item-quantity')
//         let total_elements = document.getElementsByClassName('item-total')
//         // console.log('qty:eles:', [qty_elements])
//         let qty_element = Array.from(qty_elements).filter(element => element.dataset.product === productId)
//         let total_element = Array.from(total_elements).filter(element => element.dataset.product === productId)
//         // let item_total = document.getElementsByClassName('item-total')
//         // console.log(qty_element)
//         qty_element[0].innerText = item_quantity // Array to HTML element
//         total_element[0].innerText = item_total
//     }
    

    // for (let i=0; i<item_quantity.length; i++){
    //     if (item_quantity[i].dataset.product === productId){

    //     }
    //     // console.log('item total:', items[i]['get_total'])
    //     item_quantity[i].innerText = items[i]['quantity']
    //     item_total[i].innerText = items[i]['get_total']
    // }
//}

// let item_quantity = document.getElementsByClassName('item-quantity')
// let item_total = document.getElementsByClassName('item-total')