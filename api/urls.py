from django.urls import path 
from . import views


# TO BE UPDATED 0330
urlpatterns = [
    path('order/', views.OrderList.as_view(), name= 'order-list'),
    path('order/<str:pk>', views.OrderDetail.as_view(), name= 'order-detail'),
    path('orderItemList/<str:order_id>', views.OrderItemList.as_view(), name= 'orderItem-list'),
    path('orderItem/<str:pk>', views.OrderItemDetail.as_view(), name= 'orderItem-detail'),
]