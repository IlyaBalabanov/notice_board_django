from django.contrib import admin
from django.urls import path, include

from user_auth.views import register, login, logout, profile

urlpatterns = [
    path('register', register),
    path('login', login),
    path('logout', logout),
    path('profile', profile),
]
