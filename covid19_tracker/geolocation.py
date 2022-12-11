from urllib.request import urlopen
from geopy.geocoders import Nominatim
import geocoder
import csv

#tem 2 funcoes pq existe um limite de requisições que podem ser feitas por dia em cada API
#Então caso atinja o limite, basta utilizar a outra função
def get_location(ip):

    if ip:
        #url da api
        url = f"http://ip-api.com/json/{ip}"
        
        request = urlopen(url)
        data = request.read().decode()
        
        data = eval(data)
    if data['status'] != "success": 
        myAddress = []
        return myAddress
    myAddress = []
    myAddress.append(data['lat'])
    myAddress.append(data['lon'])
    
    return myAddress


def get_location2(ip):

    f = geocoder.ip(ip)

    myAddress = f.latlng
    
    return myAddress

def get_address(lati, longi):
    geolocator = Nominatim(user_agent="my_request")
    location = geolocator.reverse((lati, longi))
    print(location)
    return str(location)
