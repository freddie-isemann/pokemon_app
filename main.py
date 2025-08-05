# DO NOT FORGET TO ACTIVATE THE VIRTUAL ENVIRONMENT HERE
# Import necessary libraries and FLask so we can create instances of the Flask class (apps)
import requests
import json
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/pokemon.html', methods=['GET', 'POST'])
def random_pokemon():
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=200')
    if response.status_code == 200:
        data = response.json()
        items = data['results']
        select = random.choice(items)
        new_url = select['url']
        new_response = requests.get(new_url)
        if new_response.status_code == 200:
            new_data = new_response.json()
            name = new_data["name"]
            weight = new_data["weight"]
            height = new_data["height"]
            sprite = new_data["sprites"]["front_default"]
            return render_template("pokemon.html", name=name, weight=weight / 10, height=height / 10, sprite=sprite)
        else:
            return "Failed to get specific Pokemon data"            
    else:
        return "Failed to get Pokemon data"
    
# To run from the terminal, copy and paste 'flask --app main.py run' into the terminal
# To activate the virtual environment paste ""C:/Users/scram/OneDrive/Documents/VS Code Projects/Python/pokemon_app/.venv/Scripts/activate.bat" into the terminal
# OR use "cd pokemon_app" to cd into the correct folder first (VSCode loads into the 'Python' folder) and then use ".venv\Scripts\activate" to activate the virtual environment
