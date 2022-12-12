from geolocation import *
from person import *
import folium

coord_geo = []
dicionarios = []
dicionario = {}

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

def user_create(lat_lon, ip, i):
    user = Person(lat_lon, ip, i)
    dicionario = user_dump(user)
    dicionarios = adicionar_dicionario(dicionario)
    insere_coord(lat_lon)
    return user

#As api de consulta tem um limite de consulta diario, entao para evitar alguns problemas, vamos utilizar
#2 apis diferentes para fazermos um "reverse" a partir do IP fornecido e encontrarmos as coordenadas do nosso "usuario encovidado"
def load_balancer(ip):
    opt  = ["0","1"]
    function = random.choice(opt)
    loc = []
    if function:
        loc = get_location(ip)
    else:
        loc = get_location2(ip)
    return loc

def print_matrix(adjacency_matrix):
    linhas = len(adjacency_matrix)
    colunas = len(adjacency_matrix[0])

    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %adjacency_matrix[i][j])
            else:
                print("%d" %adjacency_matrix[i][j], end = " ")
    print()
        

def main():
    my_location = [-29.6894956, -53.811126]
    for i in range(10):
        ip = rand_ipAddress()
        lat_lon = load_balancer(ip)
        mapa = create_map(my_location)
        if len(lat_lon) < 1: continue
        
        #Esses prints tão só pra ter algo pra ver no terminal enquanto processa os dados kkk
        print_test(lat_lon)
        
        user = user_create(lat_lon, ip, i)
        mapa = set_markup(mapa, lat_lon, user)
        
    adjacency_matrix = matrix_create()
    print_matrix(adjacency_matrix)  
    #print(dicionarios)

    mapa.save("map/my_map1.html")
    
if __name__ == '__main__': 
    main()