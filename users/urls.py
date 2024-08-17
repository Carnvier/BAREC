from django.urls import path
from .views import SignUpView, LoginView, ProfileOverviewPageView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(), name = 'login' ),
    path('logout/', views.custom_logout, name = 'logout' ),
    path('signup/', SignUpView.as_view(), name = 'signup' ),

    # profile url
    path('profile-overview/', ProfileOverviewPageView.as_view(), name='profile-overview'),
]