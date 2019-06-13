from django.shortcuts import render

from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import LoginView


class LoginViewCustom(LoginView):
    authentication_classes = (TokenAuthentication,)