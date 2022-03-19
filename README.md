# EcommerceWebsiteDjango
A ecommerce website featured with carts and payment functionality from Django 

## Paypal 金流

1. 使用 Paypal Sandbox 測試
2. 創建 personal 和 business account 
3. 創建 app, 取得 client api (有了 biz client id 交易後才知道金流給誰)
4. 修改 paypal script amount value (由 order的總金額 取得)

## utils:cartData

* 使用者已登入
    1. 取得使用者 Customer obj
    2. 取得該 Customer 對應的 Order, 如果沒有 Order 則創建
    3. 取得該 Order 所有的 OrderItems, 存為 items
    4. 取得該 Order 的商品數 (cartItems)
* 使用者未登入
    1. 利用 cookieCart 得到 user 的 cookieData 

    return json dict 紀錄 items, order, cartItems