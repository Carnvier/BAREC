from django.db import models
from django.utils.timezone import now
from django.urls import reverse_lazy, reverse


# Create your models here.
class OrganisationRegistration(models.Model):
    reg_status = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    )
    first_name = models.CharField(max_length=255, default= '')
    last_name = models.CharField(max_length=255, default= '')
    ID_Number = models.CharField(max_length = 20, null = True, blank = True)
    personal_address = models.CharField(max_length = 255, default='')
    preffered_username = models.CharField(max_length=255,  default= '')
    founder_DOB = models.DateField(default= now)
    founder_phone_number = models.CharField(max_length=255, default= '')
    founder_email = models.EmailField(max_length=255, default= '')
    organisation_name = models.CharField(max_length=255,  default= '')
    est = models.DateField(default = now)
    organisation_email = models.EmailField(max_length= 255, blank= True, null=True, default='')
    organisation_phone_number = models.CharField(max_length= 255, blank= True, default='')
    organisation_description = models.TextField(default= '')
    motive = models.TextField(max_length= 255, default = '')
    headquarters = models.CharField(max_length= 255, default= '')

    status = models.CharField(max_length= 255, default = 'Pending', choices = reg_status)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organisation_name
   
    def registration_id(self):
        id  = self.organisation_name[0] + self.first_name[0] + self.last_name[0] + f'{self.id:0004d}'
        return id

    def founder_name(self):
        name = self.first_name + ' ' + self.last_name
        return name
    
