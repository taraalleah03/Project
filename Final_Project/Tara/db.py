import random, mariadb
from flask import Flask, request , jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/start')
def api_start():
    #temporary list of countries
    countries = []