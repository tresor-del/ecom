# Projet E-Commerce Full-Stack

Ce projet est une application web full-stack avec un backend Django Rest Framework (DRF) et un frontend React avec Vite. Le backend gère la base de données et expose des APIs REST, tandis que le frontend est une application React moderne, rapide et légère.

## Structure du projet

Le projet est divisé en deux parties principales :

1: **Backend** : Utilise Django Rest Framework (DRF) pour gérer la base de données et exposer des APIs.
2: **Frontend**: Une application React, construite avec Vite, qui consomme les APIs du backend.

### Prérequis

**Backend**
* Python 3.x
* Django
* Django Rest Framework (DRF)
* PostgreSQL (ou autre base de données, selon ta configuration)

**Frontend**
* Node.js (version 16 ou supérieure)
* npm ou yarn

**Installation**
1. **Backend**
   a. **Cloner le dépôt**  
      Clone ce dépôt dans ton répertoire local :
      
      ```bash
      git clone https://github.com/ton-utilisateur/mon-projet.git
      cd mon-projet/backend
      ```

   b. **Créer un environnement virtuel**  
      Crée un environnement virtuel et l'active :
      
      ```bash
      python3 -m venv env
      source env/bin/activate  # Sur macOS/Linux
      env\Scripts\activate  # Sur Windows
      ```

   c. **Installer les dépendances**  
      Installe les dépendances nécessaires :
      
      ```bash
      pip install -r requirements.txt
      ```

   d. **Lancer le serveur**  
      Applique les migrations et lance le serveur :
      
      ```bash
      python manage.py migrate
      python manage.py runserver
      ```

2. **Frontend**
   a. **Aller dans le dossier frontend**  
      Va dans le dossier `frontend` :
      
      ```bash
      cd ../frontend
      ```

   b. **Installer les dépendances**  
      Installe les dépendances du frontend avec npm ou yarn :
      
      ```bash
      npm install
      ```

   c. **Démarrer le serveur de développement**  
      Lance le serveur de développement Vite :
      
      ```bash
      npm run dev
      ```


Ton application frontend sera maintenant accessible à l'adresse http://localhost:3000.

**API**
L'API backend expose des points d'accès REST pour interagir avec les données. Voici quelques exemples :

* GET /api/products/ – Récupérer une liste d'articles.
* POST /api/products/ – Créer un nouvel article.
* GET /api/products/{id}/ – Récupérer un article spécifique par son ID.
Consulte la documentation de l'API pour plus de détails sur les points d'accès disponibles.

**Contribuer**
Si tu souhaites contribuer à ce projet, merci de suivre ces étapes :

* Fork le projet.
* Crée une branche pour ta fonctionnalité (git checkout -b feature/nouvelle-fonctionnalité).
* Fais tes modifications et commits.
* Pousse ta branche sur ton fork.
* Ouvre une pull request pour proposer tes changements.

**Licence**

Ce projet est sous licence MIT. Consulte le fichier LICENSE pour plus de détails.
