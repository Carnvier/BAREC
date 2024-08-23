from django.urls import path
from .views import CompanyOverviewView, CompanyDashboardView, ProjectsIndexView, CreateProjectView, ProjectsDetailedView, ProjectsBriefView, UpdateProjectView, DeleteProjectView, StaffBriefView, CreateAssetsView, AssetsBriefView, CreateLiabilitiesView, LiabilitiesBriefView, SalesBriefView, AccountsBriefView, StaffOverviewView, CreateStaffView, DeleteStaffView, UpdateStaffView, StaffDetailedBriefView


urlpatterns = [
    # Dashboard Urls
    path('dashboard/<str:pk>/', CompanyDashboardView.as_view(), name = 'company-dashboard'),
    path('dashboard/<str:pk>/overview', CompanyOverviewView.as_view(), name = 'company-overview'),

    # Projects Urls
    path('projects/', ProjectsIndexView.as_view(), name = 'project-index'),
    path('projects/create/', CreateProjectView.as_view(), name = 'create-project'),
    path(f'projects/<str:pk>/', ProjectsDetailedView.as_view(), name = 'project-detailed-view'),
    path('projects/<str:pk>/brief/', ProjectsBriefView.as_view(), name = 'project-detailed-brief'),
    path('projects/<str:pk>/update/', UpdateProjectView.as_view(), name = 'update-project'),
    path('projects/<int:pk>/delete/', DeleteProjectView.as_view(), name = 'delete-project'),
    path('projects/<int:pk>/staff-overview/', StaffBriefView.as_view (), name = 'project-staff-overview' ),
    path('projects/<int:pk>/assets-overview/', AssetsBriefView.as_view(), name = 'project-assets-overview' ),
    path('projects/<str:pk>/assets-overview/create/', CreateAssetsView.as_view(), name = 'create-asset'), 
    path('projects/<int:pk>/liabilities-overview/', LiabilitiesBriefView.as_view(), name = 'project-liabilities-overview' ),
    path('projects/<str:pk>/liabilities-overview/create/', CreateLiabilitiesView.as_view(), name = 'create-liability'), 
    path('projects/<int:pk>/sales-overview/', SalesBriefView.as_view(), name = 'project-sales-overview' ),

# Accounts Urls
    path('accounts/', AccountsBriefView.as_view(), name = 'accounts-index'),
# Staff Urls
    path('staff/', StaffOverviewView.as_view(), name = 'staff-index'),
    path('staff/detailedview/<int:pk>', StaffDetailedBriefView.as_view(), name = 'staff-detail'),
    path('staff/create', CreateStaffView.as_view(), name = 'create-staff'),
    path('staff/detailedview/<int:pk>/update', UpdateStaffView.as_view(), name = 'update-staff'),
    path('staff/detailedview/<int:pk>/delete', DeleteStaffView.as_view(), name = 'delete-staff'),
]