from django.urls import path
from django.conf.urls import url
from .views import CreateUserAPIView, fetchDefaultProfile, fetchProfile, getUserNames
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^usernames/', getUserNames),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^default-profile/', fetchDefaultProfile),
    url(r'^profile/', fetchProfile),
]