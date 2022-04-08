let deleteBtns = document.getElementsByClassName('cart-delete');

for (let i=0; i < deleteBtns.length; i++){
    let deleteBtn = deleteBtns[i]
    deleteBtn.addEventListener('click', async function(e){
        e.preventDefault()
        await deleteOrderItem(deleteBtn.dataset.item)
        let tr_elements = document.getElementsByClassName('cart-row')
        let tr_element = Array.from(tr_elements).filter(element => element.dataset.product == deleteBtn.dataset.product)
        tr_element[0].remove()

        let orderId = await getCurrentOrderId();
        await renderOrder(orderId);
    })
};

async function deleteOrderItem(item_id){
    url = `http://127.0.0.1:8000/api/orderItem/${item_id}`
    await fetch(url,{
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    // .then(res => res.json())
    .then(console.log('item was deleted!'))
}