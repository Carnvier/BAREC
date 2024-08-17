from django.shortcuts import render
from .models import Messagesboard
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy

# Create your views here.
class MessageboardOverviewView(ListView):
    template_name = 'messageboard/index.html'
    model = Messagesboard
    context_object_name = 'messages'

class MessageboardDetailedView(DetailView):
    template_name = 'messageboard/detail.html'
    model = Messagesboard
    context_object_name = 'messages'

class CreateMessageView(CreateView):
    template_name = 'messageboard/create.html'
    model = Messagesboard
    fields = '__all__'
    success_url = reverse_lazy('messages-overview')

class UpdateMessageView(UpdateView):
    template_name = 'messageboard/update.html'
    model = Messagesboard
    fields = '__all__'
    success_url = reverse_lazy('messages-overview')

class DeleteMessageView(DeleteView):
    template_name = 'messageboard/delete.html'
    model = Messagesboard
    fields = '__all__'
    success_url = reverse_lazy('messages-overview')