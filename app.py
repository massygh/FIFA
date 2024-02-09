# app.py

from flask import Flask, render_template

app = Flask(__name__)

# Exemple de structure de données pour les joueurs
joueurs = [
    {"id": 1, "nom": "Messi", "equipe": "Miami FC", "stats": {"attaque": 90, "defense": 70, "physique": 85}},
    {"id": 2, "nom": "Ronaldo", "equipe": "Al Nassr", "stats": {"attaque": 92, "defense": 65, "physique": 88}},
    {"id": 3, "nom": "Wail", "equipe": "Paris Saint-Germain", "stats": {"attaque": 85, "defense": 75, "physique": 80}},
    # Ajoutez d'autres joueurs avec leurs statistiques
]

@app.route('/')
def accueil():
    return render_template('accueil.html', joueurs=joueurs)

if __name__ == '__main__':
    random_port = random.randint(5000, 9999)
    app.run(debug=True, port=random_port)
