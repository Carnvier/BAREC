from django.shortcuts import render
from django.views.generic import TemplateView, DetailView,CreateView, ListView, UpdateView, DeleteView
from .models import Company, Projects, Assets, Liabilities,Staff, Organisation, CompanyRegistration
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
    template_name = 'company/dashboard/dashboard.html'
    model = Organisation
    context_object_name = 'org'

class CompanyOverviewView(DetailView):
    template_name = 'company/dashboard/company-view.html'
    model = Company
    context_object_name = 'company'

# Projects Views 
class ProjectsIndexView(ListView):
    template_name = 'company/projects/read/index.html'
    model =  Projects
    context_object_name = 'projects'

class CreateProjectView(CreateView):
    template_name = 'company/projects/create/create-project.html'
    model = Projects
    fields = '__all__'
    success_url = reverse_lazy('project-index')

class ProjectsDetailedView(DetailView):
    template_name = 'company/projects/read/detailed-view.html'
    model = Projects

class ProjectsBriefView(DetailView):
    template_name = 'company/projects/read/detailed-brief.html'
    model = Projects
    context_object_name = 'projects'

class UpdateProjectView(UpdateView):
    template_name = 'company/projects/update/update-project.html'
    model = Projects
    fields = '__all__'
    success_url = reverse_lazy('project-index')

class DeleteProjectView(DeleteView):
    model = Projects
    template_name = 'company/projects/delete/delete-project.html'
    success_url = reverse_lazy('project-index')

class StaffBriefView(DetailView):
    template_name = 'company/projects/read/staff-brief.html'
    model = Projects

class AssetsBriefView(DetailView):
    template_name = 'company/projects/read/assets-brief.html'
    model = Projects

class CreateAssetsView(CreateView):
    template_name = 'company/projects/create/create-asset.html'
    model = Assets
    fields = '__all__'
    success_url = reverse_lazy('project-index')

class LiabilitiesBriefView(DetailView):
    template_name = 'company/projects/read/liabilities-brief.html'
    model = Projects

class CreateLiabilitiesView(CreateView):
    template_name = 'company/projects/create/create-liability.html'
    model = Liabilities
    fields = '__all__'
    success_url = reverse_lazy('project-index')

class SalesBriefView(DetailView):
    template_name = 'company/projects/read/sales-brief.html'
    model = Projects

# Accounts Views
class AccountsBriefView(ListView):
    template_name = 'company/accounts/index.html'
    model = Projects
    context_object_name = 'projects'

# Staff Views
class StaffOverviewView(ListView):
    template_name = 'company/staff/read/index.html'
    model = Staff
    context_object_name = 'staff'

class StaffDetailedBriefView(DetailView):
    template_name = 'company/staff/read/detailed-brief.html'
    model = Staff

class CreateStaffView(CreateView):
    template_name = 'company/staff/create/create-staff.html'
    model = Staff
    fields = '__all__'
    success_url = reverse_lazy('staff-index')

class UpdateStaffView(UpdateView):
    template_name = 'company/staff/update/update-staff.html'
    model = Staff
    fields = '__all__'
    success_url = reverse_lazy('staff-index')


class DeleteStaffView(DeleteView):
    template_name = 'company/staff/delete/delete-staff.html'
    model = Staff
    success_url = reverse_lazy('staff-index')