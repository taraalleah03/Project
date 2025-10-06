#import all necessary modules/libraries
import mariadb
import time
import random
connection = mariadb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'taRamart!n2003thirty', #use own password here
    database = 'flight_game',
    autocommit = True)
#visual intro

final_art = r'''
          .=     ,        =.                    __    __  __ __    ___  ____     ___ __  _____     ___ ___  __ __         __   ___   __    __  _____  __                          
  _  _   /'/    )\,/,/(_   \ \                 |  |__|  ||  |  |  /  _]|    \   /  _]  |/ ___/    |   |   ||  |  |       /  ] /   \ |  |__|  |/     ||  |                 _.-^-._    .--.
   `//-.|  (  ,\\)\//\)\/_  ) |                |  |  |  ||  |  | /  [_ |  D  ) /  [_|_ (   \_     | _   _ ||  |  |      /  / |     ||  |  |  ||  Y  ||  |              .-'   _   '-. |__|
   //___\   `\\\/\\/\/\\///'  /                |  |  |  ||  _  ||    _]|    / |    _] \|\__  |    |  \_/  ||  ~  |     /  /  |  O  ||  |  |  ||__|  ||__|             /     |_|     \|  |
,-"~`-._ `"--'_   `"""`  _ \`'"~-,_            |  `  '  ||  |  ||   [_ |    \ |   [_    /  \ |    |   |   ||___, |    /   \_ |     ||  `  '  |   |__| __             /               \  |
\       `-.  '_`.      .'_` \ ,-"~`/            \      / |  |  ||     ||  .  \|     |   \    |    |   |   ||     |    \     ||     | \      /     __ |  |           /|     _____     |\ |
 `.__.-'`/   (-\        /-) |-.__,'              \_/\_/  |__|__||_____||__|\_||_____|    \___|    |___|___||____/      \____| \___/   \_/\_/     |__||__|            |    |==|==|    |  |
   ||   |     \O)  /^\ (O/  |                                                                                                                                        |    |--|--|    |  |
   `\\  |         /   `\    /                                                                                                                                        |    |==|==|    |  |
     \\  \       /      `\ /          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      `\\ `-.  /' .---.--.\
        `\\/`~(, '()      ('
         /(O) \\   _,.-.,_)
        //  \\ `\'`      /
      / |  ||   `""""~"` 
     /'  |__||
           `o
'''

farmerinjail = r'''

  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\
   / ||--_||_____||_--|| \
  (_(||)-| S123-45 |-(||)_)
|"""""""""""""""""""""""""""|
|"Honestly officer,I always |
|   feed my cows the best   |
|   grass! I'm innocent!!"  |
 """""""""""""""""""""""""""
'''

#color codes ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
NORMAL = "\033[0m"

print(f"{GREEN}{final_art}{NORMAL}")

#Introduction to the game
def show_introduction():
    introduction = f"""
    {YELLOW}This game is about a cow who was unsatisfied 
    by the quality of grass her farmer was feeding her.
    In order to satisfy her cravings the cow escapes 
    the barn in hopes of finding better quality grass.
    The cow needs to travel via airplane 
    to different countries and to solve different puzzles 
    to find the absolute best grass.
    {NORMAL}"""
    return print(introduction)
show_introduction()

#User inputs name
name = input("Enter your name: ")
print(f"\n{YELLOW}Welcome to the game, {name}!{NORMAL}")

#Rules of the game
def show_rules():
    rules = f"""{YELLOW}
    Here are the rules:
    1. You have a 90 second timer and if you fail to complete the round in the time given you lose.
    2. You have three (3) lives.
    3. If you get a question wrong, you will lose a life.
    4. Whenever you get a question wrong, you will get a hint.
    5. You will get to select each country you travel to.
    6. If you get to a country with the best grass, you win!
    {NORMAL}"""
    return print(rules)
show_rules()
    

#Main game

