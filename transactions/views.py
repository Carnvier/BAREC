from django.forms import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, ListView, DeleteView
from .models import Sales, Stock, Customer, Expenses
from django.urls import reverse_lazy

# Sales View
class SalesOverviewView(TemplateView):
    template_name = 'transactions/read/sales-index.html'

class SalesFormView(CreateView):
    template_name = 'transactions/create/create-sale.html'
    model = Sales
    fields = ("product", "sale_details", "quantity", "discount", "branch", "project", )

    def form_valid(self, form, *args, **kwarg ):
        if form.instance.quantity > 5:
            form.add_error('quantity', 'stock is lacking')
            return self.form_invalid(form)
        return super().form_valid(form, *args, **kwarg)        
class SalesHistoryView(ListView):
    template_name = 'transactions/read/sale-history.html'
    model = Sales
    context_object_name = 'sales'

class SalesDetailedView(DetailView):
    template_name = 'transactions/sales/sales-invoice.html'
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
    template_name = 'transactions/read/search-stock.html'
    model = Stock
    context_object_name = 'stock'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        if query:
            context['results'] = Stock.objects.filter(product_name__icontains=query)
            context['query'] = query

        else:
            context['results'] = []
            context['query'] = ''
        return context
    
    def is_ajax(self, request):
        return request.headers.get('x-requested-with') == 'XMLHttpRequest'
    
    def get(self, request, *args, **kwargs):
        if self.is_ajax(request):
            query = request.GET.get('q')
            results = Stock.objects.filter(product_id__icontains=query)
            results_list = list(results.values('product_id'))
            return JsonResponse({'results': results_list})
        return super().get(request, *args, **kwargs)

class CreateStockView(CreateView):
    template_name = 'transactions/create/create-stock.html'
    model = Stock
    fields = ('company','branch','branch', 'project', 'product_name', 'product_description', 'quantity', 'product_price', )
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
    template_name = 'transactions/read/customer-index.html'
    model = Customer
    context_object_name = 'customer'

class CreateCustomerView(CreateView):
    template_name = 'transactions/create/create-customer.html'
    model = Customer
    fields = ('name', 'type_of_customer', 'address', 'phone_number', 'email',)
    success_url = reverse_lazy('customer-overview')

    def form_valid(self, form):
        form.instance.organisation = self.request.user.organisation
        return super().form_valid(form)

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
