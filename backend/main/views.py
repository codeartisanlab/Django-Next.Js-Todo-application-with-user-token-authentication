from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer,TodoSerializer,WebsiteViewsSerializer
from .models import TodoList,WebsiteViews

class UserApiView(ListCreateAPIView):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class TodoApiListView(ListCreateAPIView):
    serializer_class=TodoSerializer
    queryset=TodoList.objects.all()

class TodoApiUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class=TodoSerializer
    queryset=TodoList.objects.all()

class WebsiteViewsApi(ListCreateAPIView):
    serializer_class=WebsiteViewsSerializer
    queryset=WebsiteViews.objects.all()


