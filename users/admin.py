from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {
            'fields': (  'ID_Number', 'D_O_B', 'address', 'phone_number', 'organisation', )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)