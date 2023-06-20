from django.urls import path
from .views import schedule_app,approve_app
from .views import schedule_app,Appointment_filter
from .views import schedule_app,approve_app,Appointment_filter
urlpatterns = [
     path('',schedule_app.as_view()),
     path('PendingAppintmentList/', Appointment_filter.as_view()),
     path('approve-appointment/<int:pk>',approve_app.as_view(),name='approve-appointment'),
]
