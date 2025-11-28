from rest_framework import serializers
from .models import LoginData

class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginData
        fields = '__all__'
