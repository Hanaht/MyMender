from django.urls import path
# from .views import schedule_app,approve_app
# from .views import schedule_app,Appointment_filter
from .views import approve_app,Appointment_filter,schedule_app_serv,decline_app,schedule_app_serv_ID
# from .views import schedule_app,acceptRejectAppointment,Appointment_filter
from .views import approve_app,Appointment_filter
urlpatterns = [
     # path('',schedule_app.as_view()),
     path('PendingAppintmentList/', Appointment_filter.as_view()),
     path('approve-appointment/<int:pk>',approve_app.as_view(),name='approve-appointment'),
     path('decline-appointment/<int:pk>',decline_app.as_view(),name='decline-appointment'),
     # path('schedule_appid/<int:pk>',schedule_app_servid.as_view(),name='schedule_appid'),
     path('schedule_app/<int:pk>',schedule_app_serv.as_view(),name='schedule_app'),
     path('schedule_app_ID/',schedule_app_serv_ID.as_view(),name='schedule_app'),

     ]
