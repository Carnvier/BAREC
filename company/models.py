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
    
    def organisation_id(self):
        return self.name[0] + f'{self.id:0004d}'
    
    def no_companies(self):
        count = 0
        for item in Company.objects.all():
            if self.name == item.organisation.name:
                count += 1
        return count
    
    def total_customers(self):
        count = 0
        for item in Customer.objects.all():
            if item.organisation.name == self.name:
                count += 1
        return count
    
    def total_expenses(self):
        expense = 0.0
        expense += self.monthly_staff_salary()
        for item in self.companies.all():
            if item.organisation.name == self.name:
                expense +=  item.starting_capital
        return expense
    
    def total_income(self):
        income = 0
        for item in self.companies.all():
            if item.organisation.name == self.name:        
                income += item.total_sales()
        return income
    
    def profit(self):
        profit = 0
        profit = self.total_income() - self.total_expenses()
        return profit
    
    def asset_value(self):
        asset = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:        
                asset += item.assets_value()
        return asset
    
    def monthly_staff_salary(self):
        salary = 0.0
        for item in self.staff.all():
            if item.organisation.name == self.name:
                salary += item.monthly_salary
        return salary
    
    def net_worth(self):
        net_worth = 0.0
        net_worth += self.total_income() - self.total_expenses()
        for item in self.companies.all():
            if item.organisation.name == self.name:
                net_worth += item.stock_value()
        return net_worth
  
class Company(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='companies', on_delete= models.CASCADE, null= True, blank= True)
    company_name = models.CharField(max_length=255, default= '', unique = True)
    starting_capital = models.IntegerField(default = 0.0)
    employees = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15, default= '')
    email = models.EmailField(max_length=50, default= '')
    CEO_name = models.ForeignKey('company.Staff', null=True, blank=True, on_delete= models.CASCADE, related_name='companies')

    def __str__(self):
        return self.company_name
    
    def get_absolute_url(self):
        return reverse_lazy('company-dashboard', args=[str(self.organisation.id)])
    
    def company_id(self):
        return self.company_name[0] + f'{self.id:0004d}'
    
    def stock_value(self):
        stock = 0.0
        for item in self.stocks.all(): 
            if item.company.company_name == self.company_name:
                stock += item.total_price()
        return stock
    
    def no_employees(self):
        employee = self.employees
        employee = 0
        if self.no_branches() > 0:
            for item in Staff.objects.all():
                if item.company.company_name == self.company_name:
                    employee += 1
        return employee
    
    def no_branches(self):
        count = 0
        for item in self.branches.all():
            if item.company.company_name == self.company_name:
                count += 1
        return count
    
    def no_projects(self):
        count = 0
        for item in self.branches.all():
            if item.company.company_name == self.company_name:
                count += item.no_projects()
        return count
    
    def staff_salary(self):
        salary = 0.0
        for item in self.branches.all():
            if item.company.company_name == self.company_name:
                salary += item.total_salary()
        return salary

    def total_sales(self):
        sale = 0.0
        for item in self.branches.all():
            if item.company.company_name == self.company_name:
                sale += item.total_sales()
        return float(sale)
    
    def total_expenses(self):
        expenses = self.staff_salary()
        return expenses
    
    def total_profit(self):
        profit = self.total_sales() + self.stock_value()  - self.total_expenses() 
        return profit
    
    def assets_value(self):
        asset = 0.0
        for item in self.branches.all():
            if item.company.company_name == self.company_name:
                asset += item.asset_value()
        return float(asset)

    def net_worth(self):
        net_worth = 0.0
        net_worth = self.total_sales() + self.stock_value() - self.staff_salary() - self.starting_capital 
        return net_worth
    
