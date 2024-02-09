# app.py
import random
from flask import Flask, render_template

app = Flask(__name__)

# Exemple de structure de données pour les joueurs
joueurs = [
    {"id": 1, "nom": "Messi", "equipe": "Miami FC"},
    {"id": 2, "nom": "Ronaldo", "equipe": "Al Nassr"},
    {"id": 3, "nom": "Wail", "equipe": "Paris Saint-Germain"},
    # Ajoutez d'autres joueurs
]

# Exemple de structure de données pour les équipes
equipes = [
    {"id": 1, "nom": "Miami FC"},
    {"id": 2, "nom": "Al Nassr"},
    {"id": 3, "nom": "Paris Saint-Germain"},
    # Ajoutez d'autres équipes
]

@app.route('/')
def accueil():
    return render_template('accueil.html', joueurs=joueurs, equipes=equipes)

@app.route('/page-inaccessible')
def page_inaccessible():
    message = "Cette page est inaccessible pour le moment."
    return render_template('page_inaccessible.html', message=message)

if __name__ == '__main__':
    random_port = random.randint(5000, 9999)
    app.run(debug=True, port=random_port)
