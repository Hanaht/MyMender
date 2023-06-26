# from datetime import timezone
from django.utils import timezone
from datetime import *
from pyexpat.errors import messages
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from Auth import models as auth_model
from .models import appointment,appointmentID
from .serializers import appSerializer,appointmentStatus,appIDSerializer
from rest_framework import filters
# from Auth.views import UserLoginView
from django.contrib.auth.decorators import login_required
from services import models as serv_model


class schedule_app_serv(APIView):
    serializer_class=appSerializer
    def post(self, request,pk, format=None):
        serv=serv_model.services.objects.get(ID=pk) 
        app_form = appSerializer(data=request.data)
        if app_form.is_valid():  
            data = app_form.validated_data
            app_date=data['app_date']
            service_=serv.ID
            if datetime.now().date() < app_date: 
                count_app=appointment.objects.filter(app_date=data['app_date'], service_ID=service_).count()
                if count_app<=5:            
                    appointment.service_ID=serv.ID     
                    app_form.save(request,appointment.service_ID)
                    return Response({'Your appointment is received and pending.'})               
                else:
                    return Response({'appointment date is full!!!'})
            else:
                return Response({'Invalid date.'})            
        return Response(app_form.errors, status=status.HTTP_400_BAD_REQUEST)

class schedule_app_serv_ID(APIView):
    serializer_class=appIDSerializer
    def post(self, request, format=None):
        app_form = appIDSerializer(data=request.data)
      
        if app_form.is_valid():  
            data = app_form.validated_data
            # Full_name=data['Full_name']
            app_date=data['app_date']

            # phone_number=data['phone_number']

            service_="Identfication_number"
            if datetime.now().date() < app_date: 
                count_app=appointmentID.objects.filter(app_date=data['app_date'], service_name=service_).count()
                if count_app<=5:            
                    appointmentID.service_name="Identfication_number"     
                    app_form.save(request,appointmentID.service_name)
                    # appointment.save() 
                    # messages.add_message(request, messages.INFO, 'Your appointment is received and pending.')
                    return Response({'Your appointment is received and pending.'})
                
                else:
                    return Response({'appointment date is full!!!'})
            else:
                return Response({'Invalid date.'})
            
        return Response(app_form.errors, status=status.HTTP_400_BAD_REQUEST)





class approve_app(APIView):
    def post(self,request, pk,format=None):
            appoint = appointment.objects.get(ID=pk)
            appoint.ApprovalStatus = "approved"  
            appoint.save()
            return Response({'Appointment approved successfully.'})

class decline_app(APIView):
   def post(self,request, pk,format=None):
            appoint = appointment.objects.get(ID=pk)
            appoint.ApprovalStatus = "declined"  
            appoint.save()
            return Response({'Appointment declined successfully.'})
 
class all_app(APIView):
    def  all_app(request):         
        app=appointment.objects.all()
        return render(request,{'appointments':app})

class Appointment_filter(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointment.objects.all().filter(ApprovalStatus="pending")
    serializer_class = appointmentStatus

class Appointment_filter_approved(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointment.objects.all().filter(ApprovalStatus="approved")
    serializer_class = appointmentStatus
    
    
class AppointmentID_filter_approved(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointmentID.objects.all().filter(ApprovalStatus="pending")
    serializer_class = appIDSerializer
    
    