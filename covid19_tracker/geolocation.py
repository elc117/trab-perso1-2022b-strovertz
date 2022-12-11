import random
from geopy.geocoders import Nominatim
import geocoder
import csv

def get_location(ip):

    f = geocoder.ip(ip)

    myAddress = f.latlng
    
    return myAddress

def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))
    print(location)
    return str(location)
