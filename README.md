# My Ecommerce Website

An ecommerce website from Django (__Django Rest Framework__ included)

## What features does it include?

1. Fast deployment with __docker-compose__
2. Rest api reference from __swagger__
3. Sending newsletter schedually Using __Celery__ 
4. Can fetch resources faster by caching data Using __Redis__
5. Using Session to store user's most recently viewed products    
6. Using __Nginx__ as web server to serve static files

## What can users do on the website? 

1. can login & logout 
2. can add products to the shopping cart 
3. can update & remove products from the shopping cart 
4. can send a contact forms to the backend 
5. can receive newsletter and get promotion code 
6. can paginate through the products 
7. can place orders and pay with paypal

### About Session and Cache
- session
    - Session is created when an user views the product detail
- Cache
    - Cache is created when the home page is requested for the first time

## Deployment
> To deploy, simply run `docker-compose up -d`

## APIs 
> Use url `http://127.0.0.1:8080/swagger/` to look up the rest api documentation

## ScreenShots 

### Product List Page
![](https://i.imgur.com/F2NTbxD.jpg)

### Login Page
![](https://i.imgur.com/aSCwDxQ.png)

### Cart Page
![](https://i.imgur.com/MczKrGT.png)

### Checkout Page
![](https://i.imgur.com/m6PWZt4.png)

### Most Recently viewd Section
![](https://i.imgur.com/CsHxl2q.png)





