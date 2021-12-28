from django.db.models.base import Model
from rest_framework.viewsets import ModelViewSet
from chat.models import *
from chat.serializers import *

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer