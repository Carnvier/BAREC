from django.contrib import admin
from .models import Company, Projects, Debtor, Creditor, Staff, Asset, Organisation, Branch, Purchases, Purchased_Item, Loan

# Register your models here.
admin.site.register(Organisation)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Projects)
admin.site.register(Debtor)
admin.site.register(Creditor)
admin.site.register(Staff)
admin.site.register(Asset)
admin.site.register(Purchases)
admin.site.register(Purchased_Item)
admin.site.register(Loan)