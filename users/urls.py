from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from setup.urls import router
from users import views


# Serializers define the API representation.
# The urls router
router.register(r'api/users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
]
