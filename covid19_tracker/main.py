from geolocation import *
from person import *
import folium
import numpy

#dicionarios é uma lista que contem todos os dicionarios, ou melhor, os usuários. 
coord_geo = []
dicionarios = []
dicionario = {}

def set_markup(mapa, location, user):
    popupe = "User: " + str(user.user) + "\n" + "Nome: " + str(user.name) + "\n Born: " + str(user.birthday) + "\n Covid Status: " + str(user.covid) + "\n Vaccination Status: " + str(user.vaccination)
    if str(user.covid) == "Positive":
        icon = folium.features.CustomIcon("icon/Biohazard.png",
                                      icon_size=(14, 14))
        folium.Marker([location[0], location[1]], popup = popupe, icon=icon, icon_size=(30,30)).add_to(mapa)
        folium.CircleMarker([location[0], location[1]], radius=50, popup = "Infected Area", color = "red", fill = True, fill_color="lightred").add_to(mapa)
        return mapa
    else:
        folium.Marker([location[0], location[1]], popup = popupe, icon=folium.Icon(color='lightblue')).add_to(mapa)
        return mapa   
    
def adicionar_dicionario(dicionario):
  #Adiciona o dicionário à lista "dicionarios"
  dicionarios.append(dicionario)
  
def create_map(my_location):
    #Retorna um mapa com a minha localização
    mapa = folium.Map(location=[my_location[0], my_location[1]], zoom_start=1)
    popupe = "User: Strovertz" + "\n" + "Nome: Gleison Pires" + "\n Born: 2002-12-04" + "\n Covid Status: Negative" + "\n Vaccination Status: 3 Doses"
    folium.Marker([my_location[0], my_location[1]], popup = popupe, icon=folium.Icon(color='lightgreen', icon='home')).add_to(mapa)
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
    opt  = ["1"]
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
    #vou salvar apenas pra caso precise consultar algum específico pra verificar a as adjacencias, 
    #quando eu  aplicar uma matriz 1000x1000 vai ficar mais dificil de visualizar pelo prompt
    file = open("data/adjacency_matrix.txt", "w+")
    for i in range(linhas):
        for j in range(colunas):
            if(j == colunas - 1):
                print("%d" %adjacency_matrix[i][j])
                file.write(str(adjacency_matrix[i][j]))
            else:
                print("%d" %adjacency_matrix[i][j], end = " ")
                file.write(str(adjacency_matrix[i][j]))
        file.write('\n')
        
    print()
        
def dict_list_dump():
    with open("data/json/users/all_usr.json", "w", encoding ='utf8') as outfile:
        json.dump(dicionarios, outfile, indent=4, sort_keys=True)
        outfile.close()

def matrix_actions():
    adjacency_matrix = matrix_create()
    print_matrix(adjacency_matrix)    
    
def first_action():
    my_location = [-29.6894956, -53.811126]
    mapa = create_map(my_location)

    for i in range(1000):
        ip = rand_ipAddress()
        lat_lon = load_balancer(ip)
        if len(lat_lon) < 1: continue
        #Esses prints tão só pra ter algo pra ver no terminal enquanto processa os dados kkk
        print_test(lat_lon)
        user = user_create(lat_lon, ip, i)
        mapa = set_markup(mapa, lat_lon, user)
    mapa.save("map/my_map1.html")
    matrix_actions()
    #return mapa

def main():
    first_action()
    dict_list_dump()
    
if __name__ == '__main__': 
    main()