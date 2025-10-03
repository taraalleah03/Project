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

#Connect to database


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