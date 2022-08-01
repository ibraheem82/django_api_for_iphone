from django.urls import path
from . import views

# ! http://127.0.0.1:8000/auth/jwt/create <==== use this to post a 
urlpatterns = [
    path('', views.OrderCreatListView.as_view(), name='orders'),
    # ! when testing you should use ==> [api-phones/{your url }/{number}/]
    path('order-details/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    # ! when testing you should use ==> [api-phones/{your url }/{number}/]
    path('orders-update-status/<int:order_id>/', views.UpdateOrderStatus.as_view(), name='update_order_status'),
    path('users/<int:user_id>/orders/', views.UserOrdersView.as_view(), name='users_orders'),
]