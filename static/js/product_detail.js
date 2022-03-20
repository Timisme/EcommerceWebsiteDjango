
let DetailCartBtn = document.getElementById("detail_cart_btn_{{product.id}}");
console.log(DetailCartBtn)
console.log('id: {{product.id}}')
DetailCartBtn.addEventListener('click', function(e){
    e.preventDefault()
})