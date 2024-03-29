from django.urls import path
from .views import UserApiView

urlpatterns=[
    path('users',UserApiView.as_view())
]