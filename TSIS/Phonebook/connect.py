import psycopg2
from config import host, user, password, db_name, port

def connect():
    return psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
        port=port
    )