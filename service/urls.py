from django.urls import path
from .views import AddService

urlpatterns = [
    path('', AddService.as_view()),
]