#import all necessary modules/libraries
import mariadb
import time
import random
connection = mariadb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'princess',
    database = 'flight_game',
    autocommit = True)
print("Connected to Maria db!")

#Introduction to the game


#User inputs name
#Rules of the game


#Main game

#List of countries to choose from (get the list of countries from database)


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

print("The cow needs to solve puzzles to travel to another country!")
print("You have 3 lives and 90 seconds. Wrong answer = lose 1 life.")

while lives > 0:

    elapsed = time.time() - start_time
    if elapsed >= time_limit:
        print("\n Time’s up! The farmer catches the cow. Dinner time!️")
        break


    puzzle, answer = random.choice(list(puzzles.items()))
    user_answer = input(f"\n Puzzle: {puzzle} ").lower().strip()

    if user_answer == answer:
        print("Correct! You can travel to another country.")
        country: input("Which country do you want to go to? ").strip()
        print(f"The cow travels to {country}")
    else:
        lives -= 1
        print(f"Wrong! You lose a life.Lives left: {lives}")
        if lives > 0:
            next_country = input("Choose another country to try: ").strip()
            print(f"The cow travels to {next_country}")

if lives == 0:
    print("\n You have no lives left. The farmer catched the cow!!! Dinner time!")

#If the cow loses all three lives or if the timer runs out =  the farmer catches the cow.


#Ending

#If the cow wins the game prints out “ Farmer in jail “
"""if "?" == "?":
    print("The has been captured")"""

#If the cow loses the farmer says something like “Dinner time”
"""elif "!" == "!":"""
    message = random.randint(1, 3)

    if message == 1:
        print("FARMER: IT'S DINNER TIME!")
    elif message == 2:
        print("FARMER: WE'RE HAVING GOOD STEAK TONIGHT!")
    elif message == 3:
        print("DINNER IS SERVED")
