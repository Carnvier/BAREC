from django import forms
from .models import SaleItem

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['sale', 'product', 'quantity', 'discount']

    def clean_quantity(self):
        sales  = self.cleaned_data.get('sale')
        discount = self.cleaned_data.get('discount')
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if product and quantity > product.quantity:
            raise forms.ValidationError('The entered quantity is greater than stock (quantity)')
        return quantity