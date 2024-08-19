from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# from .models import Main

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    # model = Main
    # context_object_name = 'main'   