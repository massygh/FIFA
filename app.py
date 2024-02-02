# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Exemple de structure de données pour les joueurs
joueurs = [
    {"id": 1, "nom": "Messi", "equipe": "Barcelone"},
    {"id": 2, "nom": "Ronaldo", "equipe": "Juventus"},
    # Ajoutez d'autres joueurs
]

# Exemple de structure de données pour les équipes
equipes = [
    {"id": 1, "nom": "Barcelone"},
    {"id": 2, "nom": "Juventus"},
    # Ajoutez d'autres équipes
]

@app.route('/')
def accueil():
    return render_template('accueil.html', joueurs=joueurs, equipes=equipes)