from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your models here.
class Stock(models.Model):
    product_name = models.ForeignKey('company.Assets', on_delete= models.CASCADE, related_name= 'stocks', null= True, blank= True)
    product_id = models.CharField(max_length= 255, default = '')
    product_description = models.TextField()
    quantity = models.IntegerField(default=0.0)
    new_stock = models.IntegerField(default= 0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.product_name)  

    def branch_net_worth(self):
        net_worth = 100
        return net_worth
    
class Supplier(models.Model):
    supplier_type = (
    ('Individual', 'Individual'),
    ('Cooperate', 'Cooperate'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, related_name= 'suppliers',  null= True, blank= True)
    supplier_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    supply = models.CharField(max_length=255, default= '')
    type_of_supplier = models.CharField(max_length=255, choices=supplier_type)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255) 

    def __str__(self):
        return self.name

class Customer(models.Model):
    customer_type = (
    ('Individual', 'Individual'),
    ('Cooperate', 'Cooperate'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, related_name= 'customers',  null= True, blank= True)
    customer_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type_of_customer = models.CharField(max_length=255, choices=customer_type)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255) 

    def __str__(self):
        return self.name
 

class Sales(models.Model):
    product = models.ForeignKey('transactions.Stock', on_delete= models.CASCADE, null= True, blank= True)
    date_of_sale  = models.DateTimeField(auto_now_add=True)
    sale_id = models.CharField(max_length=255, default = '')
    sale_details = models.CharField( max_length= 255)
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE, related_name = 'sales')
    quantity = models.IntegerField( default= 0)
    discount = models.IntegerField( default= 0.0)
    sales_rep = models.ForeignKey( 'company.Staff', related_name= 'sales', on_delete= models.CASCADE, null= True, blank= True)
    branch = models.ForeignKey( 'company.Branch', related_name= 'sales', on_delete= models.CASCADE, null= True, blank= True)

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse_lazy('sales-history')
    
    def total_amount(self):
        total_amount = self.product.price * self.quantity
        return total_amount
    
    def sale_total_amount(self):
        sale_total_amount = 0
        sale_total_amount += self.total_amount()
        return sale_total_amount
    
class Expenses(models.Model):
    expense_type = (
        ('Running Expense', 'Running Expense'),
        ('Repairs', 'Repairs'),
        ('Salary', 'Salary'),
        ('Loans', 'Loans'),
    )
    liabilities = models.ForeignKey('company.Liabilities', on_delete= models.CASCADE, related_name= 'expenses',  null= True, blank= True)
    expense_id =models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=expense_type)
    details = models.TextField(max_length=255)
    quantity = models.IntegerField(default = 0)
    unit_price = models.IntegerField(default = 0.0)
    total_amount = models.IntegerField(default= 0.0)

    def __str__(self):
        return self.type
