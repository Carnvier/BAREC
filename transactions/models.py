from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from users.models import CustomUser

# Create your models here.
class Stock(models.Model):
    product_id = models.CharField(max_length= 255)
    product_name = models.CharField(max_length= 255)
    product_description = models.TextField()
    quantity = models.IntegerField(default=0.0)
    stock_brought_in = models.IntegerField(default= 0)
    price = models.FloatField(default=0.0)
    project = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name  

    def branch_net_worth(self):
        net_worth = 100
        return net_worth

class Customer(models.Model):
    customer_type = (
    ('Individual', 'Individual'),
    ('Cooperate', 'Cooperate'),
    )
    customer_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type_of_customer = models.CharField(max_length=255, choices=customer_type)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255) 

 

class Sales(models.Model):
    date_of_sale  = models.DateTimeField(auto_now_add=True)
    sale_id = models.CharField(max_length=255, default = '')
    product  = models.ForeignKey(Stock, related_name = 'products', on_delete=models.CASCADE)
    sale_details = models.CharField( max_length= 255)
    quantity = models.IntegerField( default= 0)
    discount = models.IntegerField( default= 0.0)
    sales_rep = models.ForeignKey( get_user_model(), on_delete= models.CASCADE)
    branch = models.CharField( max_length= 255)

    def get_absolute_url(self):
        return reverse_lazy('sales-history')
    
    def total_amount(self):
        total_amount = self.product.price * self.quantity
        return total_amount
    
    def customer_name(self):
         customer_name = self.customer.name
    
    def sale_total_amount(self):
        sale_total_amount = 0
        sale_total_amount += self.total_amount()
        return sale_total_amount
    
class Expenses(models.Model):
    expense_id =models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    details = models.TextField(max_length=255)
    quantity = models.IntegerField(default = 0)
    unit_price = models.IntegerField(default = 0.0)
    total_amount = models.IntegerField(default= 0.0)
