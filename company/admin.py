from django.contrib import admin
from .models import Company, Projects, Debitors, Liabilities, Staff, Assets, Organisation, Branch, Purchases, Purchased_Item

# Register your models here.
admin.site.register(Organisation)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Projects)
admin.site.register(Debitors)
admin.site.register(Liabilities)
admin.site.register(Staff)
admin.site.register(Assets)
admin.site.register(Purchases)
admin.site.register(Purchased_Item)