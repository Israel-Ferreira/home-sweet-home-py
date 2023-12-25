from bson import ObjectId, json_util

from errors import NotFoundError


def get_all(db):
    houses =  json_util.dumps(db.houses.find({}))
    return houses


def get_property_by_id(property_id, db):
    object_id  = {"_id": ObjectId(property_id)}
    
    result =  db.houses.find_one(object_id)

    if result is None:
        raise NotFoundError
    

    return  json_util.dumps(result)