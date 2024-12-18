from django.urls import path
from .views import OrganisationRegisterView, RegisteredOrganisationDetailedView, RegisteredOrganisationUpdateStatusView, CompanyOverviewView, OrganisationDashboardView, ProjectsIndexView, CreateProjectView, ProjectsDetailedView, ProjectsBriefView, UpdateProjectView, DeleteProjectView, StaffBriefView, CreateAssetView, AssetBriefView, CreateCreditorView, CreditorBriefView, SalesBriefView, StaffOverviewView, CreateStaffView, DeleteStaffView, UpdateStaffView, StaffDetailedBriefView, OrganizationRegistrationForm, OrganizationRegistrationConfirm, CreateCompanyView, BranchOverviewView, UpdateBranchView, CreateBranchView, PurchasesBriefView, PurchasedItemsDetailView, PurchasesQuoteView, CreatePurchasesView, CreatePurchasedItemsView, OrganisationIncomeStatement, OrganisationStatsView


urlpatterns = [
    #Organization Registration
    path('organization/registration/create/', OrganizationRegistrationForm.as_view(), name = 'register-organisation'),
    path('organization/registration/success/', OrganizationRegistrationConfirm.as_view(), name = 'organisation-creation-success'), 
    path('organisation/register/', OrganisationRegisterView.as_view(), name = 'organisation-register'),
    path('organisation/register/detail/<str:pk>/', RegisteredOrganisationDetailedView.as_view(), name = 'registered-organisation-detail-view'),
    path('organisation/register/detail/<str:pk>/update', RegisteredOrganisationUpdateStatusView.as_view(), name = 'registered-organisation-update-status'),

    # Orgnisation Dashboard Urls
    path('dashboard/<str:pk>/', OrganisationDashboardView.as_view(), name = 'organisation-dashboard'),
    path('dashboard/<str:pk>/overview/', CompanyOverviewView.as_view(), name = 'company-overview'),
    path('dashboard/<str:pk>/create/', CreateCompanyView.as_view(), name = 'create-company'),
    # Branch Urls
    path('dashboard/<int:pk>/overview/branch/', BranchOverviewView.as_view(), name = 'branch-overview'),
    path('dashboard/<int:pk>/create-branch/', CreateBranchView.as_view(), name = 'create-branch'),
    path('dashboard/<str:pk>/branch/<str:branch>/update', UpdateBranchView.as_view(), name = 'update-branch'),

    # Projects Urls
    path('projects/<str:pk>/', ProjectsIndexView.as_view(), name = 'project-index'),
    path('projects/<str:pk>/create/', CreateProjectView.as_view(), name = 'create-project'),
    path('dashboard/overview/branch/projects/<int:pk>/', ProjectsDetailedView.as_view(), name = 'project-detailed-view'),
    path('dashboard/overview/branch/projects/<int:pk>/brief/', ProjectsBriefView.as_view(), name = 'project-detailed-brief'),
    path('dashboard/overview/branch/projects/<int:pk>/update/', UpdateProjectView.as_view(), name = 'update-project'),
    path('projects/<int:pk>/delete/', DeleteProjectView.as_view(), name = 'delete-project'),
    path('projects/<int:pk>/staff-overview/', StaffBriefView.as_view (), name = 'project-staff-overview' ),
    path('dashboard/overview/branch/projects/<int:pk>/asset-overview/', AssetBriefView.as_view(), name = 'project-asset-overview' ),
    path('dashboard/overview/branch/projects/<int:pk>/asset-overview/create/', CreateAssetView.as_view(), name = 'create-asset'), 
    path('dashboard/overview/branch/projects/<int:pk>/Creditor-overview/', CreditorBriefView.as_view(), name = 'project-liability-overview' ),
    path('dashboard/overview/branch/projects/<int:pk>/Creditor-overview/create/', CreateCreditorView.as_view(), name = 'create-liability'), 
    path('dashboard/overview/branch/projects/<int:pk>/sales-overview/', SalesBriefView.as_view(), name = 'project-sales-overview' ),

# Accounts Urls
    path('purchases/<int:pk>/', PurchasesBriefView.as_view(), name = 'purchases-index'),
    path('purchases/<int:pk>/create-purchase', CreatePurchasesView.as_view(), name = 'create-purchase'),
    path('purchases/<int:pk>/detail-view', PurchasesQuoteView.as_view(), name = 'purchases-quote'),
    path('purchases/<int:pk>/create-purchases/view-items', PurchasedItemsDetailView.as_view(), name = 'purchased-items-view'),
    path('purchases/<int:pk>/create-purchases/view-items/create-item/', CreatePurchasedItemsView.as_view(), name = 'create-purchased-item'),
# Staff Urls
    path('staff/<int:pk>/', StaffOverviewView.as_view(), name = 'staff-index'),
    path('staff/detailedview/<int:pk>', StaffDetailedBriefView.as_view(), name = 'staff-detail'),
    path('staff/create', CreateStaffView.as_view(), name = 'create-staff'),
    path('staff/detailedview/<int:pk>/update', UpdateStaffView.as_view(), name = 'update-staff'),
    path('staff/detailedview/<int:pk>/delete', DeleteStaffView.as_view(), name = 'delete-staff'),

# Statistics Urls
    path('stats/<int:pk>/', OrganisationStatsView.as_view(), name = 'organisation-stats'),
    path('stats/<int:pk>/income-statement', OrganisationIncomeStatement.as_view(), name = 'organisation-income-statement'),
]