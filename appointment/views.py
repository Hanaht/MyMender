from datetime import timezone
from pyexpat.errors import messages
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect, render
from django.http import Http404
from rest_framework.views import APIView
from .models import appointment
from .serializers import appSerializer,appointmentStatus
from rest_framework import filters


class schedule_app(APIView):
    serializer_class=appSerializer

    def post(self, request, format=None): 
        app_form = appSerializer(data=request.data)

        if app_form.is_valid():  
            app_date = app_form.cleaned_data.get('app_date')  
            dep_id=app_form.cleaned_data.get('dep_ID')  
            if timezone.now().date() < app_date:  
                if appointment.objects.filter(app_date=app_date, dep_ID=dep_id).count()<=50:
                    app_form.save()
                    # app.save()
                    messages.add_message(request, messages.INFO, 'Your appointment is received and pending.')
                    return Response(app_form.data,
                             status=status.HTTP_201_CREATED)
                else:
                    app_form.add_error('app_date',  'appointment date is full!!!')
            else:
                app_form.add_error('app_date', 'Invalid date.')
        return Response(app_form.errors, status=status.HTTP_400_BAD_REQUEST)
    
class approve_app(APIView):
    def post(request, pk):
            appoint = appointment.objects.get(id=pk)
            appoint.status = True  # approve appointment
            appoint.pending=False
            appoint.save()

            messages.success(request, "Appointment approved successfully.")
            # return redirect(reverse('view_all_app_adm.html'))

class decline_app(APIView):
    def decline_app(request, pk):
            appoint = appointment.objects.get(id=pk)
            appoint.status = False  # decline appointment
            appoint.pending=False
            appoint.save()

            messages.success(request, "Appointment declined successfully.")
 
class all_app(APIView):
    def  all_app(request):         
        app=appointment.objects.all()
        return render(request,{'appointments':app})

class Appointment_filter(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointment.objects.all().filter(ApprovalStatus="pending")
    serializer_class = appointmentStatus

