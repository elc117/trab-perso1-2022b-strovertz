from geolocation import *
from person import *
import folium

def set_markup(mapa, location, user):

    popupe = "User" + str(user.user) + "\n" + "Nome: " + str(user.name) + "\n Born: " + str(user.birthday) + "\n Covid Status: " + str(user.covid) + "\n Vaccination Status: " + str(user.vaccination)
    folium.Marker([location[0], location[1]], popup = popupe).add_to(mapa)
    return mapa
    
def main():
    dictUser = {}
    my_location = [-29.6894956, -53.811126]
    mapa = folium.Map(location=[my_location[0], my_location[1]], zoom_start=1)

    for i in range(1000):
        ip = rand_ipAddress()
        lat_lon = get_location(ip)
        if len(lat_lon) < 1: continue
        print(lat_lon)
        print(lat_lon[1], lat_lon[0])
        user = Person(lat_lon, ip)
        mapa = set_markup(mapa, lat_lon, user)
        dictUser[user.user] = user
        user_dump(user)
    
    mapa.save("map/my_map1.html")
    
if __name__ == '__main__': 
    main()