import mariadb
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

connection = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='bootsandcats',  # use own password here
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
    countries = get_random_countries(connection, 10)
    return jsonify({"countries": countries})

if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5000, debug=True)