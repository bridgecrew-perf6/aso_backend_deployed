from django.core.exceptions import FieldDoesNotExist
from rest_framework import serializers
from chat.models import *
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializerForMessages(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Message
        fields = '__all__'