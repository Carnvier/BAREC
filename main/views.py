from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# from .models import Main

# Create your views here.
class HomePageView( TemplateView):
    template_name = 'main/read/home.html'  

class ContactUsPageView(TemplateView):
    template_name = 'main/read/contact-us.html'
