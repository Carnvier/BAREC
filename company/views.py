from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import json
from django.views.generic import TemplateView, DetailView,CreateView, ListView, UpdateView, DeleteView
from .models import Company, Projects, Assets, Liabilities,Staff, Organisation, CompanyRegistration, Branch, Purchases, Purchased_Item
from django.urls import reverse_lazy


# Company registration
class OrganizationRegistrationForm(CreateView):
    template_name = 'company/organisation/create.html'
    model = CompanyRegistration
    fields = '__all__'
    success_url  = reverse_lazy('organisation-creation-success')

class OrganizationRegistrationConfirm(TemplateView):
    template_name = 'company/organisation/confirm.html'
    model = CompanyRegistration
    context_object_name = 'reg'


# Dashboard Views
class CompanyDashboardView(DetailView):
    template_name = 'organisation/read/dashboard.html'
    model = Organisation
    context_object_name = 'org'

class CreateCompanyView(CreateView):
    template_name = 'organisation/create/create-company.html'
    model = Company
    fields = ('company_name','CEO_name', 'starting_capital', 'email', 'phone_number', )
    context_object_name = 'company'
    
    def form_valid(self, form):
        form.instance.organisation  = self.request.user.organisation
        return super().form_valid(form)

class CompanyOverviewView(DetailView):
    template_name = 'organisation/read/company-view.html'
    model = Company
    context_object_name = 'company'

# Branch view
class BranchOverviewView(DetailView):
    template_name = 'organisation/read/branch-view.html'
    model = Branch
    context_object_name = 'branch'

class CreateBranchView(CreateView):
    template_name = 'organisation/create/create-branch.html'
    model = Branch
    fields = ('company', 'branch_name', 'location', 'branch_phone_number', 'branch_supervisor',)

class UpdateBranchView(UpdateView):
    template_name = 'organisation/branch/update/update.html'
    model = Branch
    context_object_name = 'branch'
    fields = ('branch_name', 'location', 'branch_phone_number', 'branch_supervisor',)

# Projects Views 
class ProjectsIndexView(ListView):
    template_name = 'organisation/read/project-index.html'
    model =  Projects
    context_object_name = 'projects'

class CreateProjectView(CreateView):
    template_name = 'organisation/create/create-project.html'
    model = Projects
    fields = ('branch', 'project_name', 'project_supervisor', 'cash_in_hand',)
    success_url = reverse_lazy('project-index')

class ProjectsDetailedView(DetailView):
    template_name = 'organisation/read/project-detail-view.html'
    model = Projects

class ProjectsBriefView(DetailView):
    template_name = 'organisation/read/project-detailed-brief.html'
    model = Projects
    context_object_name = 'projects'

class UpdateProjectView(UpdateView):
    template_name = 'organisation/update/update-project.html'
    model = Projects
    fields = ('branch', 'project_name', 'project_supervisor', 'cash_in_hand',)
    success_url = reverse_lazy('project-index')

class DeleteProjectView(DeleteView):
    model = Projects
    template_name = 'company/projects/delete/delete-project.html'
    success_url = reverse_lazy('project-index')

class StaffBriefView(DetailView):
    template_name = 'company/projects/read/staff-brief.html'
    model = Projects

class AssetsBriefView(DetailView):
    template_name = 'organisation/read/assets-brief.html'
    model = Projects
    
class CreateAssetsView(CreateView):
    template_name = 'organisation/create/create-asset.html'
    model = Assets
    fields = '__all__'

class LiabilitiesBriefView(DetailView):
    template_name = 'organisation/read/liabilities-brief.html'
    model = Projects

class CreateLiabilitiesView(CreateView):
    template_name = 'organisation/create/create-liability.html'
    model = Liabilities
    fields = '__all__'

class SalesBriefView(DetailView):
    template_name = 'organisation/read/sales-brief.html'
    model = Projects

# Accounts Views
class PurchasesBriefView(ListView):
    template_name = 'organisation/read/purchases-index.html'
    model = Purchases
    context_object_name = 'purchases'

def chart_view(request):
    data = Purchases.objects.all()
    labels = json.dumps([point.purchase_id for point in data])
    values = json.dumps([point.grand_total for point in data])
    print(labels)
    print(values)
    return render(request, 'organisation/read/purchases-index.html', {'labels': labels, 'values': values})

class CreatePurchasesView(CreateView):
    template_name = 'organisation/create/create-purchase.html'
    model = Purchases
    fields = ('purchaser', 'source', 'branch', 'project', 'details',)    

class PurchasedItemsDetailView(DetailView):
    template_name = 'organisation/read/purchased-items-detail.html'
    model = Purchases
    context_object_name = 'purchases'

class CreatePurchasedItemsView(CreateView):
    template_name = 'organisation/create/create-purchased-items.html'
    model = Purchased_Item
    fields = ('purchase','product_name', 'quantity', 'unit_price', )
    context_object_name = 'item'

class PurchasesQuoteView(DetailView):
    template_name = 'organisation/read/purchases-quote.html'
    model = Purchases
# Staff Views
class StaffOverviewView(ListView):
    template_name = 'organisation/read/staff-index.html'
    model = Staff
    context_object_name = 'staff'

class StaffDetailedBriefView(DetailView):
    template_name = 'organisation/read/staff-detailed-brief.html'
    model = Staff

class CreateStaffView(CreateView):
    template_name = 'organisation/create/create-staff.html'
    model = Staff
    fields = ('staff_name', 'company', 'monthly_salary', 'staff_branch', 'staff_project', 'department', 'occupation',)

class UpdateStaffView(UpdateView):
    template_name = 'organisation/update/update-staff.html'
    model = Staff
    fields = ('company', 'monthly_salary', 'staff_branch', 'staff_project', 'department', 'occupation',)

class DeleteStaffView(DeleteView):
    template_name = 'organisation/delete/delete-staff.html'
    model = Staff
    success_url  =reverse_lazy('create-staff')
