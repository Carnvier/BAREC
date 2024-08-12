from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from django.contrib.auth import logout
from django.urls import reverse_lazy


# Create your views here.
class LoginView(TemplateView):
    template_name = 'registration/login.html'

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    model =  CustomUser
    success_url = reverse_lazy('login')

def custom_logout(request):
    logout.session.flush()
    logout(request)
    success_url = reverse_lazy('login')
    

