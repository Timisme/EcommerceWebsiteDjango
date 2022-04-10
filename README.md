# EcommerceWebsiteDjango
A ecommerce website featured with carts and payment functionality from Django 

# 功能
1. 購物車系統
2. 會員系統
3. 表單系統
4. 商品分類
5. newsletter系統
6. Session 暫存購物車
7. Celery 
8. Redis as Cache
9. Nginx
10. docker
11. API

- session 使用
    - 儲存使用者有瀏覽 product-detail 頁面的 product
    - 顯示於 cart 頁面的 most viewed section

- cache 使用
    - home page 的 featured product `不常更動又常存取`，使用 cache 快速存取


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


# Cache 機制

## 為甚麼要 cache？

把不常改變的資料放到 cache，減少直接讀取後端資料庫，提升網站效能。

## redis 是甚麼？

In-memory 的 key-value 資料庫，優點在於效能高。但有 data loss 的問題，就適合 cache data。

## cache 常遇到的問題

* 只用 local cache, 多台 server cache 資料不同步，cache miss 較高，
* cache flow 應該是 
1. redis 拿資料 
2. 沒有的話其中一個 request 去 db 拿資料，存在 redis
3. 其他 request 就從 redis 拿資料
 

## @cache_page 做了甚麼？

1. cache the output of views 
2. cache the view's response 
3. requests from different url will be cached separately 
4. cache arg => what cache backend to use (from setting), by default using 'default' cache is used

## How to access caches? 

## redis conf 配置概念
1. daemonize: 指定 redis 是否要用守護線程方式啟動(啟動後 redis 會把 pid 寫到一個 pidfile 中)
2. 


# Session framework 
## 利用 Session 實踐匿名用戶狀態保存機制 (api 和 普通views)

1. By default, Django stores sessions in your database (using the model django.contrib.sessions.models.Session
2. cached session for faster performance 
* Set SESSION_ENGINE to "django.contrib.sessions.backends.cache" for a simple caching session store. Session data will be stored directly in your cache. 
* For persistent, cached data, set SESSION_ENGINE to "django.contrib.sessions.backends.cached_db". This uses a write-through cache – every write to the cache will also be written to the database. Session reads only use the database if the data is not already in the cache.
* By default, Django only saves to the session database when the session has been modified
* the SESSION_SAVE_EVERY_REQUEST setting to True. When set to True, Django will save the session to the database on every single request.

* By default, SESSION_EXPIRE_AT_BROWSER_CLOSE is set to False, which means session cookies will be stored in users’ browsers for as long as SESSION_COOKIE_AGE.

* This setting is a global default and can be overwritten at a per-session level by explicitly calling the set_expiry() method of request.session 

* user login in -> django.session db 新增資料，logout -> 刪除資料。如果沒有 logout，expired session data 要手動刪除：clearsessions (可以用 celery 定期執行)；如果是 cache db 就會自動刪除 stale data 

* 匿名用戶 session 流程
1. 每個對 order, orderitem 的 api 都加入 anonymous user session 機制
2. session 儲存 cart key, value = {'productid': {'quantity': 1},} 

### Session in views 

* When SessionMiddleware is activated, each HttpRequest object will have a session attribute, which is a dictionary-like object.

### Session in rest framework 



# drf-yasg Swagger

1. 測試 rest api 
2. swagger for testing, redoc for referencing 
3. 


# Celery 

- celery 4.0+ 不支援 windows：只能在 dev, test 環境起 worker，需要加 --pool=solo: celery -A <module> worker --pool=solo -l info，變成 single threaded

# Redis 
- `docker exec -it myredis /bin/sh` 進入容器
- `redis-cli` 使用 redis 指令
- `KEYS *` 列出所有 KEYS

# Web server 
- Django 常見的 Web Application Server 有 uWSGI、gunicorn。

# docker-compose 
- docker containers 之間連線：docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' myredis

# NGINX & uWSGI 
- the web client <-> the web server （ Nginx ） <-> unix socket <-> uWSGI <-> Django
- Nginx 負責靜態內容（html js css 圖片...... ），uWSGI 負責 Python 的動態內容。
- uWSGI 對於靜態內容處理的並不是很好（ 效能差 ），所以我們可以透過

    Nginx 來處理靜態內容，而且使用 Nginx 還有很多好處，
    Nginx 比起 uWSGI 能更好地處理靜態資源
    Nginx 可以設定 Cache 機制
    Nginx 可以設定 反向代理器
    Nginx 可以進行多台機器的負載平衡（ Load balance ）

- web server 好處
    - 保護 server 安全，避免直接對 server 攻擊
    - 可以做 cache 機制


