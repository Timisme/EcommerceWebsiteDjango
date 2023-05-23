# My Ecommerce Website

An ecommerce website from Django (**Django Rest Framework** included)

## What features does it include?

1. Fast deployment with **docker-compose**
2. Rest api reference from **swagger**
3. Sending newsletter schedually Using **Celery**
4. Can fetch resources faster by caching data Using **Redis**
5. Using Session to store user's most recently viewed products
6. Using **Nginx** as web server to serve static files

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

> to build base image, run `docker build -t django-ecommerce-website-base:latest -f ./backend/docker/Dockerfile-base .`
> to build image, run `docker-compose build `
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
