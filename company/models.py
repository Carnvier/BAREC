from django.db import models
from django.utils.timezone import now
from transactions.models import Sales, Customer, Stock
from django.urls import reverse_lazy


# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length= 255, default= '')
    est = models.DateField(default='')
    headquaters = models.CharField(max_length= 255, default= '')
    founder = models.ForeignKey('users.CustomUser',related_name= 'organisations', on_delete= models.CASCADE, null= True, blank= True)
    organisation_email = models.EmailField(max_length= 255, blank= True, null=True, default='')
    organisation_phone_number = models.CharField(max_length= 255, blank= True, default='')
    organisation_description = models.TextField(default= '')
    motive = models.TextField(max_length= 255, default = '')

    def __str__(self):
        return self.name

    def total_sales(self):
        sale = 0.0
        for item in self.sales.all():
            if item.organisation.name == self.name:
                sale += item.grand_total()
        return sale
    
    def sales_returns(self):
        sale = 0.0
        for item in self.sales_item.all():
            if item.organisation.name == self.name:
                if item.returned == True:
                    sale += item.returned_total()
        return sale

    def net_sales(self):
        sale = 0.0
        sale += self.total_sales() - self.sales_returns()
        return sale
    
    def total_purchases(self):
        total = 0.0
        for item in self.purchases.all():
            if item.organisation.name == self.name:
                total += item.grand_total()
        return total    
  
class Company(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='companies', on_delete= models.CASCADE, null= True, blank= True)
    company_name = models.CharField(max_length=255, default= '', unique = True)
    starting_capital = models.IntegerField(default = 0.0)
    employees = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15, default= '')
    email = models.EmailField(max_length=50, default= '')
    CEO_name = models.ForeignKey('company.Staff', null=True, blank=True, on_delete= models.CASCADE, related_name='companies')

