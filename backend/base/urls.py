from django.urls import path
from . import views



urlpatterns = [
    path('products',views.getProducts,name='products'),
    path('users',views.getUsers,name='userы'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/',views.registerUser,name='user_register'),
    path('users/profile',views.getUserProfile,name='user_profile'),
    path('products/<str:pk>/',views.getProduct,name='product'),
]