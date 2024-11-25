from django.shortcuts import render, get_object_or_404, redirect
from .forms import SaleItemForm
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView, ListView, DeleteView
from .models import Sales, Stock, Customer, SaleItem
from django.urls import reverse_lazy

# Sales View
class SalesOverviewView(TemplateView):
    template_name = 'transactions/read/sales-index.html'

class SalesFormView(CreateView):
    template_name = 'transactions/create/create-sale.html'
    model = Sales
    fields = ( "customer", "sale_details", "project", )

    def get_success_url(self):
        return reverse_lazy("sales-items-detail", kwargs={'pk': self.object.id})


class SalesItemsDetailView(DetailView):
    template_name = 'transactions/read/sales-items-detail.html'
    model = Sales
    context_object_name = 'sales'

    def get(self, request, *args, **kwargs):
        # Call the parent class's get method to retrieve the object
        self.object = self.get_object()
        
        # Store the sales id in the session
        request.session['id'] = self.object.id# Assuming 'id' is the primary key
        
        # Prepare context data
        context = self.get_context_data(object=self.object)
        
        # Render the template with the context
        return self.render_to_response(context)

class CreateSalesItemView(View):
    template_name = 'transactions/create/create-sale-item.html'
    form_class = SaleItemForm

    def get(self, request, pk):
        product = get_object_or_404(Stock, pk=pk)
        form = self.form_class(initial={'product_id': product.id})
        return render(request, self.template_name, {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Stock, pk=pk)
        form = self.form_class(request.POST)
        
        if form.is_valid():
            sale = form.save(commit=False)  # Create SaleItem instance but don't save to DB yet
            
            # Get the sale_id from the session
            sale_id = request.session.get('id')  # Ensure this is the correct key
            
            # Retrieve the Sales instance
            sales_instance = get_object_or_404(Sales, id=sale_id)
            
            # Assign the Sales instance to the SaleItem
            sale.sale = sales_instance
            
            # Update product quantity
            product.quantity -= sale.quantity
            product.save()
            
            # Save the SaleItem
            sale.save()
            
            # Redirect to the sales items detail view
            return redirect('sales-items-detail', pk=sales_instance.id)  # Redirect using the sales instance id
            
        # If the form is not valid, re-render the form with errors
        return render(request, self.template_name, {'form': form, 'product': product})
    
class SalesInvoiceView(DetailView):
    template_name = 'transactions/read/sales-invoice.html'
    model = Sales    
class SalesHistoryView(ListView):
    template_name = 'transactions/read/sale-history.html'
    model = Sales
    context_object_name = 'sales'

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
    
    # def get(self, request, *args, **kwargs):
    #     if self.is_ajax(request):
    #         query = request.GET.get('q')
    #         results = Stock.objects.filter(product_name__icontains=query)
    #         results_list = list(results.values('product_name'))
    #         return JsonResponse({'results': results_list})
    #     return super().get(request, *args, **kwargs)

class CreateStockView(CreateView):
    template_name = 'transactions/create/create-stock.html'
    model = Stock
    fields = ('asset', 'project', 'product_name',  'quantity', 'product_price', 'product_description',)
    success_url = reverse_lazy('stock-overview')

    def form_valid(self, form):
        form.instance.organisation = self.request.user.organisation
        return super().form_valid(form)

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
        form.instance.organisation = self.request.user.organisation.name
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
# class ExpensesOverviewView(ListView):
#     template_name = 'transactions/expenses/index.html'
#     model = Expenses
#     context_object_name = 'expenses'

# class CreateExpensesView(CreateView):
#     template_name = 'transactions/expenses/create.html'
#     model = Expenses
#     fields = '__all__'
#     success_url = reverse_lazy('expenses-overview')

# class ExpensesDetailedView(DetailView):
#     template_name = 'transactions/expenses/detail.html'
#     model = Expenses
