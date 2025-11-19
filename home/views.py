from django.shortcuts import render
from accounts.models import *
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from django.views.decorators.cache import cache_page

# Create your views here.
#@cache_page(60 * 15)
def index(request):
    hotels=Hotels.objects.all().select_related('hotel_owner')
    if request.GET.get('search'):
        hotels=hotels.filter(hotel_name__icontains=request.GET.get('search'))
    if request.GET.get('sort_by'):
        sort_by=request.GET.get('sort_by')
        if sort_by=='sort_low':
            hotels=hotels.order_by('hotel_offer_price')
        elif sort_by=='sort_high':
            hotels=hotels.order_by('-hotel_offer_price')
            
    
    return render(request,'index.html',context={'hotels':hotels})

def hotel_detail(request,slug):
    hotel=Hotels.objects.get(hotel_slug=slug)
    if request.method=="POST":
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
        start_date=datetime.strptime(start_date,'%Y-%m-%d')
        end_date=datetime.strptime(end_date,'%Y-%m-%d')
        no_of_days=(end_date-start_date).days
        if no_of_days<=0:
            messages.warning(request,"Invalid Booking date")
            return HttpResponseRedirect(request.path_info)
        HotelBookings.objects.create(
            hotel=hotel,
            booking_user=HotelUser.objects.get(id=request.user.id),
            booking_start_date=start_date,
            booking_end_date=end_date,
            price=hotel.hotel_offer_price*no_of_days
            
        )
        messages.success(request,"Booking Done")
        return HttpResponseRedirect(request.path_info)
    context={'hotel':hotel}
    return render(request,'hotel_detail.html',context)