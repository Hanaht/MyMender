from rest_framework import serializers
from .models import announcement, department

class announceSerializer(serializers.ModelSerializer):
    class Meta:
        model = announcement
        fields=('__all__')

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields=('__all__')