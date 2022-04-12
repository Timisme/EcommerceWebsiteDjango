# EcommerceWebsiteDjango

An ecommerce website from Django (Django Rest Framework included)

# What features does it include?

1. Fast deployment with docker
2. Rest api reference from swagger
3. Sending newsletter schedually Using Celery 
4. Can fetch resources faster by caching data with Redis 
5. Using Session to store user's most recently viewed products    
6. Using Nginx as web server to server static files

# What can users do on the website? 

1. can login & logout 
2. can add products to the shopping cart 
3. can update & remove products from the shopping cart 
4. can send a contact forms to the backend 
5. can receive newsletter and get promotion code 
6. can paginate through the products 
7. can place an order and pay with paypal

# About Session and Cache
- session
    - session is created when a user views the product detail
- Cache
    - Cache is created when the home page is requested the first time

# Deployment

> To deploy, simply run `docker-compose up -d`





