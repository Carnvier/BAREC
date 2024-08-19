from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    capital = models.IntegerField(default = 0.0)
    branches = models.CharField(max_length = 255)
    employees = models.IntegerField(default=0)
    projects = models.IntegerField(default = 0)

    def __str__(self):
        return self.company_name

class Projects(models.Model):
    date_started = models.DateField(default = '2024-08-10' )
    branch_name = models.CharField(max_length = 255)
    project_name = models.CharField(max_length = 255, unique = True)
    project_id = models.CharField(max_length = 255)
    project_supervisor = models.CharField(max_length = 255)
    no_staff = models.IntegerField(default = 0)
    cash_in_hand = models.IntegerField(default = 0)
    project_location = models.CharField(max_length = 255)

    def net_worth(self):
        net_worth = self.cash_in_hand
        return net_worth

class Assets(models.Model):
    asset_type = (
        ('Current Asset', 'Current Asset'),
        ('Fixed Asset', 'Fixed Asset'),
    )
    asset_acquisition_date = models.DateField(default = '2024-08-10')
    asset_name = models.CharField(max_length = 255)
    type_of_asset = models.CharField(max_length = 255, choices= asset_type)
    asset_price = models.IntegerField(default = 0)
    asset_source = models.CharField(max_length = 255)
    depreciation_rate = models.IntegerField(default = 0)

class Liabilities(models.Model):
    liability_type = (
        ('Long-term', 'Long-term'),
        ('Short-term', 'Short-term'),
    )
    liablity_acquisition_date = models.DateField(default = '2024-08-10')
    Creditor_name = models.CharField(max_length = 255)
    type_of_liability = models.CharField(max_length = 255, choices=liability_type)
    liability_source = models.CharField(max_length = 255)
    liability_amount = models.IntegerField(default = 0)
    interest_rate = models.IntegerField(default = 0)

class Debitors(models.Model):
    debt_acquisition_date = models.DateField(default = '2024-08-10')
    debitor_name = models.CharField(max_length = 255)
    type_of_debt = models.CharField(max_length = 255)
    debt_source = models.CharField(max_length = 255)
    debt_amount = models.IntegerField(default = 0)
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
    staff_id = models.CharField(max_length = 255)
    staff_name = models.CharField(max_length = 255)
    monthly_salary = models.IntegerField(default =0)
    staff_branch = models.CharField(max_length = 255)
    department = models.CharField(max_length = 255, choices = departments, null = False, blank = False)
    occupation = models.CharField(max_length = 255, choices = occupations, null = False, blank = False)
    # curriculum_vitae = models.FileField()

    def dob(self):
        dob = '19.03.2015'
        return dob
    
    def id_number(self):
        id_number = 'FN520491'
        return id_number
    
    def phone_number(self):
        phone_number = '+263 78 329 2829'
        return phone_number
    
    def project(self):
        project = 'Broiler Production'
        return project
    
    def address(self):
        address = '154 Gorosure, Harare, Zimbabwe'
        return address