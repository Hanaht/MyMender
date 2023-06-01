from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import appointment
from .serializers import appSerializer,appointmentStatus
from rest_framework import filters

class schedule_app(APIView):
    serializer_class=appSerializer
    
    def get(self, request, format=None):
        app = appointment.objects.all()
        serializer = appSerializer(app, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = appSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def acceptRejectAppointment(request):
    if request.method == 'POST':
        appstatus = appointment.objects.get(ID=request.POST('ID'))
        if request.POST.get('ApprovalStatus'):
            appstatus.status = request.POST.get('ApprovalStatus')
            appstatus.save()

class Appointment_filter(generics.ListCreateAPIView):
    search_fields = ['ApprovalStatus']
    filter_backends = (filters.SearchFilter,)
    queryset = appointment.objects.all().filter(ApprovalStatus="pending")
    serializer_class = appointmentStatus
