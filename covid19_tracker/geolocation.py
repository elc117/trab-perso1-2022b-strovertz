import random
from geopy.geocoders import Nominatim
import geocoder
import csv

def get_location():

    f = geocoder.ip("2804:7f6:8087:6301::1")

    myAddress = f.latlng
    
    return myAddress

def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))
    print(location)
    return location
