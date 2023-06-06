import json
from django.shortcuts import render, redirect
from django.forms import ValidationError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_auth.views import LoginView as RestLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken, TokenAuthentication
from rest_framework import status
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import authenticate,login,logout
from rest_framework.views import APIView
from .models import User, admin, department
from MymenderProject.decorators import admin_only, customer_required, superuser_required
from .serializers import RegisteradminSerializer, UserLoginSerializer, UserLogoutSerializer, UserSerializer, AdminSerializer, departmentSerializer,RegistrationSerializer,UserSerializer1
from services import urls as url
from appointment import models as appo

class user_list(APIView):
    serializer_class=UserSerializer
    
    def get(self, request, format=None):
        account =User.objects.filter(is_customer=True).all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)

class register_user(APIView):
    serializer_class=RegistrationSerializer
    
    def get(self, request, format=None):
        account =User.objects.all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class register_admin(APIView):
    serializer_class=RegisteradminSerializer
    
    # def get(self, request, format=None):
    #     account =User.objects.all()
    #     serializer = UserSerializer(account, many=True)
    #     return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RegisteradminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class admin_list(APIView):
    serializer_class=UserSerializer
    
    def get(self, request, format=None):
        account =User.objects.filter(is_admin=True).all()
        serializer = UserSerializer(account, many=True)
        return Response(serializer.data)

#@admin_only
class dep(APIView):
    serializer_class=departmentSerializer
    #@customer_required(login_url='api/auth/login', redirect_field_name='', message='You are not authorised to view this page.')
    def get(self, request, format=None):
        dept = department.objects.all()
        serializer = departmentSerializer(dept, many=True)
        return Response(serializer.data)
  
    #@customer_required(login_url='api/auth/login', redirect_field_name='', message='You are not authorised to view this page.')
    def post(self, request, format=None):
        serializer = departmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    serializer_class=UserLoginSerializer
    def post(self, request):
        ser_data =UserLoginSerializer(data=request.POST)
        if ser_data.is_valid():
            data = ser_data.validated_data
            user = User.objects.get(identification_number=data['identification_number'])
        
            if user:
                if user.check_password(data['password']):
                    if user.is_customer==True:
                        login(request, user)
                        user.save()
                        return Response({'sucessfully logged'})
                        # return redirect("../../services/service_list")
                    #return Response(ser_data.data, status=status.HTTP_200_OK)
                    if user.is_admin==True:
                        login(request, user)
                        user.save()
                        return redirect("user_list")
                    
                return Response({'detail': 'inter password'})
            return Response({'detail': 'user does not exists'})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):

    def post(self, request):
        ser_data =UserLogoutSerializer(data=request.POST)
        if ser_data.is_valid():
            data = ser_data.validated_data
            user = User.objects.get(identification_number=data['identification_number'])
            if user:
                logout(request)
                return Response(ser_data.data, status=status.HTTP_200_OK)
            return Response({'detail': 'user does not exists'})
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class admin_dashboard(APIView):
    def get(self,request):
        user=User.objects.all()
        # app_model=appo.appointment 
        app=appo.appointment.objects.all()

        total_user=user.filter(is_customer=True).count()
        total_appointment=app.count()
        # delivered= order.filter(status='delivered').count()
        pending= app.filter(pending=True).count()
        approved= app.filter(status=True).count()
        declined= app.filter(status=False).count()
        context={'users':user,'apps':app,'total_user':total_user,'total_appointment':total_appointment,pending:'pending',approved:'approved',declined:'declined'}
        return render(request, 'admin_dashboard.html',context)