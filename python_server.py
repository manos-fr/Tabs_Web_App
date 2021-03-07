import psycopg2
from psycopg2 import Error
from json import dumps
import json
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/song_name')
def get_tab():
    name = request.args.get('name')
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="manosdb", password="12345", 
        host="127.0.0.1", port="5432", database="manosdb")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT version();")

        with connection:
            cursor.execute(f"SELECT tab FROM songs WHERE name = '{name}'")  
            response = cursor.fetchall()  
            resp = ''.join(map(str, response))
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
    return json.dumps(resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3001,debug=True,threaded=True)