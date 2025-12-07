from flask import Flask, render_template, request , jsonify
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("game.html")

@app.route('/api/start')
def api_start():
    #temporary list of countries
    countries = []