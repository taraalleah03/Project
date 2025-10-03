import mariadb #for this to work need to import mariadb
import random

connection = mariadb.connect(
host ='127.0.0.1',
port = 3306,
user = 'root',
password = 'taRamart!n2003thirty',
database = 'flight_game',
autocommit = True
)

#print("Connected to MariaDB!")

countries = {}

# Function to get countries
def get_random_countries(connection, limit=11):
    cursor = connection.cursor()
    sql = "SELECT c.name, a.continent, a.municipality FROM country c JOIN airport a ON c.iso_country = a.iso_country WHERE a.municipality IS NOT NULL ORDER BY RAND() LIMIT ?"
    cursor.execute(sql, (limit,))
    results = cursor.fetchall()
    cursor.close()

    #input into country dictionary
    countries = {}
    for name, continent, city in results:
        countries[name] = {"continent": continent, "city": city}
    return countries

countries = get_random_countries(connection, 11)
print(countries)

countries = get_random_countries(connection, 11)

# pick one country to be the “best grass”
best_country, details = random.choice(list(countries.items()))

print("The cow is looking for the best grass...")
print(f"Hint: The country is in continent {details['continent']}")

guess = input("Which country do you think it is? ").strip()

if guess.lower() == best_country.lower():
    print("Correct! You found the best grass!")
else:
    print(f"Wrong! The cow was in {best_country}, near {details['city']}.")

puzzle, answer = random.choice(list(puzzles.items()))
user_answer = input(f"Puzzle: {puzzle} ").lower().strip()