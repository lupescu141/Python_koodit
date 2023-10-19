import geopy.distance
import mysql.connector
from mysql.connector import errorcode
from geopy.distance import geodesic

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

dbQuery = connection.cursor()


userinput = input("Syötä ensimmäisen lentokentän ICAO tunnus:")
dbQuery.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{userinput}'")
cordinates1 = dbQuery.fetchall()


userinput = input("Syötä toisen lentokentän ICAO tunnus:")
dbQuery.execute(f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{userinput}'")
cordinates2 = dbQuery.fetchall()

print(f"Kohteiden välinen matka on: {geodesic(cordinates1, cordinates2).km :.0f}km")
