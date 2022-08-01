# from dataclasses import field
# from statistics import quantiles
from . models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    iphone_types = serializers.CharField(max_length=40)
    # the [order_status] can be updated by the users or the admin users
    order_status = serializers.HiddenField(default = 'PENDING')
    quantity = serializers.IntegerField()
    # * Fields needed
    class Meta:
        model = Order
        fields = ['id','iphone_types', 'order_status', 'quantity'] 
        




class OrderDetailSerializer(serializers.ModelSerializer):
    iphone_types = serializers.CharField(max_length=40)
    # the [order_status] can be updated by the users or the admin users
    order_status = serializers.CharField(default = 'PENDING')
    # description = serializers.TextField(null=True)
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()
    

    
    # * Fields needed
    class Meta:
        model = Order
        fields = ['iphone_types', 'order_status', 'quantity', 'created_at', 'update_at']
        
        
        
        
        
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField(default = 'PENDING')
    
    class Meta:
        model = Order
        fields = ['order_status']