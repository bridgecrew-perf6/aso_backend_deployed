from rest_framework import urlpatterns
from chat.api import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('chat/messages', MessageViewSet)
router.register('chat/users', UserViewSet)

urlpatterns = router.urls