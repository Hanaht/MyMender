from django.urls import path
from .views import AddService

urlpatterns = [
    path('AddNotification', AddService.as_view()),
]