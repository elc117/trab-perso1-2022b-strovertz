from geolocation import *
from person import *
import folium

def set_markup(mapa, user_data):
    j = 1
    for i in user_data:
        popupe = "user" + str(j) + "\n" + "AudioDump: " + str(i[3]) + "\nWebcamDump: " + str(i[4])
        folium.Marker([i[1], i[2]], popup = popupe).add_to(mapa)
        j = j + 1
    return mapa
    
def main():
    
    lat_lon = get_location()
    #user_data = read_data()
    print(lat_lon)
    print(lat_lon[1], lat_lon[0])
    mapa = folium.Map(location=[lat_lon[0], lat_lon[1]], zoom_start=1)
    folium.Marker([lat_lon[0], lat_lon[1]], popup = "teste").add_to(mapa)
    persona1 = Person(lat_lon)
    user_dump(persona1)
    #mapa = set_markup(mapa, user_data)
    mapa.save("map/my_map1.html")
    
if __name__ == '__main__': 
    main()