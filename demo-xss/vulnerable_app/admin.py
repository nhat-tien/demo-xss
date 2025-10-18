from django.contrib import admin

# Register your models here.

from .models import Product, User, CustomerInfo, Category, Brand, Product, Comment

admin.site.register(Product)
admin.site.register(User)
admin.site.register(CustomerInfo)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Comment)
