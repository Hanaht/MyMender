from rest_framework import serializers
from .models import appointment

class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields=['customer_ID','admin_service_ID ','dep_ID','app_date']