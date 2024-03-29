from django.shortcuts import render

from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListCreateAPIView

class UserApiView(ListCreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()


