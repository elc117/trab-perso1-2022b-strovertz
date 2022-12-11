import string as string
import random as random
from cpf_generator import CPF

def rand_name():
    with open("data/wordlists/names.txt", "r") as file:
        allText = file.read()
        name_list = list(map(str, allText.split()))
        name = random.choice(name_list)
        surname = random.choice(name_list)
    return name + " " + surname

def rand_user():
    with open("data/wordlists/usernames.txt", "r") as file:
        allText = file.read()
        user_list = list(map(str, allText.split()))
        username = random.choice(user_list)
    return username

def gender():
    opt  = ["male", "female"]
    gender = random.choice(opt)
    return gender

def get_lat(lat):
    dec_lat = random.random()/100
    return lat+dec_lat

def get_lon(lon):
    dec_lon = random.random()/100
    return lon+dec_lon
        
def rand_email():
    return rand_user() + "@fakemail.com"

def birthday():
    return  str(random.randint(1960, 2005)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 28))

def cpf_gen():
    return CPF.generate()

def cellphone():
    country = str(random.randint(1, 200))
    if country != 55:
        return "+" + country + " " + str(random.randint(111111111, 999999999))
    return "+" + country + " " + str(random.randint(41, 55)) + " " + str(random.randint(111111111, 999999999)) # Se for BR acrescenta o DDD