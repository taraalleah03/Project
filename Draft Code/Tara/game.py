# import all necessary modules/libraries
import mariadb
import time
import random

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='taRamart!n2003thirty',  # use own password here
    database='flight_game',
    autocommit=True)

# Main game
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
NORMAL = "\033[0m"

# function to get countries
def get_random_countries(connection, limit):
    cursor = connection.cursor()
    sql = "SELECT c.name, a.continent, MAX(a.municipality) FROM country c JOIN airport a ON c.iso_country = a.iso_country WHERE a.municipality IS NOT NULL GROUP BY c.name, a.continent ORDER BY RAND() LIMIT ?"
    cursor.execute(sql, (limit,))
    results = cursor.fetchall()
    cursor.close()

    # input into country dictionary
    countries = {}
    for name, continent, city in results:
        countries[name] = {"continent": continent, "city": city}
    return countries


countries = get_random_countries(connection, limit=10)

# to print choices
print("Here is the list of countries to choose from")
for c in countries:
    print(f"-{BLUE}", c, f"{NORMAL}")
print("\n")

# randomly picks one country to be the “best grass”
# dictionary → dict_items → list → tuple → unpack into variables
best_country, details = random.choice(list(countries.items()))

# to store hints
continent_hint = countries[best_country]["continent"]
city_hint = countries[best_country]["city"]

hints = [continent_hint, city_hint]
hint = random.choice(hints)

print("The cow is looking for the best grass...")

guess = input("Which country do you think it is? ").strip()

if guess.lower() == best_country.lower():
    print(f"{GREEN}The cow found the best grass in {best_country}!{NORMAL}")
    print(f"{GREEN}Farmer in jail! You win!\n", farmerinjail, f"{NORMAL}")
else:
    random_letter = random.choice(list(best_country.replace(" ", "")))
    print(f"{RED}Wrong! The grass is somewhere else. Solve the puzzle to move to another country.{NORMAL} ")
    print(f"{BLUE}Hint: The country's name has the letter '{random_letter.upper()}'{NORMAL}.")

