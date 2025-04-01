from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['id'] = user.id

        #todos los atributos del modelo
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id  
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'name',
            'surname',
            'control_number',
            'age',
            'tel',
            'join_date'
        ]