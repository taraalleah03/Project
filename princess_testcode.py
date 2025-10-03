# Introduction to the game

#Introduction to the game
def show_introduction():
    introduction = """
    This game is about a cow who was unsatisfied 
    by the quality of grass her farmer was feeding her.
    In order to satisfy her cravings the cow escapes 
    the barn in hopes of finding better quality grass.
    The cow needs to travel via airplane 
    to different countries and to solve different puzzles 
    to find the absolute best grass.
    """
    return print(introduction)
show_introduction()
# User inputs name
#User inputs name
name = input("Enter your name: ")
print(f"Welcome to the game, {name}!")

# Rules of the game
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

import mariadb
import time
import random
connection = mariadb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'princess',
    database = 'flight_game',
    autocommit = True

i