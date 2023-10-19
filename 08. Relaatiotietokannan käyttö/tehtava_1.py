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


while True:
    icao = input("Syötä lentokentän ICAO-koodi:").upper()

    if 3 <= len(icao) < 5:
        break
    else:
        print("Syötteeksi käy vain 3-4 merkkiä pitkä ICAO-koodi")


dbQuery = connection.cursor()

dbQuery.execute(f"SELECT name, iso_region FROM airport WHERE ident = '{icao}'")

dbResult = dbQuery.fetchall()

if len(dbResult) == 0:
    print("haulla ei löytynyt lentokenttää.")

else:
    for x in dbResult:
        print(x)

connection.close()



