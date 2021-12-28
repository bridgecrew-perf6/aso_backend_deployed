from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    text = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True);