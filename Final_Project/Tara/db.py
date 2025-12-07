import random, mariadb
from flask import Flask, request , jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='taRamart!n2003thirty',  # use own password here
    database='flight_game',
    autocommit=True)

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

@app.route('/api/start')
def api_start():
    data = request.json
    guess = data.get("guess","").strip()
    answer = data.get("answer","").strip()

    if guess.lower() == answer.lower():
        return jsonify({
            "correct": True,
            "message": f"Yipee, {answer} is correct! You found the country with the best grass!"
        })

    letter = random.choice