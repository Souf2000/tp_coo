# TP COO - Documentation LAHLALI Soufiane

Bienvenue dans le projet **TP COO** réalisé par **Soufiane LAHLALI** dans le cadre du Master 2 ISTR à l'Université Toulouse III - Paul Sabatier.

## Informations Générales

- **Auteur** : Soufiane LAHLALI
- **Email** : [soufiane.lahali@univ-tlse3.fr](mailto:soufiane.lahali@univ-tlse3.fr)
- **Licence** : Licence `tp_coo`
- **Documentation locale** : [Accéder à la documentation](http://localhost:8000/docs/)

---

## Table des Matières

1. [Description du Projet]
2. [Structure du Projet]
3. [Prérequis]
4. [Installation]
5. [Utilisation]
6. [URL des Classes]
7. [Détails Techniques]

---

## Description du Projet

Ce projet est une implémentation des concepts de programmation orientée objet (POO) et de systèmes distribués. Il est divisé en deux parties :

1. **low_level** : Une application C++ qui gère des entités telles que les objets, villes, locaux et sièges sociaux. Cette partie inclut des appels HTTP via la bibliothèque CPR et des manipulations JSON via nlohmann/json.

2. **crayon** : Une application web basée sur Django qui propose une API REST pour la gestion des entités et intègre une documentation Swagger pour faciliter les tests.

---

## Structure du Projet

Voici la structure principale du projet :

├── low_level/         # Code source C++
│   ├── main.cpp       # Point d'entrée du programme
│   ├── Ville.cpp      # Classe Ville
│   ├── Objet.cpp      # Classe Objet
│   ├── Local.cpp      # Classe Local
│   ├── SiegeSocial.cpp # Classe SiegeSocial
│   └── Makefile       # Fichier pour compiler le projet
├── crayon/            # Application Django
│   ├── manage.py      # Gestionnaire de commandes Django
│   ├── high_level/    # Contient les modèles, vues et serializers
│   └── urls.py        # Routes de l’application
├── README.md          # Documentation du projet



## Prérequis

### Partie C++

- **Compilateur** : `g++` avec support pour C++17
- **Bibliothèques externes** :
  - [CPR](https://github.com/libcpr/cpr) : Pour les requêtes HTTP
  - [nlohmann/json](https://github.com/nlohmann/json) : Pour la manipulation JSON

### Partie Django

- **Python** : Version 3.12+
- **Outils** :
  - Virtualenv : Gestionnaire d’environnement virtuel
  - Modules Python requis :
    - `Django`
    - `djangorestframework`
    - `drf-yasg`

---

## Installation

### Partie C++

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Souf2000/tp_coo.git
   cd tp_coo/low_level
   ```
2. Installez les dépendances requises (CPR, nlohmann/json).
   ```bash
   sudo apt-get install libcurl4-openssl-dev
   git clone https://github.com/libcpr/cpr.git
   cd cpr
   mkdir build && cd build
   cmake ..
   make
   sudo make install
   ```
3. Compilez le projet :
   ```bash
   make
   ```
4. Exécutez le programme :
   ```bash
   ./main
   ```

### Partie Django

1. Créez un environnement virtuel :
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```
3. Appliquez les migrations :
   ```bash
   python manage.py migrate
   ```
4. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

---

## Utilisation

- **Partie C++** : Le programme affiche les détails des entités et exécute des requêtes HTTP.
- **Partie Django** : Naviguez vers `http://localhost:8000` pour accéder à l’API et à la documentation Swagger.

---

## URL des Classes

Voici les URL disponibles pour les entités de l’API Django :

- [Villes]
    (http://localhost:8000/api/villes/)
    (http://localhost:8000/api/villes/?format=json)
- [Machines]
    (http://localhost:8000/api/machines/)
    (http://localhost:8000/api/machines/?format=json)
- [Usines]
    (http://localhost:8000/api/usines/)
    (http://localhost:8000/api/usines/?format=json)
- [Ressources]
    (http://localhost:8000/api/ressources/)
    (http://localhost:8000/api/ressources/?format=json)
- [Stocks]
    (http://localhost:8000/api/stocks/)
    (http://localhost:8000/api/villes/?format=json)
- [Quantités de Ressources]
    (http://localhost:8000/api/quantites_ressources/)
    (http://localhost:8000/api/quantites_ressources/?format=json)
- [Etapes]
    (http://localhost:8000/api/etapes/)
    (http://localhost:8000/api/etapes/?format=json)
- [Produits]
    (http://localhost:8000/api/produits/)
    (http://localhost:8000/api/produits/?format=json)
- [Recettes]
    (http://localhost:8000/api/recettes/)
    (http://localhost:8000/api/recettes/?format=json)

---

## Détails Techniques

### Partie C++
- Les entités gérées incluent les villes, objets, locaux et sièges sociaux.
- Chaque entité est définie dans une classe séparée avec des méthodes pour afficher leurs informations.

### Partie Django
- **Modèles** : Les modèles représentent les entités gérées dans la base de données.
- **API REST** : Permet de gérer les entités via des routes.
- **Documentation Swagger** : Disponible à `http://localhost:8000/docs/`.

---

## Contribution

Les contributions sont les bienvenues. N’hésitez pas à soumettre des issues ou des pull requests pour améliorer le projet.

---

## Contact

Pour toute question ou suggestion, contactez-moi à l’adresse suivante : [soufiane.lahali@univ-tlse3.fr](mailto:soufiane.lahali@univ-tlse3.fr).

