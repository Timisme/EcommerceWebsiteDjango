# from django.shortcuts import render
from xmlrpc.client import ResponseError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from store.models import * 

@api_view(['GET'])
def orderItemDetail(request, pk):
    orderItem = OrderItem.objects.get(id= pk)
    serializer = OrderItemSerializer(instance= orderItem, many= False)
    return Response(serializer.data)

@api_view(['POST'])
def orderItemCreate(request):
    serializer = OrderItemSerializer(
        data= request.data,
        many= False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def orderItemUpdate(request, pk):
    orderItem = OrderItem.objects.get(id= pk)
    serializer = OrderItemSerializer(
        instance= orderItem, 
        data= request.data,
        many= False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def orderItemDelete(request, pk):
    orderItem = OrderItem.objects.get(id= pk)
    orderItem.delete()
    return Response('Item successfully deleted')

@api_view(['GET'])
def orderDetail(request, pk):
    order = Order.objects.get(id= pk)
    serializer = OrderSerializer(instance= order, many= False)
    return Response(serializer.data) 

@api_view(['GET'])
def orderCurrent(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer= customer, complete= False)
    serializer = OrderSerializer(
        instance= order,
        many= False)
    return Response(serializer.data)