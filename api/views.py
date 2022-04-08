# from django.shortcuts import render
from ast import Or
from xmlrpc.client import ResponseError
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import *
from store.models import * 
from store.utils  import cartData
from rest_framework import status
from django.http import Http404

class OrderList(APIView):
    # permissions.IsAdminUser
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer = request.user.customer
        # print('customer:', customer)
        queryset = Order.objects.filter(customer__name__iexact = customer).order_by('id')
        serializer = OrderSerializer(queryset, many= True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, many= False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class OrderDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Order.objects.get(pk= pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        order = self.get_object(pk)
        serializer = OrderSerializer(instance= order, many= False)
        return Response(serializer.data)

    def put(self, request, pk):

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        order = self.get_object(pk)
        serializer = OrderSerializer(
            instance=order,
            data= request.data,
            many= False
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderItemList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, order_id):
        try:
            queryset = OrderItem.objects.filter(order__iexact = order_id)
            serializer = OrderItemSerializer(queryset, many= True)
            return Response(serializer.data)
        except:
            raise Http404
    def post(self, request, order_id):
        serializer = OrderItemSerializer(data = request.data, many= False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderItemDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk= pk)
        except OrderItem.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        orderitem = self.get_object(pk)
        serializer = OrderSerializer(instance= orderitem, many= False)
        return Response(serializer.data)

    def put(self, request, pk):

        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        orderitem = self.get_object(pk)
        serializer = OrderItemSerializer(
            instance=orderitem,
            data= request.data,
            many= False
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        orderitem = self.get_object(pk)
        orderitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# order, created = Order.objects.get_or_create(customer= customer, complete= False)
        

        

# @api_view(['GET'])
# def orderItemDetail(request, pk):
#     orderItem = OrderItem.objects.get(id= pk)
#     serializer = OrderItemSerializer(instance= orderItem, many= False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def orderItemCreate(request):
#     serializer = OrderItemSerializer(
#         data= request.data,
#         many= False)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['PATCH'])
# def orderItemUpdate(request, pk):
#     orderItem = OrderItem.objects.get(id= pk)
#     serializer = OrderItemSerializer(
#         instance= orderItem, 
#         data= request.data,
#         many= False)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def orderItemDelete(request, pk):
#     orderItem = OrderItem.objects.get(id= pk)
#     orderItem.delete()
#     return Response('Item successfully deleted')

# @api_view(['GET'])
# def orderDetail(request, pk):
#     order = Order.objects.get(id= pk)
#     serializer = OrderSerializer(instance= order, many= False)
#     return Response(serializer.data) 

# @api_view(['GET'])
# def orderCurrent(request):
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer= customer, complete= False)
#     serializer = OrderSerializer(
#         instance= order,
#         many= False)
#     return Response(serializer.data)

# @api_view(['GET'])
# def listOrderItems(request):
#     customer = request.user.customer
#     order, created = Order.objects.get_or_create(customer= customer, complete= False)
#     orderItems = order.orderitem_set.all()
#     serializer = OrderItemSerializer(orderItems, many= True)
#     return Response(serializer.data)
    