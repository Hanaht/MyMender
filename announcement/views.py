from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from .models import department, announcement
from .serializers import announceSerializer, departmentSerializer

class announce_list(APIView):
    serializer_class=announceSerializer
    
    def get(self, request, format=None):
        announce = announcement.objects.all()
        serializer = announceSerializer(announce, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = announceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class dep(APIView):
    serializer_class=departmentSerializer
    
    def get(self, request, format=None):
        dept = department.objects.all()
        serializer = departmentSerializer(dept, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = departmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
