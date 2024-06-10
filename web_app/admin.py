from django.contrib import admin

from .models import Order, Product, Category

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)