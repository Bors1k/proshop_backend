from django.urls import path
from base.views import order_views as views

urlpatterns = [
    path('add/',views.addOrderItem, name='order-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('orders/', views.getOrders, name='orders_all'),
    path('<str:pk>/', views.getOrderById, name='get-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='update-to-paid'),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='update-to-delivired'),
]