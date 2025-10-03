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
def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Time's up, the farmer got you!")
    countdown_timer(90)




#Introduction to the game
def show_introduction():
    introduction = """
    Welcome to the game!
    In this game a cow escapes 
    her farmers barn due to her unsatisfaction by the quality of grass. 
    She leaves the barn in hopes of finding the best grass. 
    In order to find the best grass she will need to 
    fly to different countries via airplane and to solve various puzzles 
    to find the absolute best grass.
"""
    print(introduction)
    show_introduction()

#User inputs name

name = input("Enter your name: ")
print(f"Welcome, {name}!")
#Rules of the game

def show_rules():
    rules = """
    Here are the rules:
    1. You have a 90 second timer and
    if you fail to complete the round in the time given you lose.
    2. You have three (3) lives.
    3. If you get a question wrong, you will lose a life.
    4. Whenever you get a question wrong, you will get a hint.
    5. You will get to select each country you travel to.
    6. If you get to a country with the best grass, you win!
    """
    print(rules)
    show_rules()



#Main game

#List of countries to choose from (get the list of countries from database)


#To move to another country solve a puzzle


#If the cow loses all three lives or if the timer runs out =  the farmer catches the cow.


#Ending

#If the cow wins the game prints out “ Farmer in jail “
if "?" == "?":
    print("The has been captured")

#If the cow loses the farmer says something like “Dinner time”
elif "!" == "!":

    print("FARMER: IT'S DINNER TIME!")