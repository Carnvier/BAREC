from django.urls import path
from .views import MessageboardOverviewView, MessageboardDetailedView, CreateMessageView, DeleteMessageView, UpdateMessageView

urlpatterns = [
    path('', MessageboardOverviewView.as_view(), name = 'messages-overview'),
    path('detailed-view/<int:pk>/', MessageboardDetailedView.as_view(), name = 'messages-detail'),
    path('create', CreateMessageView.as_view(), name =  'create-message'),
    path('detailed-view/<int:pk>/delete/', DeleteMessageView.as_view(), name ='delete-message'),
    path('detailed-view/<int:pk>/update/', UpdateMessageView.as_view(), name = 'update-message')
]