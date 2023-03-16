from django.contrib import admin
from API.models import Product, Retailer, Wholeseller, Manufacturer

# Register your models here.
admin.site.register(Product)
admin.site.register(Retailer)
admin.site.register(Wholeseller)
admin.site.register(Manufacturer)