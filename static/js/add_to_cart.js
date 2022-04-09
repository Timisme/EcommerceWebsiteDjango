// 1. 新增至購物車按鈕
// 2. 如果是 detail 畫面，有指定商品數量，則該 Btn 商品數量同步更新
// 3. call url 更新後端 order 資訊
// 4. 如果在 cart 頁面點擊 add_to_cart，則 reload 頁面

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

        if (addToCartBtns[i].classList.contains('reload')){
            location.reload();
        }
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
