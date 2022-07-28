from rest_framework import serializers
from core.user.models import User
from core.pos.models import Client

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("is_staff","date_joined","groups","user_permissions")
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields ="__all__"
    
   