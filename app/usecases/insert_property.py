from util import json_has_required_properties
from factories.factory import ProperyFactory

from errors import ValidationError, UnprocessableEntityError




def insert_house(request_json, db):
    json_contain_required_attrs = json_has_required_properties(request_json)

    if not json_contain_required_attrs:
        raise ValidationError("Erro de Validação: Campos Obrigatórios Ausentes no Corpo da Requisição")

    if request_json["title"] is None or request_json["title"] == "":
        raise ValidationError("Erro de Validação: O titulo do Anúncio não deve ficar em branco")

    if request_json["square_footage"] is None or request_json["square_footage"] < 0:
        raise ValidationError("Erro de Validação: a metragem do imovel não deve estar com o valor nulo ou menor que 0")

    if request_json["type"] is None or request_json["type"] == "":
        raise ValidationError("Erro de Validação: O tipo do imóvel não deve estar com o valor nulo ou em branco")
    

    property_obj =  ProperyFactory.create_property_object(request_json)

    if property_obj is not None:
        dict_property =  property_obj.to_dict()
        
        result =  db.houses.insert_one(dict_property)

        return result
    else:
        raise UnprocessableEntityError("Erro ao criar o objeto")