from django.contrib import admin
from django.urls import path
from accounts.views import *
urlpatterns = [
    path("login/",login_page,name='login'),
    path("register/",register,name='register'),
    path("verify-account/<token>/",verify_email_token,name='verify_email_token'),
]