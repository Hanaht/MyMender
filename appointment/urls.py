from django.urls import path
from .views import schedule_app,approve_app
urlpatterns = [
     path('',schedule_app.as_view()),
      path('approve-appointment/<int:pk>',approve_app.as_view(),name='approve-appointment'),
]