#function to get countries
def get_random_countries(connection, limit):
    cursor = connection.cursor()
    sql = "SELECT c.name, a.continent, MAX(a.municipality) FROM country c JOIN airport a ON c.iso_country = a.iso_country WHERE a.municipality IS NOT NULL GROUP BY c.name, a.continent ORDER BY RAND() LIMIT ?"
    cursor.execute(sql, (limit,))
    results = cursor.fetchall()
    cursor.close()

    #input into country dictionary
    countries = {}
    for name, continent, city in results:
        countries[name] = {"continent": continent, "city": city}
    return countries

countries = get_random_countries(connection,limit = 10)

#to print choices
print("Here is the list of countries to choose from")
for c in countries:
    print(f"-{BLUE}",c,f"{NORMAL}")
print("\n")

# randomly picks one country to be the “best grass”
# dictionary → dict_items → list → tuple → unpack into variables
best_country, details = random.choice(list(countries.items()))

#to store hints
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

#To move to another country solve a puzzle
puzzles = {
    "What is 25 x 11? ": "171",
    "What color do you get by mixing red and blue? ": "purple",
    "What is the capital of France? ": "paris",
    "How many legs does a cow have? ": "4",
    "What is 10 - 3? ": "7",
    "What is 'Thank you' in Finnish ": "kiitos",
    "Is Cleopatra from India? ": "no",
    "What language do Japanese people speak ": "japanese"
}
### game rules and timer
lives = 3
time_limit = 90
start_time = time.time()
question_count = 0

while lives > 0:
### Timer
    elapsed = time.time() - start_time
    remaining_time = int(time_limit - elapsed)

### if the timer runs out = farmer catches the cow = lose
    if remaining_time <= 0:
        print(f"\n{RED}Time’s up! The farmer catches the cow. Dinner time!{NORMAL}")
        break

    question_count += 1
    if question_count % 3 == 0:
        print(f"\n{YELLOW}Announcement: {remaining_time} seconds left! Hurry up!{NORMAL}")

### Puzzle solving
    puzzle, answer = random.choice(list(puzzles.items()))
    user_answer = input(f"\nPuzzle: {puzzle} \n").lower().strip()

    if user_answer == answer:
        print(f"{GREEN}Correct! You can travel to another country.{NORMAL}\n")
        next_country= input("Which country do you want to go to? ").strip()
        print(f"The cow travels to {next_country}\n")
        if next_country.lower() == best_country.lower(): #if the user guess the right country
            print(f"{GREEN}The cow found the best grass in {best_country}!{NORMAL}")
            print(f"{GREEN}Farmer in jail! You win!\n",farmerinjail,f"{NORMAL}")
            break
        else:
            print(f"{RED}Wrong! The grass is somewhere else. Solve the puzzle to move to another country.{NORMAL}")
            hint = random.choice(hints)
            print(f"{BLUE}Hint: the country's city/continent is {hint}{NORMAL}")
    else: #if thr answer is wrong, lose 1 live and the system gives a hint
        lives -= 1
        print(f"{RED}Wrong! You lose a life.Lives left: {lives}{NORMAL}")
        hint = random.choice(hints)
        print(f"{BLUE}Hint: the country's city/continent is {hint}{NORMAL}")
        #if lives > 0:
        #    next_country = input("Choose another country to try: ").strip()
        #    print(f"The cow travels to {next_country}")

#If the cow loses all three lives =  the farmer catches the cow.
if lives == 0:
    print(f"\n{RED}You have no lives left. The farmer catches the cow!!! Dinner time!{NORMAL}")




#Ending

#If the cow wins the game prints out “ Farmer in jail “
"""if "?" == "?":
    print("The has been captured")"""

#If the cow loses the farmer says something like “Dinner time”
"""elif "!" k== "!":"""
#message = random.randint(1, 3)

#    if message == 1:
#        print("FARMER: IT'S DINNER TIME!")
#    elif message == 2:
#        print("FARMER: WE'RE HAVING GOOD STEAK TONIGHT!")
#    elif message == 3:
#        print("DINNER IS SERVED")
