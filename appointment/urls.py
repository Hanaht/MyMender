from django.urls import path
<<<<<<< HEAD
from .views import schedule_app,approve_app
from .views import schedule_app,Appointment_filter
=======
from .views import schedule_app,approve_app,Appointment_filter
# from .views import schedule_app,acceptRejectAppointment,Appointment_filter
>>>>>>> 4df90241102e9c6cb9bc6d71c8111fcde98433bf
urlpatterns = [
     path('',schedule_app.as_view()),
     # path("status", acceptRejectAppointment, name="acceptRejectAppointment"),
     path('PendingAppintmentList/', Appointment_filter.as_view()),
     path('approve-appointment/<int:pk>',approve_app.as_view(),name='approve-appointment'),
]
