import mariadb #for this to work need to import mariadb

connection = mariadb.connect(
host ='127.0.0.1',
port = 3306,
user = 'root',
password = 'princess',
database = 'flight_game',
autocommit = True
)

#print("Connected to MariaDB!")

countries = {}

# Function to get countries
def get_countries(connection, continent=None):
    cursor = connection.cursor()
    if continent:
        sql = "SELECT name FROM country WHERE continent = 'EU'"
        cursor.execute(sql, (continent,))

    results = cursor.fetchall()

    if results:
        if continent:
            print(f"Countries in {continent}:")
            for row in results:
                print(f"- {row[0]}")
        else:
            print("All countries and continents:")
            for row in results:
                print(f"{row[0]} ({row[1]})")
    else:
        print("No countries found.")

    cursor.close()

connection.close()
print("Connection closed.")

#Introduction to the game


#User inputs name
#Rules of the game


#Main game

#List of countries to choose from (get the list of countries from database)


#To move to another country solve a puzzle


#If the cow loses all three lives or if the timer runs out =  the farmer catches the cow.


#Ending

#If the cow wins the game prints out “ Farmer in jail “
#If the cow loses the farmer says something like “Dinner time”