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
question_count = 0

print("The cow needs to solve puzzles to travel to another country!")
print("You have 3 lives and 90 seconds. Wrong answer = lose 1 life.")

while lives > 0:
### Timer
    elapsed = time.time() - start_time
    remaining_time = int(time_limit - elapsed)

### if the timer runs out = farmer catches the cow = lose
    if remaining_time <= 0:
        print("\nTime’s up! The farmer catches the cow. Dinner time!")
        break

    question_count += 1
    if question_count % 3 == 0:
        print(f"\n Announcement: {remaining_time} seconds left! Hurry up!")

### Puzzle solving
    puzzle, answer = random.choice(list(puzzles.items()))
    user_answer = input(f"\n Puzzle: {puzzle} ").lower().strip()

    if user_answer == answer:
        print("Correct! You can travel to another country.")
        country: input("Which country do you want to go to? ").strip()
        print(f"The cow travels to {country}")
        if country == best_country: #if the user guess the right country
            print(f"The cow found the best grass in {best_country}!")
            print("Farmer in jail! You win!")
            break
    else: #if thr answer is wrong, lose 1 live and the system gives a hint
        lives -= 1
        print(f"Wrong! You lose a life.Lives left: {lives}")
        hint = random.choice(hints[best_country])
        print(f" Here is a hint your you: {hint}")
        if lives > 0:
            next_country = input("Choose another country to try: ").strip()
            print(f"The cow travels to {next_country}")

#If the cow loses all three lives =  the farmer catches the cow.
if lives == 0:
    print("\n You have no lives left. The farmer catches the cow!!! Dinner time!")




#Ending

#If the cow wins the game prints out “ Farmer in jail “
"""if "?" == "?":
    print("The has been captured")"""

#If the cow loses the farmer says something like “Dinner time”
"""elif "!" k== "!":"""
    message = random.randint(1, 3)

    if message == 1:
        print("FARMER: IT'S DINNER TIME!")
    elif message == 2:
        print("FARMER: WE'RE HAVING GOOD STEAK TONIGHT!")
    elif message == 3:
        print("DINNER IS SERVED")
