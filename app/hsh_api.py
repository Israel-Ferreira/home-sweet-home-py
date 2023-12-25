from flask import Flask, request, jsonify, Response

from bson.errors import InvalidId

from dotenv import load_dotenv

from util import make_error_response

from config.mongodb_connection import connect_in_mongo, load_db_env_vars

from errors import ValidationError, UnprocessableEntityError, NotFoundError

import usecases


load_dotenv()

db_env_vars = load_db_env_vars()


app = Flask(__name__)

mongo = connect_in_mongo(**db_env_vars)

db = mongo["home-sweet-home-db"]


@app.get("/properties")
def list_properties():
    houses = usecases.get_all(db)

    response = Response(response=houses, status=200,
                        mimetype="application/json")
    return response


@app.post("/properties")
def add_new_property():
    property_received = request.json

    try:
        result = usecases.insert_house(property_received, db)

        resource_url = f"http://localhost:9090/properties/{result.inserted_id}"

        resp = {
            "msg": "Anúncio Criado com Sucesso",
            "resource_url": resource_url
        }

        return jsonify(resp), 201

    except ValueError as _:
        return make_error_response("Apartamento Inválido", 400)

    except ValidationError as valid_error:
        return make_error_response(valid_error.msg, 400)

    except UnprocessableEntityError as unpe_err:
        return make_error_response(unpe_err.msg, unpe_err.status_code)


@app.get("/properties/<property_id>")
def get_house_by_id(property_id: str):
    try:
        result = usecases.get_property_by_id(property_id, db)
        response = Response(response=result, status=200,
                            mimetype="application/json", content_type="application/json")
        return response
    except InvalidId:
        return make_error_response("ID Inválido", 400)
    except NotFoundError as error_404:
        return make_error_response(error_404.msg, 404)


@app.put("/properties/<property_id>")
def update_announcement(property_id: str):
    pass


@app.delete("/properties/<propery_id>")
def archive_property(property_id: str):
    pass


if __name__ == "__main__":
    API_PORT = 9090
    app.run(host="0.0.0.0", port=API_PORT)
