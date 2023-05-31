from rest_framework import serializers
from .models import Feedback
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('title','description',)
class FeedbackSeASerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
        
        