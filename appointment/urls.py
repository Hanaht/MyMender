from django.urls import path
from .views import schedule_app,acceptRejectAppointment,Appointment_filter
urlpatterns = [
     path('',schedule_app.as_view()),
     path("status", acceptRejectAppointment, name="acceptRejectAppointment"),
     path('PendingAppintmentList/', Appointment_filter.as_view())

]
