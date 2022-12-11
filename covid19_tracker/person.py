import json
from json_gen_fn import *
from geolocation import *
class Person:
    
    def __init__(self, Address):
        self.name = rand_name()
        self.email = rand_email()
        self.gender = gender()
        self.birthday = birthday()
        self.cpf = cpf_gen()
        self.cellphone = cellphone()
        self.user = rand_user()
        self.address = Address
        
    
def user_dump(persona1):
    user_infos = {    
    "name": persona1.name,
    "username": persona1.user,
    "email": persona1.email,
    "gender": persona1.gender,
    "person_id": 121,
    "birthdate": persona1.birthday,
    "documents": [
        {
        "doctype": "CPF",
        "rand_cpfnumber": persona1.cpf
        }
    ],
    "address": [
        {
        "GeoLoc": persona1.address,
        #"Address": get_address(persona1.address[0], persona1.address[1]),
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
            "phone_number": persona1.cellphone,
            "type": "cellphone"
            }
            ]
        }
        ]
    }

    my_json = json.dumps(user_infos, indent=2)
    with open("data/json/user_data.json", "w") as outfile:
        outfile.write(my_json)
    print(type(my_json))