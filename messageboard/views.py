from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Messagesboard
from django.core.exceptions import PermissionDenied 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.
class MessageboardOverviewView(LoginRequiredMixin, ListView):
    template_name = 'messageboard/index.html'
    model = Messagesboard
    context_object_name = 'messages'

class MessageboardDetailedView(LoginRequiredMixin, DetailView):
    template_name = 'messageboard/detail.html'
    model = Messagesboard
    context_object_name = 'messages'

class CreateMessageView(LoginRequiredMixin, CreateView):
    template_name = 'messageboard/create.html'
    model = Messagesboard
    fields = ('ref', 'receipient', 'text', 'urgency', )
    success_url = reverse_lazy('messages-overview')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateMessageView(LoginRequiredMixin, UpdateView):
    template_name = 'messageboard/update.html'
    model = Messagesboard
    fields = ('ref', 'receipient', 'text', 'urgency', )
    success_url = reverse_lazy('messages-overview')
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    

class DeleteMessageView(LoginRequiredMixin, DeleteView):
    template_name = 'messageboard/delete.html'
    model = Messagesboard
    fields = '__all__'
    success_url = reverse_lazy('messages-overview')