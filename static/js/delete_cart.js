let deleteBtns = document.getElementsByClassName('cart-delete');

for (let i=0; i < deleteBtns.length; i++){
    let deleteBtn = deleteBtns[i]
    deleteBtn.addEventListener('click', async function(e){
        console.log('i:', i)
        e.preventDefault()
        await deleteOrderItem(deleteBtn.dataset.item)

        let tr_elements = document.getElementsByClassName('cart-row')
        let tr_element = Array.from(tr_elements).filter(element => element.dataset.product == deleteBtn.dataset.product)
        console.log('tr_element:', tr_element[0])
        tr_element[0].remove()
        console.log('element was removed')
    })
};

async function deleteOrderItem(item_id){
    url = `http://127.0.0.1:8000/api/orderItem-delete/${item_id}`
    await fetch(url,{
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    })
    .then(res => res.json())
    .then(console.log('item was deleted!'))
}