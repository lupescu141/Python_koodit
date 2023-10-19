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


dbQuery = connection.cursor()

userInput = input("Kirjoita lentokenttien maatunnus:").upper()

dbQuery.execute(f"SELECT type FROM airport WHERE iso_country = '{userInput}' AND type = 'small_airport'")
smallAirports = dbQuery.fetchall()
print(f"Pienten lentokenttien määrä: {len(smallAirports)}")

dbQuery.execute(f"SELECT type FROM airport WHERE iso_country = '{userInput}' AND type = 'heliport'")
heliports = dbQuery.fetchall()
print(f"Helikopterikenttien määrä: {len(heliports)}")

dbQuery.execute(f"SELECT type FROM airport WHERE iso_country = '{userInput}' AND type = 'closed'")
closedAirports = dbQuery.fetchall()
print(f"Suljettujen lentokenttien määrä: {len(closedAirports)}")

connection.close()



