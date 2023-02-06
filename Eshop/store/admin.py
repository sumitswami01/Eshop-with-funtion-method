from django.contrib import admin
from .models import Product, Category, Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
admin.site.register(Product, ProductAdmin)

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CatagoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password']
admin.site.register(Customer, CustomerAdmin)