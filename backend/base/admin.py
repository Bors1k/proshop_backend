from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from base import models

admin.site.register(models.Product)
admin.site.register(models.Review)
admin.site.register(models.ShippingAddress)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.UserProfile)