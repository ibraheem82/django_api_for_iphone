from ast import Or
from django.shortcuts import render,get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from . models import Order

# /-----------------------------------------------------\#
# TODO * Making permissions from django restframe work ===> [ IsAuthenticated ] <===
# /------------------------------------------------------\#
from rest_framework.permissions import IsAuthenticated



# ! you have to specify [AUTH_USER_MODEL = 'authentication.User'] in your settings.py file to be able to use the [get_user_model]
from django.contrib.auth import get_user_model 


User = get_user_model()

# Create your views here.

class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        # rest_framewok allows us to get our http status
        return Response(data={"message": "This is an api for all iphones"}, status = status.HTTP_200_OK)

























class OrderCreatListView(generics.GenericAPIView):
    # * ===> this will help us validate the data that we want to pass in our api
    serializer_class  = serializers.OrderCreationSerializer
    queryset = Order.objects.all()
    
    # TODO: specifing the list of permission classes
    permission_classes =[IsAuthenticated]
    
    def get(self, request):

        # #* ===> this will return the queryset of all orders
        
        orders = Order.objects.all()

        # ! Must specify (many =True) when returning a queryset
        serializer = self.serializer_class(instance=orders, many = True)
        
        # ===> anytime we add an instance to the serializer, we can access the data by getting the serializer
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        
        # ===> to place our order
        # ! the function will enable us place how orders !
    def post(self, request):
        # ===> get access to the request [data] that the user is sending to our [api]
        data = request.data
        
        # ===> Using [serializer] to validate the users data
        serializer = self.serializer_class(data=data)
        
        # * when the user purchase on the website he should be set to a user
        user = request.user

        # * Check if the [serializer] is valid
        if serializer.is_valid():
            
            # TODO: make sure your user exist before setting them
            # TODO: only logged in users should be able to place order
            # * setting the user to customer, because their is a relationship between the customer and the order
            serializer.save(customer = user)

            # # A resoucre has been created
            return Response(data  = serializer.data, status = status.HTTP_201_CREATED)
        
        
        # ! incase you have errors with you serializer []
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)

























class OrderDetailView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer
    
    permission_classes =[IsAuthenticated]
    
    
    def get(self, request, order_id):
        # ! To get a specific order by it [id]
        # ! Get the order primary key
        order = get_object_or_404(Order, pk=order_id)
        
        
        # * Returning the instance
        serializer  = self.serializer_class(instance=order)

        return Response(data=serializer.data, status = status.HTTP_200_OK)



    def put(self, request, order_id):
        data = request.data
        
        order = get_object_or_404(Order, pk=order_id)
    #     # ! [data] is the data you want to update it with.
        serializer = self.serializer_class(data = data, instance=order)
        if serializer.is_valid():
            serializer.save()

            return Response(data = serializer.data, status = status.HTTP_200_OK)
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
        # ! The user can only be accessed if the end point is protected
        # user  = request.user
        
        # serializer = self.serializer_class(data = data)

        # if serializer.is_valid():
        #     serializer.save(customer = user)

        #     return Response(data = serializer.data, status = status.HTTP_200_OK)
        
        # return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    
    
    
    def delete(self, request, order_id):
        order =  get_object_or_404(Order, pk=order_id)
        order.delete()
        # ! [HTTP_204_NO_CONTENT] means that you have deleted the request.
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

class UpdateOrderStatus(generics.GenericAPIView):
    serializer_class = serializers.OrderStatusUpdateSerializer
    
    
    def put(self, request, order_id):
        order =  get_object_or_404(Order, pk=order_id)
        data  = request.data
        # ! [instance = order] we are updating the [order] which is a  model.
        serializer = self.serializer_class(data = data, instance = order)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_200_OK)
        return Response(data= serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
class UserOrdersView(generics.GenericAPIView):
    serializer_class = serializers.OrderDetailSerializer

    def get(self, request, user_id):
        # ! Getting access to the currently logged in user.
        # ! Specify the user id.
        # user  = request.user
        user = User.objects.get(pk=user_id)
        
        
        # ! Get the order specific for that current user
        orders = Order.objects.all().filter(customer= user)
        
        serializer = self.serializer_class(instance = orders, many= True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

