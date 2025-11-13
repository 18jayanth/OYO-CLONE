from django.shortcuts import render,redirect
from .models  import *
from django.db.models import Q
from django.contrib import messages
from .utils import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_page(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        hotel_user=HotelUser.objects.filter(email=email)
        if not hotel_user.exists():
            messages.warning(request, "User Not Found")
            return redirect('/accounts/login')
        if not hotel_user[0].is_verified:
            messages.warning(request, "Account Not Verified")
            return redirect('/accounts/login/')
            
        hotel_user=authenticate(username=hotel_user[0].username,password=password)
        
            
        if hotel_user:
            messages.success(request, "Login Successfully")
            login(request,hotel_user)
            return redirect('/accounts/login')
        messages.warning(request, "Invalid Creditianls")
        return redirect('/accounts/login/')
            
        
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        password=request.POST.get('password')
        hotel_user=HotelUser.objects.filter(
        Q(phone_number=phone_number)| Q(email=email))
        if hotel_user.exists():
            messages.error(request, "User Already Exists")
            return redirect('/accounts/register')
        hotel_user=HotelUser.objects.create(
            username=phone_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            email_token=generateRandomToken()
        )
        hotel_user.set_password(password)
        hotel_user.save()
        sendEmailToken(email,hotel_user.email_token)
        messages.success(request, "Email Successfully Sent")
        return redirect('/accounts/register')
            
    return render(request,'register.html')
def verify_email_token(request,token):
    try:
        hotel_user=HotelUser.objects.get(email_token=token)
        hotel_user.is_verified=True
        hotel_user.save()
        messages.success(request, "Email Verified")
        return redirect('/accounts/login')
    except HotelUser.DoesNotExist:
        pass
    try:
        vendor = HotelVendor.objects.get(email_token=token)
        vendor.is_verified = True
        vendor.email_token = None
        vendor.save()
        messages.success(request, "Vendor email verified successfully!")
        return redirect('/accounts/login/')
    except HotelVendor.DoesNotExist:
        pass  
    return HttpResponse("Invalid Token")
import random   
def send_otp(request,email):
    hotel_user=HotelUser.objects.filter(email=email)
    if not hotel_user.exists():
        messages.warning(request, "User Not Found")
        return redirect('/accounts/login/')
    otp=random.randint(1000,9999)
    hotel_user.update(otp=otp)
    
    sendotptoEmail(email,otp)
    return redirect(f'/accounts/verify_otp/{email}/')

def verify_otp(request,email):
    if request.method=="POST":
        otp=request.POST.get('otp')
        hotel_user=HotelUser.objects.get(email=email)
        if otp==hotel_user.otp:
            messages.success(request, "Login Successfully")
            login(request,hotel_user)
            return redirect('/accounts/login')
        messages.warning(request, "Wrong OTP")
        return redirect(f'/accounts/verify_otp/{email}')
    return render(request,'verify_otp.html')


def register_vendor(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        business_name=request.POST.get('business_name')
        password=request.POST.get('password')
        hotel_user=HotelVendor.objects.filter(
        Q(phone_number=phone_number)| Q(email=email))
        if hotel_user.exists():
            messages.error(request, "User Already Exists")
            return redirect('/accounts/register-vendor/')
        hotel_user=HotelVendor.objects.create(
            username=phone_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            business_name=business_name,
            phone_number=phone_number,
            email_token=generateRandomToken()
        )
        print("Generated token:", hotel_user.email_token)
        hotel_user.set_password(password)
        hotel_user.save()
        print("Saved token in DB:", hotel_user.email_token)
        sendEmailToken(email,hotel_user.email_token)
        messages.success(request, "Email Successfully Sent")
        return redirect('/accounts/register-vendor/')
            
    return render(request,'vendor/register_vendor.html')

def login_vendor(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        hotel_user=HotelVendor.objects.filter(email=email)
        if not hotel_user.exists():
            messages.warning(request, "User Not Found")
            return redirect('/accounts/login-vendor/')
        if not hotel_user[0].is_verified:
            messages.warning(request, "Account Not Verified")
            return redirect('/accounts/login-vendor/')
            
        hotel_user=authenticate(username=hotel_user[0].username,password=password)
        
            
        if hotel_user:
            messages.success(request, "Login Successfully")
            login(request,hotel_user)
            return redirect('/accounts/dashboard/')
        messages.warning(request, "Invalid Creditianls")
        return redirect('/accounts/login-vendor/')
            
        
    return render(request,'vendor/login_vendor.html') 

 
@login_required(login_url='login_vendor')   
def dasboard_vendor(request):
    return render(request,'vendor/dashboard_vendor.html')

@login_required(login_url='login_vendor')   
def add_hotel(request):
    if request.method=='POST':
        hotel_name=request.POST.get('hotel_name')
        hotel_description=request.POST.get('hotel_descrption')
        amenties=request.POST.get('amenties')
        hotel_price=request.POST.get('hotel_price')
        hotel_offer_price=request.POST.get('hotel_offer_price')
        hotel_location=request.POST.get('hotel_location')
        hotel_slug=generateslug(hotel_name)
        
        Hotels.objects.create(
        hotel_name=hotel_name,
        hotel_description=hotel_description,
        hotel_price=hotel_price,
        hotel_offer_price=hotel_offer_price,
        hotel_location=hotel_location,
        hotel_slug=hotel_slug
        )
        messages.success(request, "Hotel Created Successfully")
        return redirect('/accounts/dashboard/')
        
    return render(request,'vendor/add_hotel.html')
    