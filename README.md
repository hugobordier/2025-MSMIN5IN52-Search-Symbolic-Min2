# EPF Min2 - IA Exploratoire et Symbolique

Anaïs DEWEVER - Edwige LEBLANC - Marianne LEPERE

---

## Sujets détaillés pour le projet

### 9. Solveur de Wordle par CSP (et LLM)

**Description du problème et contexte**
Wordle est un jeu de mots dans lequel à chaque tentative de mot, on obtient des indications de lettres bien placées, mal placées ou absentes. Ces indices se traduisent par des contraintes sur le mot secret : certaines positions doivent contenir certaines lettres, d'autres non, etc. Un programme peut appliquer ces contraintes à un dictionnaire pour filtrer les mots possibles. Par exemple, une approche par contraintes définit des variables pour chaque lettre du mot secret et impose les retours (vert, jaune, gris) comme contraintes logiques sur ces variables.

**Références multiples**

- **Approche CSP** : [Beating Wordle: Constraint Programming](https://medium.com/better-programming/beating-wordle-constraint-programming-ef0b0b6897fe) - Utilisation d'un solver de contraintes sur un dataset de mots
- **Implémentation** : hakank.org - Implémentation d'un solveur Wordle en OR-Tools CP-SAT
- **Function calling** : [OpenAI Function calling documentation](https://platform.openai.com/docs/guides/function-calling) - Appel de fonctions pour déléguer des tâches (ex. solveur externe)
- **Intégration LLM** : On peut intégrer un LLM en function-calling pour qu'il exploite un solveur CSP sous-jacent et propose des coups optimisés

**Approches suggérées**

- Définir des variables pour chaque lettre du mot secret et imposer les contraintes de retour (vert/jaune/gris)
- Utiliser un solveur de contraintes pour réduire l'espace des solutions à chaque coup
- Intégrer un LLM via function calling pour déduire les contraintes linguistiques
- Développer une stratégie d'optimisation pour minimiser le nombre de tentatives

**Technologies pertinentes**

- Python avec python-constraint ou OR-Tools CP-SAT pour la résolution
- Dictionnaires de mots français/anglais pour les domaines de variables
- API OpenAI ou modèles locaux pour l'intégration LLM
- Interface web avec React/Vue pour une expérience interactive

---

# Wordle Solver Project

This project is a **Wordle Solver and Visualizer** with a FastAPI backend and a simple HTML/JS frontend.  
It allows you to:

- Play the **Daily Wordle**
- Play a **Random Wordle**
- See the solver automatically solve the word step by step with visual feedback

---

## 📂 Project Structure

project-root/
│
├─ Api_wordle/
│ ├─ main.py
│ ├─ utils.py
│
├─ Solveur_wordle/
│ └─ Solveur_Wordle.py
│
├─ frontend/
│ └─ index.html
│
├─ word_list.txt
├─ requirements.txt
├─ README.me
└─ launch.py # Script to start the project

## 🚀 Running the Project Locally

The project includes a single launch.py script that:

Starts the FastAPI backend (Api_wordle/main.py)

Opens the frontend in your default browser

Run:
python launch.py
at the root of the project.

This will:

- Install Python dependencies from requirements.txt.

- Start the FastAPI backend (default port 5000).

- Start the frontend HTTP server (default port 8080).

- Automatically open the frontend in your default browser at: http://127.0.0.1:8080/ (serves index.html by default).

##  🔧 Configuring Ports

At the top of launch.py you can change:

- API_PORT = 5000       # Port for FastAPI backend
- FRONTEND_PORT = 8080  # Port for frontend HTTP server

If a port is already used, change it here and restart the script.

## 🔹 Using the Frontend

Open the frontend if it didn’t open automatically: frontend/index.html

Click:

🟦 Daily Wordle – selects the word of the day

🟩 Random Wordle – generates a random word

▶ Solve – runs the solver and shows each step with colored feedback

---