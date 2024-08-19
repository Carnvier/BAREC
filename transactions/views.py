from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, ListView, DeleteView
from .models import Sales, Stock, Customer, Expenses
from django.urls import reverse_lazy

# Sales View
class SalesOverviewView(TemplateView):
    template_name = 'transactions/sales/index.html'

class SalesFormView(CreateView):
    template_name = 'transactions/sales/create.html'
    model = Sales
    fields = ("sale_id", "product", "sale_details", "quantity", "discount", "branch",)

    def form_valid(self, form):
        form.instance.sales_rep = self.request.user
        return super().form_valid(form)
    def form_valid(self, form):
        form.instance.sales_rep = self.request.user
        return super().form_valid(form)

class SalesHistoryView(ListView):
    template_name = 'transactions/sales/history.html'
    model = Sales
    context_object_name = 'sales'

class SalesDetailedView(DetailView):
    template_name = 'transactions/sales/detail.html'
    model = Sales

class UpdateSalesForm(UpdateView):
    template_name = 'transactions/sales/update.html'
    model = Sales
    fields = '__all__'
    success_url = reverse_lazy('sales-history')

    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)


# Stock Views
class StockOverviewView(ListView):
    template_name = 'transactions/stock/index.html'
    model = Stock
    context_object_name = 'stock'

class CreateStockView(CreateView):
    template_name = 'transactions/stock/create.html'
    model = Stock
    fields = "__all__"
    success_url = reverse_lazy('stock-overview')

class StockDetailedView(DetailView):
    template_name = 'transactions/stock/detail.html'
    model = Stock

class UpdateStockView(UpdateView):
    template_name = 'transactions/stock/update.html'
    model = Stock
    success_url = reverse_lazy('stock-overview')
    fields = '__all__'

# Customer View
class CustomerOverviewView(ListView):
    template_name = 'transactions/customer/index.html'
    model = Customer
    context_object_name = 'customer'

class CreateCustomerView(CreateView):
    template_name = 'transactions/customer/create.html'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customer-overview')


class CustomerDetailedView(DetailView):
    template_name = 'transactions/customer/detail.html'
    model = Customer

class UpdateCustomerView(UpdateView):
    template_name = 'transactions/customer/update.html'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customer-overview')

class DeleteCustomerView(DeleteView):
    template_name = 'transactions/customer/delete.html'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customer-overview')

# Expenses view
class ExpensesOverviewView(ListView):
    template_name = 'transactions/expenses/index.html'
    model = Expenses
    context_object_name = 'expenses'

class CreateExpensesView(CreateView):
    template_name = 'transactions/expenses/create.html'
    model = Expenses
    fields = '__all__'
    success_url = reverse_lazy('expenses-overview')

class ExpensesDetailedView(DetailView):
    template_name = 'transactions/expenses/detail.html'
    model = Expenses
