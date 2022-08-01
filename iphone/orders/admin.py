from django.contrib import admin
from .models import Order
# Register your models here.

# ===> customizing the admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['iphone_types', 'order_status', 'quantity', 'created_at']
    list_filter = ['created_at', 'order_status', 'iphone_types']