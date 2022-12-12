from urllib.request import urlopen
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import geocoder

infection_list = []

#Como iria demorar muito pra criar algo como 100000 de pessoas, preferi aumentar o range de infecção, então caso alguém se encontre a 5000 km ou menos
#de distância de um infectado, ele sera considerado como possível infectado e adicionado na matriz de adjacencia
def infection_distance(coord_geo, matrix_adjacencia):
    for i in range(len(coord_geo)):
        for j in range(len(coord_geo)):
            # Função geodesic da biblioteca Geopy para calcular a distância entre os pontos
            distance = geodesic(coord_geo[i], coord_geo[j]).kilometers
            # Verificamos se a distância é menor que 5000 km
            if distance < 5000:
                # Se for, armazenamos "true" na matriz de adjacência
                matrix_adjacencia[i][j] = True
    return matrix_adjacencia            
        

#tem 2 funcoes pq existe um limite de requisições que podem ser feitas por dia em cada API
#Então caso atinja o limite, basta utilizar a outra função
def get_location(ip):

    myAddress = []
    
    if ip:
        #url da api
        url = f"http://ip-api.com/json/{ip}"
        
        request = urlopen(url)
        data = request.read().decode()
        
        data = eval(data)
    if data['status'] != "success": 
        return myAddress
    
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
