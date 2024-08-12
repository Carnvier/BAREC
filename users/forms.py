from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'ID_Number', 'D_O_B', 'address','email', 'phone_number', )

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'