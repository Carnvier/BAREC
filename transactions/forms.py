from django import forms
from .models import SaleItem
from django.core.exceptions import ValidationError

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['sale', 'product', 'quantity', 'discount']

    def clean_quantity(self):
        sales  = self.cleaned_data.get('sale')
        discount = self.cleaned_data.get('discount')
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        # try:
        #     product = SaleItem.objects.get(id=product.id)
        # except SaleItem.DoesNotExist:
        #     raise ValidationError('Product does not exist')


        if product and quantity > product.quantity:
            raise forms.ValidationError(f'The entered quantity is greater than stock. Current stock: {product.quantity}')
        return quantity