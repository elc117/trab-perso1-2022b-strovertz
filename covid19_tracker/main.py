from geolocation import *
from person import *
import folium

coord_geo = []
dicionarios = []

def set_markup(mapa, location, user):

    popupe = "User" + str(user.user) + "\n" + "Nome: " + str(user.name) + "\n Born: " + str(user.birthday) + "\n Covid Status: " + str(user.covid) + "\n Vaccination Status: " + str(user.vaccination)
    folium.Marker([location[0], location[1]], popup = popupe).add_to(mapa)
    return mapa   
    
def adicionar_dicionario(dicionario):
  # Adiciona o dicionário à lista "dicionarios"
  dicionarios.append(dicionario)
  
def create_map(my_location):
    mapa = folium.Map(location=[my_location[0], my_location[1]], zoom_start=1)
    popupe = "User: Strovertz" + "\n" + "Nome: Gleison Pires" + "\n Born: 2002-12-04" + "\n Covid Status: Negative" + "\n Vaccination Status: 3 Doses"
    folium.Marker([my_location[0], my_location[1]], popup = popupe).add_to(mapa)
    return mapa      

def print_test(lat_lon):
    print(lat_lon)
    print(lat_lon[1], lat_lon[0])
    
def insere_coord(lat_long):
    coord_geo.append((lat_long[0], lat_long[1]))
    
def matrix_create():
    adjacency_matrix = [[False for _ in range(len(coord_geo))] for _ in range(len(coord_geo))]
    adjacency_matrix = infection_distance(coord_geo, adjacency_matrix)
    return adjacency_matrix

def main():
    my_location = [-29.6894956, -53.811126]
    dicionario = {}
    for i in range(10):
        ip = rand_ipAddress()
        lat_lon = get_location(ip)
        mapa = create_map(my_location)
        if len(lat_lon) < 1: continue
        #Esses prins tão só pra ter algo pra ver no terminal enquanto processa os dados kkk
        print_test(lat_lon)
        user = Person(lat_lon, ip, i)
        dicionario = user_dump(user)
        dicionarios = adicionar_dicionario(dicionario)
        insere_coord(lat_lon)
        mapa = set_markup(mapa, lat_lon, user)
        
    adjacency_matrix = matrix_create()
    print(adjacency_matrix)  
    print(dicionarios)

    mapa.save("map/my_map1.html")
    
if __name__ == '__main__': 
    main()