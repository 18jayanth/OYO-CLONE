from django.contrib import admin
from django.urls import path
from home.views import *
urlpatterns = [
    path("",index,name='index'),
    path("login/",login,name='login'),
    path("register/",register,name='register'),
]