class Branch(models.Model):
    company = models.ForeignKey('company.Company', related_name= 'branches', null=True, blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length = 255, default= '', unique=True)
    location = models.CharField(max_length = 255, default= '')
    phone_number = models.CharField(max_length = 15, default = '')
    branch_supervisor = models.ForeignKey('company.Staff', related_name= 'branches', null = True, blank= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

class Projects(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    branch = models.ForeignKey('company.Branch', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    date_started = models.DateField(default = '2024-08-10' )
    name = models.CharField(max_length = 255, unique = True, default= '')
    supervisor = models.ForeignKey('users.CustomUser', related_name= 'projects', null = True, blank= True, on_delete= models.CASCADE)
    no_staff = models.IntegerField(default = 0)
    cash_in_hand = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('project-index', args=(self.organisation.id))
    
    def project_id(self):
        project = str(self.organisation.name[0]) + str(self.name[0]) + f'{self.id:0004d}'
        return project
    
    def total_purchases(self):
        total = 0.00
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.grand_total()
        return total
        

class Assets(models.Model):
    asset_type = (
        ('Current Asset', 'Current Asset'),
        ('Fixed Asset', 'Fixed Asset'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name='assets', on_delete= models.CASCADE, null= True, blank= True)
    date_brought_in = models.DateField(default = now)
    projects = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True, related_name = 'assets')
    source = models.ForeignKey('company.Purchased_Item', on_delete= models.CASCADE, null=True, blank= True, related_name= 'assets')
    asset_name = models.CharField(max_length = 255, default= '')
    type_of_asset = models.CharField(max_length = 255, choices= asset_type, default = 'Current Asset')
    quantity = models.IntegerField(default= 0)
    acquistion_price = models.IntegerField(default = 0)
    asset_value = models.IntegerField(default = 0)
    asset_source = models.CharField(max_length = 255, default= '')
    depreciation_rate = models.IntegerField(default = 0)
    disposed = models.BooleanField(default = False)
    branch = models.ForeignKey('company.Branch', null=True, on_delete=models.CASCADE, blank = True, related_name = 'assets')

class Liabilities(models.Model):
    liability_type = (
        ('Long-term', 'Long-term'),
        ('Short-term', 'Short-term'),
    )
    liability_sources = (
        ('Individual', 'Individual'),
        ('Corporate', 'Corporate'),
        ('Other', 'Other'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name='liabilities', on_delete= models.CASCADE, null= True, blank= True)
    projects = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True, related_name='liabilities')
    sources = models.CharField(max_length = 50, default = 'Other', choices=liability_sources)
    liablity_acquisition_date = models.DateField(default = '2024-08-10')
    creditor =  models.CharField(max_length = 50, default= '')
    phone_number = models.CharField(max_length = 15, default= '')
    email = models.EmailField(max_length = 50, null = True, blank = True)
    type_of_liability = models.CharField(max_length = 255, choices=liability_type, default = 'Short-term')
    details = models.CharField(max_length = 50, default= '')
    liability_amount = models.IntegerField(default = 0)
    liability_paid_status = models.BooleanField(default = False)
    interest_rate = models.IntegerField(default = 0)

class Debitors(models.Model):
    debt_type = (
        ('Short Term', 'Short Term'),
        ('Long Term', 'Long Term'), 
    )
    assets = models.ForeignKey('company.Assets', on_delete= models.CASCADE, null= True, blank= True)
    debt_acquisition_date = models.DateField(default = '2024-08-10')
    debitor_name = models.ForeignKey('transactions.Customer', on_delete= models.CASCADE, related_name= 'debitors', null= True, blank= True)
    type_of_debt = models.CharField(max_length = 255, choices = debt_type, default = 'Short Term')
    debt_amount = models.IntegerField(default = 0)
    debt_paid_status = models.BooleanField(default = False)
    interest_rate = models.IntegerField(default = 0)

class Staff(models.Model):
    departments = (
        ('Sales and Marketing', 'Sales and Marketing'),
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Administration and Development', 'Administration and Development'),
        ('Other', 'Other'),
        ('Not Applicable', 'Not Applicable'),
    )
    occupations = (
        ('Junior', 'Junior'),
        ('Customer', 'Customer'),
        ('Senior', 'Senior'),
        ('Cashier', 'Cashier'),
        ('Field Employee', 'Field Employee'),
        ('Manager', 'Manager'),
        ('CEO', 'CEO'),
        ('Software Developer', 'Software Developer'),
        ('Other', 'Other'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, null= True, related_name= 'staff',  blank= True)
    company = models.ForeignKey('company.Company', on_delete= models.CASCADE, null= True, related_name= 'staff',  blank= True)
    staff_name = models.ForeignKey('users.CustomUser', on_delete= models.CASCADE, null= True, blank= True, related_name= 'staff')
    staff_id = models.CharField(max_length = 255, default= '')
    monthly_salary = models.IntegerField(default = 0)
    staff_branch = models.ForeignKey('company.Branch', on_delete= models.CASCADE, related_name= 'staffs', null= True, blank= True, default = '')
    staff_project = models.ForeignKey('company.Projects', on_delete= models.CASCADE, related_name = 'staffs', null= True, blank = True)
    department = models.CharField(max_length = 255, choices = departments, null = False, blank = False, default='IT')
    occupation = models.CharField(max_length = 255, choices = occupations, null = False, blank = False, default='Junior')
    # curriculum_vitae = models.FileField()
    
class CompanyRegistration(models.Model):
    first_name = models.CharField(max_length=255, default= '')
    last_name = models.CharField(max_length=255, default= '')
    ID_Number = models.CharField(max_length = 20, null = True, blank = True)
    personal_address = models.CharField(max_length = 255, default='')
    preffered_username = models.CharField(max_length=255,  default= '')
    phone_number = models.CharField(max_length=255, default= '')
    email = models.EmailField(max_length=255, default= '')
    organisation_name = models.CharField(max_length=255,  default= '')
    est = models.DateField(default = now)
    headquaters = models.CharField(max_length= 255, default= '')
    organisation_email = models.EmailField(max_length= 255, blank= True, null=True, default='')
    organisation_phone_number = models.CharField(max_length= 255, blank= True, default='')
    company_description = models.TextField(default= '')
    motive = models.TextField(max_length= 255, default = '')
   
class Purchases(models.Model):
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, null= True, related_name= 'purchases',  blank= True)
    date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey('users.CustomUser', on_delete= models.CASCADE, default = '', related_name='purchases', null= True, blank=True)
    branch = models.ForeignKey('company.Branch', default='', related_name='purchases', on_delete= models.CASCADE)
    project = models.ForeignKey('company.Projects', default='', related_name='purchases', on_delete= models.CASCADE)
    source = models.CharField(max_length=255, default='')
    details = models.TextField(max_length=255, default = '')
    tax_percentage = models.IntegerField(default= 0.00)
    

    def __str__(self):
        return self.purchase_id()

    def get_absolute_url(self):
        return reverse_lazy('purchased-items-view', args=[str(self.id)])
    
    def purchase_id(self):
        purchase = self.organisation.name[0] + self.source[0] + f'{self.id:0004d}'
        return purchase
    
    def stock_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase_type == 'Stock':
                total += item.total_amount()
        return total
    
    def asset_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase_type == 'Assets':
                total += item.total_amount()
        return total
    
    def overheads_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase_type == 'Overheads':
                total += item.total_amount()
        return total
    
    def sub_total(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase.purchase_id() == self.purchase_id():
                total += item.total_amount()
        return total
    
    def tax_amount(self):
        tax = 0.00
        tax += (self.sub_total() * (self.tax_percentage/100))
        tax =  round(tax, 2)
        return tax

    
    def grand_total(self):
        total = 0.00
        total += self.sub_total() + self.tax_amount()
        return total

    
class Purchased_Item(models.Model):
    purchase_types = (
        ('Stock', 'Stock'),
        ('Overheads', 'Overheads'),
        ('Assets', 'Assets'),
    )
    purchase = models.ForeignKey('company.Purchases', related_name='item_purchased', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, default='')
    purchase_type = models.CharField(max_length=255, default = 'Stock', choices = purchase_types)
    quantity = models.FloatField(default=0.00)
    unit_price = models.FloatField(default=0.00)

    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse_lazy('purchased-items-view', args=[str(self.purchase.id)])
    
    def total_amount(self):
        total = 0.00
        total += round(self.quantity * self.unit_price, 2)
        return total
    
        
class Loan(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    receiver = models.CharField(max_length=50)
    amount = models.FloatField(default= 0.00)
    details = models.TextField(default='')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)