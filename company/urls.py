from django.urls import path
from .views import CompanyDashboardView, ProjectsIndexView, CreateProjectView, ProjectsDetailedView, ProjectsBriefView


urlpatterns = [
    # Dashboard Views
    path('dashboard/', CompanyDashboardView.as_view(), name = 'company-dashboard'),

    # Projects Views
    path('projects/', ProjectsIndexView.as_view(), name = 'project-index'),
    path('projects/create/', CreateProjectView.as_view(), name = 'create-project'),
    path(f'projects/<str:pk>/', ProjectsDetailedView.as_view(), name = 'project-detailed-view'),
    path('projects/<str:pk>/brief/', ProjectsBriefView.as_view(), name = 'project-detailed-brief'),
]