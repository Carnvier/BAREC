from django.contrib import admin
from django.db import models
from .models import OrganisationRegistration, Organisation, Company, Branch, Projects, Asset, Creditor, Debtor, Staff, Salary, Purchases, PurchasedItem, Expense, Income

# Register your models here.
admin.site.register(OrganisationRegistration)
admin.site.register(Organisation)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Projects)
admin.site.register(Asset)
admin.site.register(Creditor)
admin.site.register(Debtor)
admin.site.register(Staff)
admin.site.register(Salary)
admin.site.register(Purchases)
admin.site.register(PurchasedItem)
admin.site.register(Expense)
admin.site.register(Income)