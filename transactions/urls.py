from django.urls import path
from .views import SalesOverviewView, SalesFormView, StockOverviewView, SalesHistoryView, SalesInvoiceView,SalesItemsDetailView, CreateSalesItemView, UpdateSalesForm, StockOverviewView, StockDetailedView, CreateStockView, UpdateStockView, CustomerOverviewView, CreateCustomerView, CustomerDetailedView, UpdateCustomerView, DeleteCustomerView

urlpatterns  =[
    # Sales
    path('sales/', SalesOverviewView.as_view(), name='sales-overview'),
    path('history/', SalesHistoryView.as_view(), name='sales-history'),
    path('form/', SalesFormView.as_view(), name='sales-form'),
    path('sales/<int:pk>/detail-view/', SalesInvoiceView.as_view(), name='sales-invoice'),
    path('history/detail-view/<int:pk>/update', UpdateSalesForm.as_view(), name='update-sales-form'),
    path('sales/<int:pk>/create-sales/view-items', SalesItemsDetailView.as_view(), name = 'sales-items-detail'),
    path('sales/<int:pk>/create-sales/view-items/create-item/', CreateSalesItemView.as_view(), name = 'create-sales-item'),

 
  
    

    # Stock
    path('stock/', StockOverviewView.as_view(), name='stock-overview'),
    path('stock/detailed-view/<int:pk>/', StockDetailedView.as_view(), name='stock-detailed-view'),
    path('stock/detail-view/create/', CreateStockView.as_view(), name='create-stock'),
    path('stock/detail-view/<int:pk>/update/', UpdateStockView.as_view(), name='update-stock'),

    # Customer
    path('customer/', CustomerOverviewView.as_view(), name='customer-overview'),
    path('customer/create/<int:pk>/', CreateCustomerView.as_view(), name='create-customer'),
    path('customer/detail-view/<int:pk>/', CustomerDetailedView.as_view(), name='customer-detail-view'),
    path('customer/detail-view/<int:pk>/update/', UpdateCustomerView.as_view(), name='update-customer'),
    path('customer/detail-view/<int:pk>/delete/', DeleteCustomerView.as_view(), name='delete-customer'),

    # #Expenses
    # path('expenses/', ExpensesOverviewView.as_view(), name='expenses-overview'),
    # path('expenses/create/', CreateExpensesView.as_view(), name = 'create-expenses'),
    # path('expenses/detail-view/<int:pk>', ExpensesDetailedView.as_view(), name = 'expenses-detail'),

]