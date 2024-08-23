from django.db import models


# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length= 255, default= '')
    est = models.DateField(default='')
    headquaters = models.CharField(max_length= 255, default= '')
    founder = models.ForeignKey('users.CustomUser',related_name= 'organisations', on_delete= models.CASCADE, null= True, blank= True)

    def __str__(self):
        return self.name
    
    def no_companies(self):
        count = 0
        for item in self.companies.all():
            count += 1
        return count
    
    def total_expenses(self):
        expense = 0 
        for item in self.companies.all():
            expense += item.staff_salary()
        return expense
    
    def total_income(self):
        income = 0
        for item in self.companies.all():
            income += item.total_sales()
        return income
    
    def profit(self):
        profit = 0
        profit = self.total_income() - self.total_expenses()
        return profit
  
class Company(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='companies', on_delete= models.CASCADE, null= True, blank= True)
    company_name = models.CharField(max_length=255, default= '')
    starting_capital = models.IntegerField(default = 0.0)
    employees = models.IntegerField(default=0)
    

    def __str__(self):
        return self.company_name
    
    def no_employees(self):
        employee = self.employees
        employee = 0
        for item in self.staff.all():
            employee += 1
        return employee
    
    def no_branches(self):
        count = 0
        for item in self.branches.all():
            count += 1
        return count
    
    def no_projects(self):
        count = 0
        for item in self.branches.all():
            count += item.no_projects()
        return count
    
    def staff_salary(self):
        salary = 0
        for item in self.branches.all():
            salary += item.total_salary()
        return salary

    def total_sales(self):
        sale = 0
        for item in self.branches.all():
            sale += item.total_sales()
        sale += self.starting_capital
        return sale
    
    def net_worth(self):
        net_worth = 0
        return net_worth
    
class Branch(models.Model):
    company = models.ForeignKey('company.Company', related_name= 'branches', null=True, blank=True, on_delete= models.CASCADE)
    branch_name = models.CharField(max_length = 255, default= '')
    location = models.CharField(max_length = 255, default= '')
    branch_supervisor = models.ForeignKey('company.Staff', related_name= 'branches', null = True, blank= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.branch_name
    
    def no_projects(self):
        count = 0
        for item in self.projects.all():
            count += 1
        return count
    
    def total_salary(self):
        salary = 0
        for item in self.staffs.all():
            salary += item.monthly_salary
        return salary
    
    def total_sales(self):
        sale = 0
        for item in self.sales.all():
            sale += item.total_amount()
        return sale


class Projects(models.Model):
    branch = models.ForeignKey('company.Branch', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    date_started = models.DateField(default = '2024-08-10' )
    project_name = models.CharField(max_length = 255, unique = True, default= '')
    project_id = models.CharField(max_length = 255, default= '')
    project_supervisor = models.ForeignKey('users.CustomUser', related_name= 'projects', null = True, blank= True, on_delete= models.CASCADE)
    no_staff = models.IntegerField(default = 0)
    cash_in_hand = models.IntegerField(default = 0)

    def __str__(self):
        return self.project_name
    
    def net_worth(self):
        net_worth = self.cash_in_hand
        return net_worth

class Assets(models.Model):
    asset_type = (
        ('Current Asset', 'Current Asset'),
        ('Fixed Asset', 'Fixed Asset'),
    )
    projects = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True)
    asset_acquisition_date = models.DateField(default = '2024-08-10')
    asset_name = models.CharField(max_length = 255, default= '')
    type_of_asset = models.CharField(max_length = 255, choices= asset_type)
    asset_price = models.IntegerField(default = 0)
    asset_source = models.CharField(max_length = 255, default= '')
    depreciation_rate = models.IntegerField(default = 0)

    def __str__(self):
        return self.asset_name
    
class Liabilities(models.Model):
    liability_type = (
        ('Long-term', 'Long-term'),
        ('Short-term', 'Short-term'),
    )
    projects = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True)
    supplier = models.ForeignKey('transactions.Supplier', related_name='liabilities', on_delete= models.CASCADE, null= True, blank= True)
    liablity_acquisition_date = models.DateField(default = '2024-08-10')
    type_of_liability = models.CharField(max_length = 255, choices=liability_type)
    liability_source = models.CharField(max_length = 255, default= '')
    liability_amount = models.IntegerField(default = 0)
    interest_rate = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.supplier)

class Debitors(models.Model):
    debt_type = (
        ('', ''),
        ('Short Term', 'Short Term'),
        ('Long Term', 'Long Term'), 
    )
    assets = models.ForeignKey('company.Assets', on_delete= models.CASCADE, null= True, blank= True)
    debt_acquisition_date = models.DateField(default = '2024-08-10')
    debitor_name = models.ForeignKey('transactions.Customer', on_delete= models.CASCADE, related_name= 'debitors', null= True, blank= True)
    type_of_debt = models.CharField(max_length = 255, default= '', choices = debt_type)#TO ADD CHOICES
    debt_amount = models.IntegerField(default = 0)
    interest_rate = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.debitor_name

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
    company = models.ForeignKey('company.Company', on_delete= models.CASCADE, null= True, related_name= 'staff',  blank= True)
    staff_name = models.ForeignKey('users.CustomUser', on_delete= models.CASCADE, null= True, blank= True)

    staff_id = models.CharField(max_length = 255, default= '')
    monthly_salary = models.IntegerField(default = 0)
    staff_branch = models.ForeignKey('company.Branch', on_delete= models.CASCADE, related_name= 'staffs', null= True, blank= True)
    department = models.CharField(max_length = 255, choices = departments, null = False, blank = False)
    occupation = models.CharField(max_length = 255, choices = occupations, null = False, blank = False)
    # curriculum_vitae = models.FileField()

    def __str__(self):
        return str(self.staff_name)
    
    def total_salary(self):
        salary = 0
        for salary in Staff:
            salary += self.monthly_salary
        return salary

    
   
    
    
   
    
    
  