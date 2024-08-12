from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    capital = models.IntegerField(default = 0.0)
    branches = models.CharField(max_length = 255)
    employees = models.IntegerField(default=0)
    projects = models.IntegerField(default = 0)

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
    asset_accusation_date = models.DateField(default = '2024-08-10')
    asset_name = models.CharField(max_length = 255)
    type_of_asset = models.CharField(max_length = 255)
    asset_price = models.IntegerField(default = 0)
    asset_source = models.CharField(max_length = 255)
    depreciation_rate = models.IntegerField(default = 0)

class Liabilities(models.Model):
    liablity_accusation_date = models.DateField(default = '2024-08-10')
    liability_name = models.CharField(max_length = 255)
    type_of_liability = models.CharField(max_length = 255)
    liability_source = models.CharField(max_length = 255)
    liability_amount = models.IntegerField(default = 0)
    interest_rate = models.IntegerField(default = 0)

class Debitors(models.Model):
    debit_accusation_date = models.DateField(default = '2024-08-10')
    debitor_name = models.CharField(max_length = 255)
    type_of_debit = models.CharField(max_length = 255)
    debit_source = models.CharField(max_length = 255)
    debited_amount = models.IntegerField(default = 0)
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
    staff_salary = models.IntegerField(default =0)
    staff_branch = models.CharField(max_length = 255)
    department = models.CharField(max_length = 255, choices = departments, null = False, blank = False)
    address = models.CharField(max_length = 255, null = False, blank = False)
    occupation = models.CharField(max_length = 255, choices = occupations, null = False, blank = False)
    # curriculum_vitae = models.FileField()

    