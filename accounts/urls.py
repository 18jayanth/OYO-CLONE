from django.contrib import admin
from django.urls import path
from accounts.views import *
urlpatterns = [
    path("login/",login_page,name='login'),
     path("logout/",logout_view,name='logout'),
    path("register/",register,name='register'),
    path("send_otp/<email>/",send_otp,name='send_otp'),
    path("login-vendor/",login_vendor,name='login_vendor'),
    path("register-vendor/",register_vendor,name='register_vendor'),
    path("dashboard/",dasboard_vendor,name='dashboard'),
    path("add-hotel/",add_hotel,name='add_hotel'),
    path("edit_hotel/<slug>/",edit_hotel,name='edit_hotel'),
    path("<slug>/upload_images/",upload_images,name='upload_images'),
    path("delete_image/<id>/",delete_image,name='delete_image'),
    path("verify_otp/<email>/",verify_otp,name='verify_otp'),
    path("verify-account/<token>/",verify_email_token,name='verify_email_token'),
]