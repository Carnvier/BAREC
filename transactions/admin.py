from django.contrib import admin
from .models import Customer, Sales, Expenses, Stock, Supplier

# Register your models here.
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Sales)
admin.site.register(Expenses)
admin.site.register(Stock)
