from django.contrib.auth.models import User
from accounts.models import *
from faker import Faker
fake = Faker()
import random

def createUser():
    for i in range(100):
        email = fake.email()
        HotelVendor.objects.create(
            email = email,
            business_name = fake.name(),
            username = email,
            first_name = fake.name(),
            phone_number = random.randint(1111111111, 9999999999)
        )


from random import choice
def createHotel():
    for i in range(100):
        hotel_vendor = choice(HotelVendor.objects.all())
        amenties = list(Amenties.objects.all())
        hotel = Hotels.objects.create(
            hotel_name=fake.company(),
            hotel_description=fake.text(),
            hotel_slug=fake.slug(),
            hotel_owner=hotel_vendor,
            hotel_price=fake.random_number(digits=4) / 100.0,
            hotel_offer_price=fake.random_number(digits=4) / 100.0,
            hotel_location=fake.address(),
            is_active=fake.boolean()
        )
        hotel.amenties.set(amenties)