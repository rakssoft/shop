from django.contrib import admin
from ecomapp.models import Category, Brand, Product, CartItem, Cart, Images


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Images)



# Register your models here.