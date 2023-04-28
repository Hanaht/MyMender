import json
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
from .serializers import UserLoginSerializer, UserLogoutSerializer, UserSerializer, AdminSerializer, departmentSerializer,RegistrationSerializer

class user_list(APIView):
    serializer_class=UserSerializer
    
    def get(self, request, format=None):
        account =User.objects.all()
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

class admin_list(APIView):
    serializer_class=AdminSerializer
    
    def get(self, request, format=None):
        admins =admin.objects.all()
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = AdminSerializer(data=request.data)
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
    

# @api_view(['POST'])
# def login(request):
#     serializer = AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.validated_data['user']
#     _, token = AuthToken.objects.create(user)
#     return Response({
#         #'user_data': serialize_user(user),
#         'token': token
#     })
        

# class Login(APIView):
#     #permission_classes = (permissions.AllowAny,)

#    def post(self, request):
#         ser_data =LoginUserSerializer(data=request.POST)
#         if ser_data.is_valid():
#             data = ser_data.validated_data
#             user = User.objects.get(identification_number=data['identification_number'])
#             if user:
#                 if user.check_password(data['password']):
#                     login(request, user)
#                     user.save()
#                     return Response(ser_data.data, status=status.HTTP_200_OK)
#                 return Response({'detail': 'inter password or otp'})
#             return Response({'detail': 'user does not exists'})
#         return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer_class=UserLoginSerializer
    def post(self, request):
        ser_data =UserLoginSerializer(data=request.POST)
        if ser_data.is_valid():
            data = ser_data.validated_data
            user = User.objects.get(identification_number=data['identification_number'])
            if user:
                if user.check_password(data['password']):
                    login(request, user)
                    user.save()
                    return Response(ser_data.data, status=status.HTTP_200_OK)
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