from django.urls import path
from .views import schedule_app
urlpatterns = [
     path('',schedule_app.as_view()),
]
