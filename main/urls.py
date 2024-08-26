from django.urls import path
from .views import HomePageView, ContactUsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact-us/', ContactUsPageView.as_view(), name='contact-company'),
]