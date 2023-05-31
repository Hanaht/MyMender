from django.shortcuts import render
from .serializer import FeedbackSerializer,FeedbackSeASerializer
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Feedback
from rest_framework import filters

class CreateFeedback(generics.GenericAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "Feedback": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class User_filter(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSeASerializer



































