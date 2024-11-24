from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.timezone import now

# Create your models here.
class Stock(models.Model):
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, related_name= 'stocks', null= True, blank= True)
    date = models.DateField(default= now)
    asset = models.ForeignKey('company.Asset', on_delete= models.CASCADE, related_name= 'stocks', null= True, blank= True)
    product_name = models.CharField(max_length = 50, default='')
    product_description = models.TextField()
    quantity = models.FloatField(default=0.0)
    product_price = models.FloatField( default = 0.0)
    project = models.ForeignKey('company.Projects', null = True, blank = True, on_delete = models.CASCADE, related_name='stocks')

    def __str__(self):
        return str(self.product_name) 
    
    def product_id(self):
        return self.id
    
    def total_product_value(self):
        total = 0.00
        total += (self.quantity * self.product_price)
        return total

class Supplier(models.Model):
    supplier_type = (
    ('Individual', 'Individual'),
    ('Cooperate', 'Cooperate'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, related_name= 'suppliers',  null= True, blank= True)
    name = models.CharField(max_length=255)
    supply = models.CharField(max_length=255, default= '')
    type_of_supplier = models.CharField(max_length=255, choices=supplier_type)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255) 

    def __str__(self):
        return self.name
    
    def supplier_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id

class Customer(models.Model):
    customer_type = (
    ('Individual', 'Individual'),
    ('Cooperate', 'Cooperate'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, related_name= 'customers',  null= True, blank= True)
    name = models.CharField(max_length=255, default='')
    type_of_customer = models.CharField(max_length=255, choices=customer_type)
    address = models.CharField(max_length=255, default= '')
    phone_number = models.CharField(max_length=255, default='')
    email = models.EmailField(max_length=255, default='', blank= True, null=True) 
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
 
    def customer_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id

class Sales(models.Model):
    date_of_sale  = models.DateTimeField(auto_now_add=True)
    organisation = models.ForeignKey('company.Organisation', blank=True, null=True, on_delete=models.CASCADE, related_name = 'sales')
    sale_details = models.CharField( max_length= 255)
    customer = models.ForeignKey('transactions.Customer', blank=True, null=True, on_delete=models.CASCADE, related_name = 'sales')
    sales_rep = models.ForeignKey( 'company.Staff', related_name= 'sales', on_delete= models.CASCADE, null= True, blank= True)
    project = models.ForeignKey( 'company.Projects', related_name= 'sales', on_delete= models.CASCADE, null= True, blank= True, default='')
    tax_status = models.BooleanField( default=False)
    processing_fee = models.FloatField( default= 0.0)

    def __str__(self):
        return str(self.sale_id())
    
    def sale_id(self):
        sale_id = self.project.name[0] + self.project.branch.name[0] + f'{self.id:0004d}'
        return sale_id
    
    def sub_total(self):
        total_amount = 0.0
        for item in self.sales_item.all():
            if item.sale.id == self.id:
                total_amount = total_amount + item.total_amount()
                if item.returned == True:
                    total_amount -= item.returned_total()
        return total_amount
    
    def tax_amount(self):
        tax = 0.0
        if self.tax_status == True:
            tax += (self.sub_total() * (self.organisation.tax/100))
        return tax
    
    def grand_total(self):
        total = 0.0
        total += self.sub_total() + self.tax() + self.processing_fee
        return total
    
class SaleItem(models.Model):
    organisation = models.ForeignKey('company.Organisation', blank=True, null=True, on_delete=models.CASCADE, related_name = 'sales_item')
    sale = models.ForeignKey('transactions.Sales', on_delete= models.CASCADE, null=True, blank = True, related_name='sales_item')
    product = models.ForeignKey('transactions.Stock', on_delete= models.CASCADE, null= True, blank= True, related_name='sales_item')
    quantity = models.IntegerField( default= 0)
    discount = models.FloatField( default= 0.0)
    returned = models.BooleanField( default= False)
    returned_quantity= models.IntegerField( default= 0)

    def __str__(self):
        return self.product.product_name
    
    def get_absolute_url(self):
        return reverse_lazy('sales-items-detail', args=str(self.product.id))
    
    def total_amount(self):
        total = 0.0
        total = total + float(self.quantity * self.product.product_price)
        return total
    
    def returned_total(self):
        total = 0.0
        if self.returned == True:
            total += (self.returned_quantity * self.product.product_price)
        return total
    




# class Expenses(models.Model):
#     expense_type = (
#         ('Running Expense', 'Running Expense'),
#         ('Repairs', 'Repairs'),
#         ('Salary', 'Salary'),
#         ('Loans', 'Loans'),
#     )
#     liabilities = models.ForeignKey('company.Liabilities', on_delete= models.CASCADE, related_name= 'expenses',  null= True, blank= True)
#     expense_id =models.CharField(max_length=255)
#     type = models.CharField(max_length=255, choices=expense_type)
#     details = models.TextField(max_length=255)
#     quantity = models.IntegerField(default = 0)
#     unit_price = models.IntegerField(default = 0.0)
#     total_amount = models.IntegerField(default= 0.0)

#     def __str__(self):
#         return self.type
