from errors.invalid_status_code_error import InvalidStatusCodeError

from flask import jsonify

def json_has_required_properties(request_json: dict):
    required_attrs =  {"title", "address", "type", "square_footage"}

    json_diff = required_attrs - request_json.keys()

    return len(json_diff) == 0


def make_error_response(error_msg, status_code):
    try:
        if status_code < 400 or status_code > 600:
            raise InvalidStatusCodeError()
    
        return jsonify({"msg": error_msg}), status_code
    except (InvalidStatusCodeError, ValueError) as err:
        internal_error_msg =  f"{err}"
        return jsonify({"msg": internal_error_msg}), 500
    


def is_a_valid_apartment(request_json: dict):
    apartment_required_attrs =  {"floor", "qty_bathrooms", "qty_rooms"}


    print(apartment_required_attrs - request_json.keys())
    
    apartment_contains_attrs = len(apartment_required_attrs - request_json.keys()) == 0

    if not apartment_contains_attrs:
        return apartment_contains_attrs
    

    qty_bathrooms, qty_rooms = int(request_json["qty_bathrooms"]), int(request_json["qty_rooms"])
    
    floor = int(request_json["floor"])


    return apartment_contains_attrs and (qty_bathrooms > 0) and (qty_rooms > 0) and floor >= 0
    