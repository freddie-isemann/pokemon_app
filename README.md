# Pokemon Randomizer 

A simple web application designed by Freddie Isemann that fetches data about a random Pokemon with each button press or page reload and displays it using the PokeAPI.

---

## Features

- Fetches a random Pokemon's name, sprite, height and weight each time you press a button or reload the page
- Responsive and styled with Bootstrap and Custom CSS

---

## Windows Installation

1. Clone the repo
    ''' bash
    git clone https://github.com/freddie-isemann/pokemon_app.git
    cd pokemon_app

2. Create a virtual environment (optional)
    ''' bash
    python -m venv .venv
    .venv\Scripts\activate

3. Install dependencies
    ''' bash
    pip install requirements.txt

4. Run the app
    ''' bash
    flask run

    Or

    flask --app main.py run

5. Open the browser and go to:
    http://127.0.0.1:5000

---

## Usage

- Click the button on the homepage to retrieve the data of a random Pokemon.
- Press the same button on the following page to retrieve the data of another random Pokemon.
- Reload the page for the same effect.

## Technologies Used
- Python
- Flask
- Bootstrap 5
- PokeAPI