from django.contrib import admin
from django.urls import path
from home.views import *
urlpatterns = [
    path("",index,name='index'),
    path("hotel_detail/<slug>/",hotel_detail,name='hotel_detail')
   
]