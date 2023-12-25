from flask import Flask, request, jsonify

from dotenv import load_dotenv

from util import json_has_required_properties, make_error_response
from models.property_factory import ProperyFactory

from config.mongodb_connection import connect_in_mongo,load_db_env_vars


load_dotenv()

db_env_vars = load_db_env_vars()

app = Flask(__name__)

mongo =  connect_in_mongo(**db_env_vars)
db =  mongo["home-sweet-home-db"]


@app.route("/properties")
def list_properties():
    return []


@app.post("/properties")
def add_new_property():
    property_received = request.json

    json_contain_required_attrs = json_has_required_properties(property_received)


    if not json_contain_required_attrs:
        return make_error_response("Erro de Validação: Campos Obrigatórios Ausentes no Corpo da Requisição", 400)

    if property_received["title"] is None or property_received["title"] == "":
        return make_error_response("Erro de Validação: O titulo do Anúncio não deve ficar em branco", 400)

    if property_received["square_footage"] is None or property_received["square_footage"] < 0:
        return make_error_response("Erro de Validação: a metragem do imovel não deve estar com o valor nulo ou menor que 0", 400)

    if property_received["type"] is None or property_received["type"] == "":
        return make_error_response("Erro de Validação: O tipo do imóvel não deve estar com o valor nulo ou em branco", 400)
    

    try:
        property_obj =  ProperyFactory.create_property_object(property_received)

        if property_obj is not None:
            dict_property =  property_obj.to_dict()
            
            result =  db.houses.insert_one(dict_property)

            resp =  {
                "inserted_id": result.inserted_id
            }

            return jsonify(resp), 201
        else:
            return make_error_response("Erro ao criar o objeto", 422)

    except ValueError as _:
        return make_error_response("Apartamento Inválido", 400)


    


@app.get("/properties/:property_id")
def get_property_by_id(property_id: str):
    pass


@app.put("/properties/:property_id")
def update_announcement(property_id: str):
    pass


@app.delete("/properties/:propery_id")
def archive_property(property_id: str):
    pass


if __name__ == "__main__":
    API_PORT = 9090
    app.run(host="0.0.0.0", port=API_PORT)
