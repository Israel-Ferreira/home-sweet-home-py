from models.apartment import Apartment
from models.property import Property

from models.address import Address

from util import is_a_valid_apartment

class ProperyFactory:

    @staticmethod
    def create_property_object(request_json: dict) -> Property:

        title = request_json["title"]

        square_footage = request_json["square_footage"]

        address_obj = request_json["address"]

        address =  Address(
            address_obj["public_place"],
            address_obj["number"],
            address_obj["neighborhood"],
            address_obj["city"],
            address_obj["state"],
            address_obj["country"],
            address_obj["latitude"],
            address_obj["longitude"],
            ""
        )
        
        if request_json["type"] == "apartment" :
            if is_a_valid_apartment(request_json):
                return Apartment(
                    title, 
                    square_footage, 
                    address, 
                    request_json["qty_bathrooms"], 
                    request_json["qty_rooms"], 
                    request_json["floor"],
                    request_json["pets_is_allowed"]
                )
            else:
                raise ValueError("Erro de Validação: requisição não contém os campos necessários para o tipo Apartamento")
            

        

        return None