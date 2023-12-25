import os
import sys

from pymongo import MongoClient


def connect_in_mongo(host, port, database, user="", password=""):

    if user == "" and password == "":
        cnstr = f"mongodb://{host}:{port}/{database}"
    else:
        cnstr = f"mongodb://{user}:{password}@{host}:{port}/{database}"

    print(cnstr)

    client = MongoClient(cnstr, authSource="admin")

    try:
        client.admin.command("ping")
        return client
    except Exception as e:
        print(f"Problema ao conectar com a base de dados: {e}")
        sys.exit(1)


def load_db_env_vars():
    db_host = os.getenv("API_MONGO_DB_HOST")
    db_port = os.getenv("API_MONGO_DB_PORT")

    db_name = os.getenv("API_MONGO_DB_DATABASE_NAME")

    db_user = os.getenv("API_MONGO_DB_USER")

    db_password = os.getenv("API_MONGO_DB_PASSWORD")

    return {
        "host": db_host,
        "port": db_port,
        "database": db_name,
        "user": db_user,
        "password": db_password
    }
