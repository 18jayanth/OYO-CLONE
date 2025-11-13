from django.contrib import admin
from django.urls import path
from accounts.views import *
urlpatterns = [
    path("login/",login_page,name='login'),
    path("register/",register,name='register'),
    path("send_otp/<email>/",send_otp,name='send_otp'),
    path("login-vendor/",login_vendor,name='login_vendor'),
    path("register-vendor/",register_vendor,name='register_vendor'),
    path("dashboard/",dasboard_vendor,name='dashboard'),
     path("add-hotel/",add_hotel,name='add_hotel'),
    path("verify_otp/<email>/",verify_otp,name='verify_otp'),
    path("verify-account/<token>/",verify_email_token,name='verify_email_token'),
]