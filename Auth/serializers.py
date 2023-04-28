from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, admin, department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','last_name','email','identification_number','password']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields=['user_ID']

class RegistrationSerializer(serializers.ModelSerializer):
    #password=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','email','identification_number','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        account=User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            identification_number=self.validated_data['identification_number'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'password doesnot match'})
        account.set_password(password)
        account.save()
        return account

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields=('__all__')
        
# class LoginUserSerializer(serializers.Serializer):
#     Identification_number = serializers.IntegerField()
#     password = serializers.CharField(
#         style={'input_type': 'password'}, trim_whitespace=False)

#     def validate(self, attrs):
#         identification_number= attrs.get('identification_number')
#         password = attrs.get('password')

#         if identification_number and password:
#             if User.objects.filter(identification_number=identification_number).exists():
#                 user = authenticate(request=self.context.get('request'),
#                                     identification_number=identification_number, password=password)

#             else:
#                 msg = {'detail': 'identification_number is not registered.',
#                        'register': False}
#                 raise serializers.ValidationError(msg)

#             if not user:
#                 msg = {
#                     'detail': 'Unable to log in with provided credentials.', 'register': True}
#                 raise serializers.ValidationError(msg, code='authorization')

#         else:
#             msg = 'Must include "username" and "password".'
#             raise serializers.ValidationError(msg, code='authorization')

#         attrs['user'] = user
#         return attrs


class UserLoginSerializer(serializers.Serializer):
    identification_number = serializers.IntegerField(required=True)
    password = serializers.CharField(required=False, allow_null=True, write_only=True)

    def validate(self, attrs):
        identification_number = attrs.get('identification_number')
        user = User.objects.filter(identification_number=identification_number).exists()
        if user:
            return attrs
        else:
            msg = {
                'detail': 'User does not exists.', 'register': True}
            raise serializers.ValidationError(msg, code='authorization')


class UserLogoutSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=11, required=True)

    def validate(self, attrs):
        identification_number = attrs.get('identification_number')
        user = User.objects.filter(identification_number=identification_number).exists()
        if user:
            return attrs
        else:
            msg = {
                'detail': 'User does not exists.', 'register': True}
            raise serializers.ValidationError(msg, code='authorization')