class Organisation(models.Model):
    name = models.CharField(max_length= 255, default= '')
    est = models.DateField(default='')
    headquarters = models.CharField(max_length= 255, default= '')
    founder = models.ForeignKey('users.CustomUser',related_name= 'organisations', on_delete= models.CASCADE, null= True, blank= True)
    organisation_email = models.EmailField(max_length= 255, blank= True, null=True, default='')
    organisation_phone_number = models.CharField(max_length= 255, blank= True, default='')
    organisation_description = models.TextField(default= '')
    motive = models.TextField(max_length= 255, default = '')
    tax = models.FloatField(default= 0.0)

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
    
    def organisation_id(self):
        id = self.name[0] + self.founder[0] + f'{self.id:0004d}'
        return id
    
    def no_companies(self):
        total = 0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += 1
        return total
    
    def total_customers(self):
        total = 0
        for item in self.customers.all():
            if item.organisation.name == self.name:
                total += 1
        return total
    
     #Assets
    def total_acquisition_price(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.total_acquisition_price()
        return total

    def total_depreciation(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.total_depreciation()
        return total
    
    def total_assets(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.total_assets()
        return total
    
    #Stock
    def total_stock(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.total_stock()
        return total
    
    # Sales
    def total_tax_amount(self):
        tax = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                tax += item.total_tax_amount()
        return tax

    def sales_grand_total(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.grand_total()
        return total
    
    # Creditors
    def total_credits(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_credits()
        return total
    
    def total_interest(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_interest()
        return total

    def total_amount_paid(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_amount_paid()
        return total
    
    #Debitors
    def total_debts(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_debts()
        return total

    def total_interest(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_interest()
        return total
    
    def total_debt_paid(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_amount_paid()
        return total
    
    # Staff
    def total_salary_earned(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_salary_earned()
        return total
    
    def total_salary_paid(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.total_salary_paid()
        return total

    # Purchases
    def stock_purchases(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                    total += item.stock_purchases()
        return total

    def taxed_stock_purchases(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.taxed_stock_purchases()
        return total
    
    def fixed_asset_purchase(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.fixed_asset_purchase()
        return total
    
    def taxed_fixed_asset_purchases(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.taxed_fixed_asset_purchases()
        return total
    
    def manufacturing_purchase(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.manufacturing_purchase()
        return total

    def taxed_manufacturing_purchase(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.taxed_manufacturing_purchase()
        return total

    def overheads_purchase(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.overheads_purchase()
        return total
    
    def taxed_overheads_purchase(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.taxed_overheads_purchase()
        return total
    
    def total_tax_amount(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.total_tax_amount()
        return total
    
    def purchases_grand_total(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.grand_total()
        return total
    
    def total_expenses(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.total_expenses()
        return total
    
    def total_income(self):
        total = 0.0
        total += self.total_debt_paid() + self.sales_grand_total() 
        return total
    
    def profit(self):
        total = 0.0
        total -= self.total_expenses() + self.total_income()
        return total

    def net_worth(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.net_worth()
        return total

    def cash_in_hand(self):
        total = 0.0
        for item in self.companies.all():
            if item.organisation.name == self.name:
                total += item.cash_in_hand()
        return total
  
class Company(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='companies', on_delete= models.CASCADE, null= True, blank= True)
    name = models.CharField(max_length=255, default= '', unique = True)
    starting_capital = models.IntegerField(default = 0.0)
    phone_number = models.CharField(max_length=15, default= '')
    email = models.EmailField(max_length=50, default= '')
    CEO_name = models.ForeignKey('company.Staff', null=True, blank=True, on_delete= models.CASCADE, related_name='companies')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('company-overview', args=[str(self.organisation.id)])

    def no_employees(self):
        total = 0
        for item in self.staff.all():
            if item.company.name == self.name:
                total += 1
        return total
    
    def company_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id
    
     #Assets
    def total_acquisition_price(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.total_acquisition_price()
        return total

    def total_depreciation(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.total_depreciation()
        return total
    
    def total_assets(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.total_assets()
        return total
    
    #Stock
    def total_stock(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.total_stock()
        return total
    
    # Sales
    def total_tax_amount(self):
        tax = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                tax += item.total_tax_amount()
        return tax

    def sales_grand_total(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.grand_total()
        return total
    
    # Creditors
    def total_credits(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_credits()
        return total
    
    def total_interest(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_interest()
        return total

    def total_amount_paid(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_amount_paid()
        return total
    
    #Debitors
    def total_debts(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_debts()
        return total

    def total_interest(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_interest()
        return total
    
    def total_amount_paid(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_amount_paid()
        return total
    
    # Staff
    def total_salary_earned(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_salary_earned()
        return total
    
    def total_salary_paid(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.total_salary_paid()
        return total

    def total_salary_unpaid(self):
        total = self.total_salary_earned() -self.total_salary_paid()
        return total

    # Purchases
    def stock_purchases(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                    total += item.stock_purchases()
        return total

    def taxed_stock_purchases(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.taxed_stock_purchases()
        return total
    
    def fixed_asset_purchase(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.fixed_asset_purchase()
        return total
    
    def taxed_fixed_asset_purchases(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.taxed_fixed_asset_purchases()
        return total
    
    def manufacturing_purchase(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.manufacturing_purchase()
        return total

    def taxed_manufacturing_purchase(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.taxed_manufacturing_purchase()
        return total

    def overheads_purchase(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.overheads_purchase()
        return total
    
    def taxed_overheads_purchase(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.taxed_overheads_purchase()
        return total
    
    def total_tax_amount(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.total_tax_amount()
        return total
    
    def grand_total(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.grand_total()
        return total
    
    def total_expenses(self):
        total = 0.0
        return total
    
    def net_worth(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.net_worth()
        return total
    
    def cash_in_hand(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.cash_in_hand()
        return total
    
    def no_branches(self):
        total = 0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += 1
        return total

    def no_projects(self):
        total = 0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.no_projects()
        return total
    
    def total_profit(self):
        total = 0.0
        for item in self.branches.all():
            if item.company.name == self.name:
                total += item.total_profit()
        return total

class Branch(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='branches', on_delete= models.CASCADE, null= True, blank= True)
    company = models.ForeignKey('company.Company', related_name= 'branches', null=True, blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length = 255, default= '', unique=True)
    location = models.CharField(max_length = 255, default= '')
    phone_number = models.CharField(max_length = 15, default = '')
    branch_supervisor = models.ForeignKey('company.Staff', related_name= 'branches', null = True, blank= True, on_delete= models.CASCADE)

    def __str__(self):
        return self.name
    
    def branch_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id
    
     #Assets
    def total_acquisition_price(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.total_acquisition_price()
        return total

    def total_depreciation(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.total_depreciation()
        return total
    
    def total_assets(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.total_assets()
        return total
    
    #Stock
    def total_stock(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.total_stock()
        return total
    
    # Sales
    def total_tax_amount(self):
        tax = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                tax += item.total_tax_amount()
        return tax

    def grand_total(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.grand_total()
        return total
    
    # Creditors
    def total_credits(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_credits()
        return total
    
    def total_interest(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_interest()
        return total

    def total_amount_paid(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_amount_paid()
        return total
    
    #Debitors
    def total_debts(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_debts()
        return total

    def total_interest(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_interest()
        return total
    
    def total_amount_paid(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_amount_paid()
        return total
    
    # Staff
    def total_salary_earned(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_salary_earned()
        return total
    
    def total_salary_paid(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.total_salary_paid()
        return total

    # Purchases
    def stock_purchases(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                    total += item.stock_purchases()
        return total

    def taxed_stock_purchases(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.taxed_stock_purchases()
        return total
    
    def fixed_asset_purchase(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.fixed_asset_purchase()
        return total
    
    def taxed_fixed_asset_purchases(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.taxed_fixed_asset_purchases()
        return total
    
    def manufacturing_purchase(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.manufacturing_purchase()
        return total

    def taxed_manufacturing_purchase(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.taxed_manufacturing_purchase()
        return total

    def overheads_purchase(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.overheads_purchase()
        return total
    
    def taxed_overheads_purchase(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.taxed_overheads_purchase()
        return total
    
    def total_tax_amount(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.total_tax_amount()
        return total
    
    def grand_total(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.grand_total()
        return total

    def no_projects(self):
        total = 0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += 1
        return total
    
    def total_profit(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.total_profit()
        return total

    def net_worth(self):
        total = 0.0
        for item in self.projects.all():
            if item.branch.name == self.name:
                total += item.net_worth()
        return total


class Projects(models.Model):
    organisation = models.ForeignKey('company.Organisation', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    branch = models.ForeignKey('company.Branch', related_name='projects', on_delete= models.CASCADE, null= True, blank= True)
    date_started = models.DateField(default = '2024-08-10' )
    name = models.CharField(max_length = 255, unique = True, default= '')
    supervisor = models.ForeignKey('users.CustomUser', related_name= 'projects', null = True, blank= True, on_delete= models.CASCADE)
    no_staff = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
    
    def project_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id
    
    #Assets
    def total_acquisition_price(self):
        total = 0.0
        for item in self.assets.all():
            if item.project.name == self.name:
                total += item.total_acquisition_price()
        return total

    def total_depreciation(self):
        total = 0.0
        for item in self.assets.all():
            if item.project.name == self.name:
                total += item.total_depreciation()
        return total
    
    def total_assets(self):
        total = 0.0
        for item in self.assets.all():
            if item.project.name == self.name:
                total += item.total_asset_value
        return total
    
    #Stock
    def total_stock(self):
        total = 0.0
        for item in self.stocks.all():
            if item.project.name == self.name:
                total += item.total_product_value()
        return total
    
    # Sales
    def total_tax_amount(self):
        tax = 0.0
        for item in self.sales.all():
            if item.project.name == self.name:
                tax += item.tax_amount()
        return tax

    def grand_total(self):
        total = 0.0
        for item in self.sales.all():
            if item.project.name == self.name:
                total += item.grand_total()
        return total
    
    # Creditors
    def total_credits(self):
        total = 0.0
        for item in self.creditors.all():
            if item.project.name == self.name:
                if item.credit_paid_status == False:
                    total += item.credit_amount - item.credit_amount_paid + self.credit_interest()
        return total
    
    def total_interest(self):
        total = 0.0
        for item in self.expenses.all():
            if item.project.name == self.name:
                if item.type == 'Credit Interest':
                    total += item.total_expense()
        return total

    def total_amount_paid(self):
        total = 0.0
        for item in self.creditors.all():
            if item.project.name == self.name:
                    total += item.credit_amount_paid
        return total
    
    #Debitors
    def total_debts(self):
        total = 0.0
        for item in self.debtors.all():
             if item.project.name == self.name:
                if item.paid_status == False:
                    total += item.amount - item.amount_paid + self.debt_interest_amount()
        return total

    def total_interest(self):
        total = 0.0
        for item in self.incomes.all():
            if item.project.name == self.name:
                if item.type == 'Debit Interest':
                    total += item.total_income
        return total
    
    def total_amount_paid(self):
        total = 0.0
        for item in self.debtors.all():
            if item.project.name == self.name:
                    total += item.amount_paid
        return total
    
    # Staff
    def total_salary_earned(self):
        total = 0.0
        for item in self.staffs.all():
            if item.project.name == self.name:
                total += item.total_salary_earned()
        return total
    
    def total_salary_paid(self):
        total = 0.0
        for item in self.staffs.all():
            if item.project.name == self.name:
                total += item.total_salary_paid()
        return total

    # Purchases
    def stock_purchases(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.stock_purchase()
        return total

    def taxed_stock_purchases(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.taxed_stock_purchase()
        return total
    
    def fixed_asset_purchase(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.fixed_asset_purchase()
        return total
    
    def taxed_fixed_asset_purchases(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.taxed_fixed_asset_purchases()
        return total
    
    def manufacturing_purchase(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.manufacturing_purchase()
        return total

    def taxed_manufacturing_purchase(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.taxed_manufacturing_purchases()
        return total

    def overheads_purchase(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.overheads_purchase()
        return total
    
    def taxed_overheads_purchase(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.taxed_overhead_purchase()
        return total
    
    def total_tax_amount(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.tax_amount()
        return total
    
    def grand_total(self):
        total = 0.0
        for item in self.purchases.all():
            if item.project.name == self.name:
                total += item.grand_total()
        return total
    
    # Expenses
    def total_expenses(self):
        total = 0.0
        for item in self.expenses.all():
            if item.project.name == self.name:
                total += item.total_expenses()
        return total
    
    def expenses_grand_total(self):
        total = 0.0
        total += self.total_expenses() 
    
    # Income
    def total_income(self):
        total = 0.0
        for item in self.incomes.all():
            if item.project.name == self.name:
                total += item.total_income()
        return total
class Asset(models.Model):
    asset_type = (
        ('Current Asset', 'Current Asset'),
        ('Fixed Asset', 'Fixed Asset'),
    )
    asset_statuses = (
        ('Active', 'Active'),
        ('Depreciated', 'Depreciated'),
        ('Disposed', 'Disposed'),
    )
    depreciation_periods = (
        ('Weekly', 'Weekly'),
        ('Bi-weekly', 'Bi-weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half-Yearly', 'Half-Yearly'),
        ('Yearly', 'Yearly'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name='assets', on_delete= models.CASCADE, null= True, blank= True)
    date_brought_in = models.DateField(default = now)
    projects = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True, related_name = 'assets')
    source = models.CharField(max_length=50, default='')
    asset_name = models.CharField(max_length = 255, default= '')
    type_of_asset = models.CharField(max_length = 255, choices= asset_type, default = 'Current Asset')
    quantity = models.IntegerField(default= 0)
    acquistion_price = models.IntegerField(default = 0)
    asset_value = models.IntegerField(default = 0)
    asset_source = models.CharField(max_length = 255, default= '')
    depreciation_period = models.CharField(max_length=50, choices= depreciation_periods, default= 'Yearly' )
    depreciation_rate = models.IntegerField(default = 0)
    asset_status = models.CharField(max_length=50, choices=asset_statuses, default = 'Active')


    def __str__(self):
        return self.asset_name
    
    def asset_id(self):
        id = self.organisation.name[0] + self.asset_name[0] + f'{self.id:0004d}'
        return id
    
    def total_acqusition_price(self):
        total = 0.0
        total += (self.acquistion_price * self.quantity)
        return total
    
    def total_asset_value(self):
        total = 0.0
        total += (self.asset_value * self.quantity)
        return total
    
    def total_depreciation(self):
        total = 0.0
        total += (self.total_asset_value() * (self.depreciation_rate / 100))
        return total

    def unit_depreciation(self):
        total = 0.0
        total += (self.asset_value * (self.depreciation_rate / 100))
        return total
    
class Creditor(models.Model):
    credit_types = (
        ('Long-term', 'Long-term'),
        ('Short-term', 'Short-term'),
    )
    credit_source = (
        ('Individual', 'Individual'),
        ('Corporate', 'Corporate'),
        ('Other', 'Other'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name='creditors', on_delete= models.CASCADE, null= True, blank= True)
    project = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True, related_name='creditors')
    sources = models.CharField(max_length = 50, default = 'Other', choices=credit_source)
    credit_acquisition_date = models.DateField(default = '2024-08-10')
    creditor =  models.CharField(max_length = 50, default= '')
    phone_number = models.CharField(max_length = 15, default= '')
    email = models.EmailField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length = 255,default='')
    credit_type = models.CharField(max_length = 255, choices=credit_types, default = 'Short-term')
    details = models.CharField(max_length = 50, default= '')
    credit_amount = models.IntegerField(default = 0)
    credit_paid_status = models.BooleanField(default = False)
    interest_rate = models.IntegerField(default = 0)
    credit_amount_paid = models.FloatField(default = 0.0)

    def __str__(self):
        return self.creditor
    
    def credit_interest(self):
        total = 0.0
        total += (self.credit_amount * (self.interest_rate/100))
        return total


class Debtor(models.Model):
    debt_type = (
        ('Short Term', 'Short Term'),
        ('Long Term', 'Long Term'), 
    )
    interest_periods = (
        ('Weekly', 'Weekly'),
        ('Bi-weekly', 'Bi-weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half-Yearly', 'Half-Yearly'),
        ('Yearly', 'Yearly'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, null= True, related_name= 'debtors',  blank= True)
    project = models.ForeignKey('company.Projects', on_delete= models.CASCADE, null= True, blank= True, related_name='debtors')
    assets = models.ForeignKey('company.Asset', on_delete= models.CASCADE, null= True, blank= True)
    debt_acquisition_date = models.DateField(auto_now_add= True)
    debtor = models.ForeignKey('transactions.Customer', on_delete= models.CASCADE, related_name= 'debtors', null= True, blank= True)
    receiver = models.CharField(max_length=50)
    type_of_debt = models.CharField(max_length = 255, choices = debt_type, default = 'Short Term')
    details = models.TextField(default='')
    amount = models.IntegerField(default = 0)
    paid_status = models.BooleanField(default = False)
    interest_period = models.CharField(max_length = 50, choices = interest_periods, default = 'Monthly')
    interest_rate = models.IntegerField(default = 0)
    amount_paid = models.FloatField(default=0.00)

    def __str__(self):
        return self.debtor
    
    def debt_id(self):
        id = self.organisation.name[0] + self.debtor[0] + f'{self.id:0004d}'
        return id

    def debt_interest_amount(self):
        total = 0.00
        total += (self.amount * (self.interest_rate/100))
        return total

class Staff(models.Model):
    departments = (
        ('Sales and Marketing', 'Sales and Marketing'),
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Administration and Development', 'Administration and Development'),
        ('Other', 'Other'),
        ('Not Applicable', 'Not Applicable'),
    )
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, null= True, related_name= 'staff',  blank= True)
    company = models.ForeignKey('company.Company', on_delete= models.CASCADE, null= True, related_name= 'staff',  blank= True)
    employment_date = models.DateTimeField(auto_now_add=True, null=True, blank= True)
    staff_name = models.ForeignKey('users.CustomUser', on_delete= models.CASCADE, null= True, blank= True, related_name= 'staff')
    project = models.ForeignKey('company.Projects', on_delete= models.CASCADE, related_name = 'staffs', null= True, blank = True, default = '')
    active = models.BooleanField(default=False)
    department = models.CharField(max_length = 255, choices = departments, null = False, blank = False, default='IT')
    occupation = models.CharField(max_length = 30,  null = False, blank = False, default='')
    # curriculum_vitae = models.FileField()

    def __str__(self):
        return self.staff_name
    
    def staff_id(self):
        id = self.organisation.name[0] + self.staff_name + f'{self.id:0004d}'
        return id
    
    def total_salary_earned(self):
        total = 0.00
        for i in self.salaries.all():
            if i.staff.staff_name == self.staff_name:
                    total += i.earned_salary
        return total  

    def total_paid_salary(self):
        total = 0.00
        for i in self.salaries.all():
            if i.staff.staff_name == self.staff_name:
                    total += i.amount_paid
        return total     
    
class Salary(models.Model):
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, null= True, related_name= 'salaries',  blank= True)
    staff = models.ForeignKey('company.Staff', related_name='salaries', null = True, blank=True, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default = False)
    amount_paid = models.FloatField(default = 0.0)
    earned_salary = models.FloatField(default = 0.0)

    def __str__(self):
        return self.staff.staff_name
    
    def salary_id(self):
        id = self.organisation.name[0] + self.staff.staff_name[0] + f'{self.id:0004d}'
        return id
    
class Purchases(models.Model):
    organisation = models.ForeignKey('company.Organisation', on_delete= models.CASCADE, null= True, related_name= 'purchases',  blank= True)
    date = models.DateTimeField(auto_now_add=True)
    purchaser = models.ForeignKey('users.CustomUser', on_delete= models.CASCADE, default = '', related_name='purchases', null= True, blank=True)
    project = models.ForeignKey('company.Projects', default='', related_name='purchases', on_delete= models.CASCADE)
    source = models.CharField(max_length=255, default='')
    paid = models.BooleanField(default=False)
    details = models.TextField(max_length=255, default = '')
    tax_percentage = models.IntegerField(default= 0.00)
    

    def __str__(self):
        return self.purchase_id()

    def get_absolute_url(self):
        return reverse_lazy('purchased-items-view', args=[str(self.id)])
    
    def purchase_id(self):
        purchase = self.organisation.name[0] + self.source[0] + f'{self.id:0004d}'
        return purchase
    
    # function
    def taxed_amount(self, amount):
        total = 0.0
        total += amount + (amount * (self.tax_percentage/100))
        return total
    # end of functions
    
    def stock_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase.purchase_id() == self.purchase_id():
                if item.purchase_type == 'Stock':
                    total += item.total_amount()
        return total
    
    def taxed_stock_purchases(self):
        stock = self.stock_purchase()
        return self.taxed_amount(stock)
    
    def fixed_asset_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase.purchase_id() == self.purchase_id():
                if item.purchase_type == 'Fixed Assets':
                    total += item.total_amount()
        return total
    
    def taxed_fixed_asset_purchases(self):
        asset = self.fixed_asset_purchase()
        return self.taxed_amount(asset)
    
    def manufacturing_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase.purchase_id() == self.purchase_id():
                if item.purchase_type == 'Manufacturing':
                    total += item.total_amount()
        return total
    
    def taxed_manufacturing_purchases(self):
        manufacturing_purchases = self.manufacturing_purchase()
        return self.taxed_amount(manufacturing_purchases)
    
    def overheads_purchase(self):
        total = 0.00
        for item in self.item_purchased.all():
            if item.purchase.purchase_id() == self.purchase_id():
                if item.purchase_type == 'Overheads':
                    total += item.total_amount()
        return total
    
    def taxed_overhead_purchase(self):
        overheads = self.overheads_purchase()
        return self.taxed_amount(overheads)
    
    def sub_total(self):
        total = 0.00
        total += self.fixed_asset_purchase() + self.stock_purchase() + self.overheads_purchase() + self.manufacturing_purchase()
        return total
    
    def tax_amount(self):
        tax = 0.00
        tax += (self.sub_total() * (self.tax_percentage/100))
        tax =  round(tax, 2)
        return tax

    
    def grand_total(self):
        total = self.sub_total()
        return self.taxed_amount(total)
    
class PurchasedItem(models.Model):
    purchase_types = (
        ('Stock', 'Stock'),
        ('Overheads', 'Overheads'),
        ('Fixed Assets', 'Fixed Assets'),
        ('Manufacturing', 'Manufacturing'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name = 'item_purchased', on_delete= models.CASCADE, null=True, blank=True, default='')
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
    
    def product_ref(self):
        id = self.organisation.name[0] + self.product_name[0] + f'{self.id:0004d}'
        return id    

class Expense(models.Model):
    type_of_expense = (
        ('Credit Interest', 'Credit Interest'),
        ('Other', 'Other'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name = 'expenses', blank = True, null = True, on_delete=models.CASCADE)
    project = models.ForeignKey('company.Projects', null = True, blank = True, related_name='expenses',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    details = models.TextField(default='')
    expense_type = models.CharField(max_length = 50, choices = type_of_expense, default = 'Credit Interest')
    quantity = models.FloatField(default=0.0)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def expense_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id
    
    def total_expense(self):
        total = 0.0
        total += (self.quantity * self.unit_price)
        return total

class Income(models.Model):
    type_of_expense = (
        ('Debit Interest', 'Debit Interest'),
        ('Other', 'Other'),
    )
    organisation = models.ForeignKey('company.Organisation', related_name = 'incomes', blank = True, null = True, on_delete=models.CASCADE)
    project = models.ForeignKey('company.Projects', null = True, blank = True, related_name='incomes', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    details = models.TextField(default='')
    expense_type = models.CharField(max_length = 50, choices = type_of_expense, default = 'Debit Interest')
    quantity = models.FloatField(default=0.0)
    unit_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def income_id(self):
        id = self.organisation.name[0] + self.name[0] + f'{self.id:0004d}'
        return id
    
    def total_income(self):
        total = 0.0
        total += (self.quantity * self.unit_price)
        return total