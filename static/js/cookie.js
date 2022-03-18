function getCookie(name){

    let cookieArr = document.cookie.split(";");

    for (let i= 0; i< cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");
        if(name == cookiePair[0].trim()){
            return decodeURIComponent(cookiePair[1]);
        }
    }

    return null; 
}

var cart = JSON.parse(getCookie('cart'))
console.log('Cart:', cart)

if (cart === null) {
    cart = {}
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/" 
}