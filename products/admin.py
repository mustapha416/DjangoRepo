from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')
    search_fields = ('code','description')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)