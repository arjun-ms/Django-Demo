from django.contrib import admin
from .models import Product,Offeres

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Offeres,OfferAdmin)
