import imp
from django.contrib import admin
from .models import Product, Review,ShippingAddress,OrderItem,Order
# Register your models here.

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)