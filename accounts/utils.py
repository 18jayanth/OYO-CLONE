import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.utils.text import slugify
from .models import *
def generateRandomToken():
    return str(uuid.uuid4())
def sendEmailToken(email,token):
    subject="verify ur email adress"
    message=f"""
    Please verify Your Account by clicking this click
    http://127.0.0.1:8000/accounts/verify-account/{token}
    """
    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)
    
def sendotptoEmail(email,otp):
    subject="OTP For Account Login"
    message=f"""
    Please use this otp to login
{otp}
    """
    send_mail(
    subject,
    message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)

def generateslug(instance):
    slug=slugify(instance.hotel_name)+(uuid.uuid4()).split('-')[0]
    if Hotels.objects.filter(slug=slug).exists():
        return generateslug(instance)
    return slug
                                                            
    