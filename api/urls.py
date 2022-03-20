from django.urls import path 
from . import views

urlpatterns = [
    path('orderItem-detail/<str:pk>', views.orderItemDetail, name= 'orderItem-detail'),
    path('orderItem-create/', views.orderItemCreate, name= 'orderItem-create'),
    path('orderItem-update/<str:pk>', views.orderItemUpdate, name= 'orderItem-update'),
    path('orderItem-delete/<str:pk>', views.orderItemDelete, name= 'orderItem-delete'),
    path('order-detail/<str:pk>', views.orderDetail, name= 'order-detail'),
    path('order-current/', views.orderCurrent, name= 'order-current'),
]