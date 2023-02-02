from User.models import CustomUser
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password')
        
        

class UserCreateSerializer(BaseUserCreateSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        fields = BaseUserCreateSerializer.Meta.fields + ('username', 'email', 'password')