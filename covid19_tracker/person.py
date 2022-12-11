import json
from json_gen_fn import *
from geolocation import *
class Person:
    
    def __init__(self, Address, ip):
        self.name = rand_name()
        self.email = rand_email()
        self.gender = gender()
        self.birthday = birthday()
        self.cpf = cpf_gen()
        self.cellphone = cellphone()
        self.user = rand_user()
        self.address = Address
        self.ipAddress = ip
        self.covid = covid_status()
        self.vaccination = vaccination_status()
        
    
def user_dump(persona):
    user_infos = {    
    "name": persona.name,
    "username": persona.user,
    "email": persona.email,
    "gender": persona.gender,
    "person_id": 121,
    "birthdate": persona.birthday,
    "documents": [
        {
        "doctype": "CPF",
        "rand_cpfnumber": persona.cpf
        }
    ],
    "Covid19": [
        {
        "Status": persona.covid,
        "Vaccination Status": persona.vaccination
        }
    ],
    "address": [
        {
        "IpAddress": persona.ipAddress,
        "GeoLoc": persona.address,
        "Address": get_address(persona.address[0], persona.address[1]),
        "city": "Williamsburg Street",
        "address_number": 257,
        "country_residence": "Saint Lucia",
        "province": "Virginia",
        "street": "Laurelton",
        "zip": 26492
        }
    ],
    "contacts": [
        {
        "phones": [
            {
            "phone_number": persona.cellphone,
            "type": "cellphone"
            }
            ]
        }
        ]
    }

    my_json = json.dumps(user_infos, indent=2)
    with open("data/json/users/user_data" + persona.user +".json", "w") as outfile:
        outfile.write(my_json)
    print(type(my_json))