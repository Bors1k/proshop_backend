from django.urls import path
from base.views import product_view as views

urlpatterns = [
    path('',views.getProducts,name='products'),
    path('<str:pk>/',views.getProduct,name='product'),
]