
from django.urls import path
from .views import UserApiView,TodoApiListView,TodoApiUpdateView,WebsiteViewsApi
from rest_framework.authtoken import views

urlpatterns=[
    path('users/',UserApiView.as_view()),
    path('todos/',TodoApiListView.as_view()),
    path('todos/<pk>/',TodoApiUpdateView.as_view()),
    path('total-views/',WebsiteViewsApi.as_view()),
    path('token-auth', views.obtain_auth_token)
]