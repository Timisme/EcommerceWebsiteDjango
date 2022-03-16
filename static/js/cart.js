let updateBtns = document.getElementsByClassName('update-cart')

for (let i = 0; i< updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        let productId = this.dataset.product
        let action = this.dataset.action 
        console.log(productId, action) 

        if(user === 'AnonymousUser'){
            console.log('Not Logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })

}

function updateUserOrder(productId, action) {
    let url = '/update_item/' // urls 對應的 view 會 handle request 

    fetch(url, {
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
        location.reload() // 刷新頁面 沒效率
    })
}