let addToCartBtns = document.getElementsByClassName('add-to-cart');

for (let i = 0; i< addToCartBtns.length; i++) {
    addToCartBtns[i].addEventListener('click', async function(e) {
        e.preventDefault();

        // 該按鈕需要得到 input quantity 資訊
        if (addToCartBtns[i].classList.contains('update-quantity')){
            value = await getItemQauntity('item-quantity-input')
            addToCartBtns[i].dataset.quantity = value
            console.log('this btn quantity has been updated to:', this.dataset.quantity)
        }

        let productId = this.dataset.product;
        let action = this.dataset.action ;
        let quantity = this.dataset.quantity;
        // console.log(productId, action) 

        await updateUserOrder(productId, action, quantity); // 更新 db 
    })
};

function getItemQauntity(input_tag_id){
    input = document.getElementById(input_tag_id)
    return input.value
}; 

// function renderQuantity(input_id){
//     let btn = document.getElementsByClassName('update-quantity')
//     btn.addEventListener('click', async function(e){
//         e.preventDefault();
//         value = await getItemQauntity(input_id)

//         btn.dataset.quantity = value;
//     }) 
// }
