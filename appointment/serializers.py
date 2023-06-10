from rest_framework import serializers
from .models import appointment

class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields=['service_ID','dep_ID','app_date']
        
    def save(self,request):
        user_id = request.user.identification_number
        request.session['user_id'] = user_id
        appo=appointment(
            service_ID=self.validated_data['service_ID'],
            dep_ID=self.validated_data['dep_ID'],
            app_date=self.validated_data['app_date'],
            customer_ID= request.session['user_id']
        )
        appo.save()
        return appo
    
class appointmentStatus(serializers.ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'