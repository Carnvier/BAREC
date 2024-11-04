from django.forms import BaseModelForm
from django.db import transaction
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import json
from django.views.generic import TemplateView, DetailView,CreateView, ListView, UpdateView, DeleteView
from .models import OrganisationRegistration, Organisation, Company, Branch, Projects, Asset, Creditor, Debtor, Staff, Salary, Purchases, PurchasedItem, Expense, Income
from users.models import CustomUser
from .forms import OrganisationRegistrationForm
from django.urls import reverse_lazy



# Company registration
class OrganizationRegistrationForm(CreateView):
    template_name = 'organisation/create/register-organisation.html'
    form_class = OrganisationRegistrationForm
    success_url  = reverse_lazy('organisation-creation-success')

class OrganizationRegistrationConfirm(TemplateView):
    template_name = 'company/organisation/confirm.html'
    model = OrganisationRegistration
    context_object_name = 'reg'

class OrganisationRegisterView(ListView):
    template_name = 'organisation/read/organisation-register.html' 
    model = OrganisationRegistration
    context_object_name = 'reg'

class RegisteredOrganisationDetailedView(DetailView):
    template_name = 'organisation/read/registered-organisation-detail.html'
    model = OrganisationRegistration
    context_object_name = 'reg'

class RegisteredOrganisationUpdateStatusView(UpdateView):
    template_name = 'organisation/update/status-registered-organisation.html'
    model = OrganisationRegistration
    fields = ('status',)
    success_url = reverse_lazy('organisation-register')
    context_object_name = 'reg'

    def form_valid(self, form):
        if form.instance.status == 'Approved':
            registration = form.instance
            count = 0
            for i in CustomUser.objects.all():
                if registration.preffered_username == i.username:
                    count += 1
            if count == 0:
                with transaction.atomic():
                    CustomUser.objects.create(first_name=registration.first_name, last_name = registration.last_name, email=registration.founder_email, address=registration.personal_address, username=registration.preffered_username, D_O_B = registration.founder_DOB, phone_number=registration.founder_phone_number, ID_Number = registration.ID_Number)

                    try:
                        founder = CustomUser.objects.get(first_name=registration.first_name)
                    except CustomUser.DoesNotExist:
                        return self.form_invalid(form)
        
                    organisation = Organisation.objects.create(name = registration.organisation_name,
                    est = registration.est,
                    headquarters = registration.headquarters,
                    founder =  founder,
                    organisation_email = registration.organisation_email,
                    organisation_phone_number = registration.organisation_phone_number,
                    organisation_description = registration.organisation_description,
                    motive = registration.motive,)

                    try:
                        founder.organisation = organisation
                        founder.save()
                    except CustomUser.DoesNotExist:
                        return self.form_invalid(form)
            else:
                return HttpResponseBadRequest('Username is taken')
        return super().form_valid(form)

# Organisation Dashboard Views
class OrganisationDashboardView(DetailView):
    template_name = 'organisation/read/dashboard.html'
    model = Organisation
    context_object_name = 'org'

class CreateCompanyView(CreateView):
    template_name = 'organisation/create/create-company.html'
    model = Company
    fields = ('name','CEO_name', 'starting_capital', 'email', 'phone_number', )
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
    fields = ('company', 'name', 'location', 'phone_number', 'branch_supervisor',)

    def form_valid(self, form):
        form.instance.organisation  = self.request.user.organisation
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("company-overview", kwargs={'pk': self.object.company.id})

    


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
    fields = ('branch', 'name', 'supervisor')
    
    def get_success_url(self):
        return reverse_lazy("project-index", kwargs={'pk': self.object.branch.id})
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.organisation = self.request.user.organisation
        return super().form_valid(form)

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

class AssetBriefView(DetailView):
    template_name = 'organisation/read/asset-brief.html'
    model = Projects
    
class CreateAssetView(CreateView):
    template_name = 'organisation/create/create-asset.html'
    model = Asset
    fields = '__all__'

class CreditorBriefView(DetailView):
    template_name = 'organisation/read/Creditor-brief.html'
    model = Projects

class CreateCreditorView(CreateView):
    template_name = 'organisation/create/create-liability.html'
    model = Creditor
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
    fields = ('source', 'branch','project','tax_percentage', 'details',)  

    def form_valid(self, form):
        form.instance.purchaser = self.request.user
        form.instance.organisation = self.request.user.organisation
        return super().form_valid(form)  

class PurchasedItemsDetailView(DetailView):
    template_name = 'organisation/read/purchased-items-detail.html'
    model = Purchases
    context_object_name = 'purchases'

class CreatePurchasedItemsView(CreateView):
    template_name = 'organisation/create/create-purchased-items.html'
    model = PurchasedItem
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

#Stats
class OrganisationStatsView(DetailView):
    template_name = 'organisation/read/organisation-stats.html'
    model = Organisation

class OrganisationIncomeStatement(DetailView):
    template_name = 'organisation/read/organisation-income-statement.html'
    model = Organisation



