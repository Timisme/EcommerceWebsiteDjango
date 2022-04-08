const couponBtn = document.querySelector('.coupon-btn')
const couponInput = document.querySelector('.coupon-input')
// console.log(couponBtn)
couponBtn.addEventListener('click', async function(e){
    e.preventDefault();
    let code = couponInput.value;
    let url = '/coupon/';
    let data = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'code': code,
        }),
    })
    .then((res) => { return res.json()})
    .then((data) => { 
        return data
    })  

    if (data['discount_type'] === 'shipping'){
        // let shipping = document.querySelector('#cart-shipping')
        await updateOrderShipping(data['discount'])
        location.reload();
    } else {
        console.log('data:', data)
    }
})

async function updateOrderShipping(value){
    let currentOrderId = await getCurrentOrderId()
    let url = `/api/order/${currentOrderId}`

    await fetch(url, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'shipping_fee': value
        }),
    })
    .then((res) => {return res.json()})
    .then((data) => {
        console.log('data after update shipping:', data)
    })
}