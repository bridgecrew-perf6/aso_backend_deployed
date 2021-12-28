from django.contrib import admin
from chat.models import *

# Register your models here.

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Message)
