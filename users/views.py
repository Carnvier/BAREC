from django.shortcuts import render, redirect 
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView, CreateView
from .models import CustomUser
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed

# Create your views here.
class LoginView(TemplateView):
    template_name = 'registration/login.html'

class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm
    model =  CustomUser
    success_url = reverse_lazy('login')

def custom_logout(request):
    logout(request)  # Log the user out
    request.session.flush()  # Clear the session data
    return redirect(reverse_lazy('login'))  # Redirect to the login page

class ProfileOverviewPageView(TemplateView):
    template_name = 'profile/index.html'
    model = CustomUser
    