class Branch(models.Model):
    company = models.ForeignKey('company.Company', related_name= 'branches', null=True, blank=True, on_delete= models.CASCADE)
    branch_name = models.CharField(max_length = 255, default= '', unique=True)
    location = models.CharField(max_length = 255, default= '')
    branch_phone_number = models.CharField(max_length = 15, default = '')
    branch_supervisor = models.ForeignKey('company.Staff', related_name= 'branches', null = True, blank= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.branch_name
    
    def get_absolute_url(self):
        return reverse_lazy('branch-overview', args=[str(self.id)])
    
    def branch_id(self):
        branch_id = ''
        branch_id = self.branch_name[0] + self.company.company_name[0] + f'{self.id:0004d}'
        return branch_id
    
    def no_projects(self):
        count = 0
        for item in self.projects.all():
            if item.branch.branch_name == self.branch_name:
                count += 1
        return count
    
    def total_salary(self):
        salary = 0.0
        for item in self.staffs.all():
            if item.staff_branch.branch_name == self.branch_name:
                salary += item.monthly_salary
        return salary
    
    def branch_expenses(self):
        expenses = 0.0
        expenses += self.total_salary()
        return expenses
    
    def total_sales(self):
        sale = 0.0  
        for item in self.sales.all():
            if item.branch.branch_name == self.branch_name:
                sale += item.grand_total()
        return sale
    
    def total_branch_staff(self):
        staff = 0
        for item in self.projects.all():
            if item.branch.branch_name == self.branch_name:
                staff += item.project_staff()
        return staff
    
    def asset_value(self):
        asset = 0.0
        for item in self.assets.all():
            if item.branch.branch_name == self.branch_name:
                asset += item.asset_networth()
        return float(asset)
    
    def branch_income(self):
        income = 0.0
        income += self.total_sales()
        return income
    
    def branch_profit(self):
        profit = 0.0
        profit += self.branch_income() - self.branch_expenses()
        return profit

class Projects(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    branch = models.ForeignKey('company.Branch', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    date_started = models.DateField(default = '2024-08-10' )
    project_name = models.CharField(max_length = 255, unique = True, default= '')
    project_id = models.CharField(max_length = 255, default= '')
    project_supervisor = models.ForeignKey('users.CustomUser', related_name= 'projects', null = True, blank= True, on_delete= models.CASCADE)
    no_staff = models.IntegerField(default = 0)
    cash_in_hand = models.IntegerField(default = 0)

    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse_lazy('project-index', args=str(self.organisation.id))
    
    def total_cash_in_hand(self):
        cash = self.cash_in_hand
        for item in self.sales.all():
            if item.project.project_name == self.project_name:
                cash += item.grand_total()
        return cash

    def project_location(self):
        return self.branch.location

    def project_id(self):
        id = self.project_name[0] + self.branch.branch_name[0] + f'{self.id:0004d}'
        return id
    
    def net_worth(self):
        net_worth = 0
        net_worth += self.total_cash_in_hand()
        for item in self.assets.all():
            if item.projects.project_name == self.project_name:
                net_worth += item.asset_networth()
        return net_worth
    
    def project_staff(self):
        no_staff = self.no_staff
        for item in self.staffs.all():
            if item.staff_project.project_name == self.project_name:
                no_staff += 1
        return no_staff
    
    def project_staff_salary(self):
        salary = 0.0
        for item in self.staffs.all():
            if item.staff_project.project_name == self.project_name:
                salary += item.monthly_salary
        return salary
    
    def project_expenses(self):
        expenses = 0.0
        expenses += self.project_staff_salary()
        return expenses
    
    def fixed_assets(self):
        asset = 0.0
        for item in self.assets.all():
            if item.type_of_asset == 'Fixed Asset':
                asset += item.asset_networth()
        return asset
    
    def current_assets(self):
        asset = 0.0
        for item in self.assets.all():
            if item.type_of_asset == 'Current Asset':
                asset += item.asset_networth()
        return asset
    
    def total_assets(self):
        asset = 0.0
        asset += self.fixed_assets() + self.current_assets()
        return asset
    
    def long_liabilities(self):
        liability = 0.0
        for item in self.liabilities.all():
            if item.type_of_liability == 'Long-term':
                liability += item.total_liability_amount()
        return liability
    
    def short_liabilities(self):
        liability = 0.0
        for item in self.liabilities.all():
            if item.type_of_liability == 'Short-term':
                liability += item.total_liability_amount()
        return liability
    
    def total_liabilities(self):
        liability = 0.0
        liability += self.short_liabilities() + self.long_liabilities()
        return liability
    
    def no_sales(self):
        count = 0
        for item in self.sales.all():
            if item.project.project_name == self.project_name:
                count += 1
        return count
    
    def project_sales_income(self):
        sale = 0.0
        for item in self.sales.all():
            if item.project.project_name == self.project_name:
                sale += item.grand_total()
        return sale
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

    def __str__(self):
        return self.asset_name
    
    def get_absolute_url(self):
        return reverse_lazy('project-index', args=str(self.organisation.id))
    
    def asset_id(self):
        id = self.asset_name[0] + self.type_of_asset[0] + f'{self.id:0004d}'
        return id
    
    def asset_networth(self):
        value = 0.0
        if self.disposed == False:
            value = self.quantity * float(self.asset_value - (self.asset_value * self.depreciation_rate))
        return float(value)
    
    def total_assets_value(self):
        value =  0.0
        for item in Assets.objects.all():
            value += item.asset_networth()
        return value   
    
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
    type_of_liability = models.CharField(max_length = 255, choices=liability_type, default = 'Short-term')
    details = models.CharField(max_length = 50, default= '')
    liability_amount = models.IntegerField(default = 0)
    liability_paid_status = models.BooleanField(default = False)
    interest_rate = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.supplier)
    
    def get_absolute_url(self):
        return reverse_lazy('project-index', args=str(self.organisation.id))
    
    def liability_id(self):
        id = '' 
        if self.sources == True:
            id += self.sources[0] + self.projects[0] + f'{self.id:0004d}'
        else:
            id += f'{self.id:0004d}'
        return id

    def total_liability_amount(self):
        if self.liability_paid_status == False:
            liability = self.liability_amount + (100 * self.interest_rate)
        return liability

    def monthly_liability_amount(self):
        liability = 0
        for item in Liabilities.objects.all():
            liability += item.total_liability_amount()
        return liability
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

    def __str__(self) -> str:
        return self.debitor_name
    
    def debt_id(self):
        debt_id = self.debitor_name[0] + f'{self.id:0004d}'
        return debt_id
    
    def total_debt_amount(self):
        if self.debt_paid_status == False:
            total_debt = self.debt_amount * (100 + self.interest_rate)
        return total_debt
    
    def total_monthtly_debt_amount(self):
        total_monthly = 0
        for item in Debitors.objects.all():
            total_monthly += item.total_debt_amount()  
        return total_monthly

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

    def __str__(self):
        return str(self.staff_name)
    
    def get_absolute_url(self):
        return reverse_lazy('staff-index', args=str(self.staff_name.organisation.id))
    
    def monthly_total_salary(self):
        salary = 0
        for salary in Staff.objects.all():
            salary += self.monthly_salary
        return salary

    def staff_id_no(self):
        staff_id = self.id
        return staff_id
    
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

    def __str__(self):
        return self.organisation_name

   
class Purchases(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey('company.Staff', on_delete= models.CASCADE, default = '')
    source = models.CharField(max_length=255, default='')
    details = models.TextField(max_length=255, default = '')
    branch = models.ForeignKey('company.Branch', default='', related_name='purchases', on_delete= models.CASCADE)
    project = models.ForeignKey('company.Projects', default='', related_name='purchases', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.source
    
    def get_absolute_url(self):
        return reverse_lazy('purchased-items-view', args = [str(self.id)])
    
    def purchase_id(self):
        return self.branch.branch_name[0] + f'{self.id:0004d}'
    
    def sub_total(self):    
        total_price = 0.0
        for item in self.item_purchased.all():
            if item.purchase.purchase_id() == self.purchase_id():
                total_price += item.total_price()
        return total_price
    
    def processing_fee(self):
        fee = 0.0
        return fee
    
    def tax(self):
        tax = 0.0
        return tax
    
    def grand_total(self):
        total = 0.0
        total += self.sub_total() + self.processing_fee() + self.tax()
        return total
    
class Purchased_Item(models.Model):
    purchase = models.ForeignKey('company.Purchases', related_name='item_purchased', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255, default='')
    quantity = models.IntegerField(default=0)
    unit_price = models.IntegerField(default=0.0 )

    def __str__(self):
        return self.product_name
    
    def total_price(self):
        total = 0.0
        total += self.quantity * self.unit_price
        return total

    def get_absolute_url(self):
        return reverse_lazy('purchased-items-view', args=[str(self.purchase.id)])

  