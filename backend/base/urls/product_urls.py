from django.urls import path
from base.views import product_view as views

urlpatterns = [
    path('',views.getProducts,name='products'),
    path('create/',views.createProduct,name='product_create'),
    path('upload_image/',views.uploadImage,name='product_uload_img'),
    path('<str:pk>/',views.getProduct,name='product'),
    path('<str:pk>/delete/',views.delProductById,name='product_delete'),
    path('<str:pk>/update/',views.updateProduct,name='product_update'),
]