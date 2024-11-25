from django import forms
from .models import OrganisationRegistration

class OrganisationRegistrationForm(forms.ModelForm):
    class Meta:
        model = OrganisationRegistration
        fields = '__all__'
        exclude = ['status', 'registration_date']