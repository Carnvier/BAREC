from django.shortcuts import render
from django.views.generic import TemplateView, DetailView,CreateView, ListView
from .models import Company, Projects
from django.urls import reverse_lazy
# Create your views here.
class CompanyDashboardView(ListView):
    template_name = 'company/dashboard/dashboard.html'
    model = Company
    context_object_name = 'company'

# Projects Views 
class ProjectsIndexView(ListView):
    template_name = 'company/projects/index.html'
    model =  Projects
    context_object_name = 'projects'

class CreateProjectView(CreateView):
    template_name = 'company/projects/create.html'
    model = Projects
    fields = '__all__'
    success_url = reverse_lazy('project-index')

class ProjectsDetailedView(DetailView):
    template_name = 'company/projects/detailed-view.html'
    model = Projects

class ProjectsBriefView(ListView):
    template_name = 'company/projects/detailed-brief.html'
    model = Projects
    context_object_name = 'projects'