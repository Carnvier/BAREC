from django.contrib import admin
from .models import Customer, Sales, Stock, Supplier, SaleItem

# Register your models here.
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Sales)
admin.site.register(Stock)
admin.site.register(SaleItem)
