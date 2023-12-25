from models.apartment import Apartment
from models.property import Property

from util import is_a_valid_apartment

class ProperyFactory:

    @staticmethod
    def create_property_object(request_json: dict) -> Property:

        title = request_json["title"]

        square_footage = request_json["square_footage"]

        address = request_json["address"]
        
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