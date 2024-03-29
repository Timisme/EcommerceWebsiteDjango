from django.urls import path 
from . import views 

# app_name = 'store'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('shop/', views.shop, name= 'shop'),
    path('shop/<str:category_pk>', views.shop, name= 'shop_category'),
    path('contact/', views.contact, name= 'contact'),
    path('cart/', views.cart, name= 'cart'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('account/', views.myaccount, name= 'account'),
    path('product_detail/<str:pk>', views.product_detail, name= 'product_detail'),
    path('coupon/', views.validateCoupon, name= 'coupon'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('process_order/', views.processOrder, name= 'process_order'),
]