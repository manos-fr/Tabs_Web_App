import psycopg2
from psycopg2 import Error
from json import dumps
import json

def main():
    text = 'Dark Necessities.txt'
    with open(text) as txt:
        data = txt.read()
        db(data)

def db(data):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="manosdb", password="12345", 
        host="127.0.0.1", port="5432", database="manosdb")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT version();")

        with connection:
            # cursor.execute(f"INSERT INTO songs(id, name, tab) VALUES(3,'Dark Necessities', {data})")
            cursor.execute(f"UPDATE songs SET tab = '{data}' WHERE id = 2")    
            # cursor.execute(f"INSERT INTO songs(id, name, tab) VALUES(2,'Dark Necessities', 'mike')")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()

if __name__ == '__main__':
    main()