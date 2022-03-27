# EcommerceWebsiteDjango
A ecommerce website featured with carts and payment functionality from Django 

# 功能
1. 購物車系統
2. 會員系統
3. 表單系統
4. 商品分類
5. 優惠券系統
6. Session 暫存購物車

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

## utils: cookieCart

1. 用 request.COOKIE 中 cart key load 成 json  
2. 創建預設 order (購物車總價、購物車總數、是否寄送)
3. 針對 cart 中每個 item 做 iteration 計算 2. 的數值
4. 回傳 items, order, cartItems

## cart.js 

* 利用 data-product / data-action 自訂義設定 DOM 物件屬性，利用 view render 將 context 渲染到 HTML 的 DOM 上
* JS 取得 DOM 物件後獲取該物件的 product-id 及 action，進行操作

* 只有 checkout 完成 order 才會是 complete

