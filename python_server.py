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
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        with connection:
            cursor.execute(f"SELECT tab FROM songs WHERE name = '{name}'")
            response = cursor.fetchall()
            resp = ''.join(map(str, response))
            tabsStr = ''.join(map(str, resp))
            formatted_output = tabsStr.replace(
                '\\n', '\n').replace('\\t', '\t')
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    return formatted_output


if __name__ == '__main__':
    connection = psycopg2.connect(user="manosdb", password="12345",
                                  host="127.0.0.1", port="5432", database="manosdb")
    app.run(host="0.0.0.0", port=3001, debug=True, threaded=True)
