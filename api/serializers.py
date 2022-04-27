from dataclasses import fields
from rest_framework import serializers
from queijaria.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'groups']
