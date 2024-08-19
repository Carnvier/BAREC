from django.contrib import admin
from .models import Company, Projects, Debitors, Liabilities, Staff, Assets

# Register your models here.
admin.site.register(Company)
admin.site.register(Projects)
admin.site.register(Debitors)
admin.site.register(Liabilities)
admin.site.register(Staff)
admin.site.register(Assets)