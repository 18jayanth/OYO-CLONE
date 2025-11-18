from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HotelUser(User):
    profile_picture=models.ImageField(upload_to='profile')
    phone_number=models.CharField(max_length=100,unique=True)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    otp=models.CharField(max_length=10,null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    def __str__(self):
        return self.email
    class Meta:
        db_table='hotel_user'
class HotelVendor(User):
    profile_picture=models.ImageField(upload_to='profile')
    business_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100,unique=True)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    otp=models.CharField(max_length=10,null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    def __str__(self):
        return self.email
    class Meta:
        db_table='hotel_vendor'
class Amenties(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="hotels")
    def __str__(self):
        return self.name
    
class Hotels(models.Model):
    hotel_name=models.CharField(max_length=100)
    hotel_description=models.TextField()
    hotel_slug=models.SlugField(max_length=100,unique=True)
    hotel_owner=models.ForeignKey(HotelVendor,on_delete=models.CASCADE,related_name='hotels')
    amenties=models.ManyToManyField(Amenties)
    hotel_price=models.FloatField()
    hotel_offer_price=models.FloatField()
    hotel_location=models.TextField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.hotel_name
    
class HotelImages(models.Model):
    hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE,related_name='hotel_images')
    image=models.ImageField(upload_to="hotels")
    
class HotelManager(models.Model):
    hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE,related_name='hotel_manager')
    manager_name=models.CharField(max_length=100)
    manager_phone=models.CharField(max_length=100)
    
    