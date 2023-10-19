from flask import Flask, request
import mysql.connector
from mysql.connector import errorcode

database = {'user': 'root',
            'password': 'h93cx3et',
            'host': '127.0.0.1',
            'database': 'flight_game',
            'raise_on_warnings': True}

try:
    connection = mysql.connector.connect(**database)

except mysql.connector.errors.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")

    else:
        print(err)

else:
    print("Connection: Succesful")

app = Flask(__name__)


@app.route('/kenttä/<icao>')
def kentta(icao):

    db_query = connection.cursor()
    db_query.execute(f"SELECT name FROM airport WHERE ident = '{str(icao).upper()}'")
    db_result = db_query.fetchone()

    vastaus = {
        "ICAO": str(icao).upper(),
        "Name": db_result[0],
    }

    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)