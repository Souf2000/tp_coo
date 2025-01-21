# TP COO - Documentation LAHLALI Soufiane

Bienvenue dans le projet **TP COO** réalisé par **Soufiane LAHLALI** dans le cadre des cours à l'Université Toulouse III - Paul Sabatier.

**Auteur** : Soufiane LAHLALI  
**Email** : [soufiane.lahali@univ-tlse3.fr](mailto:soufiane.lahali@univ-tlse3.fr)  
**Licence** : Licence `tp_coo`  
**URL de documentation** : [Documentation locale](http://localhost:8000/docs/)  
**URL des classes** :

- [Villes](http://localhost:8000/api/villes/)
- [Machines](http://localhost:8000/api/machines/)
- [Usines](http://localhost:8000/api/usines/)
- [Ressources](http://localhost:8000/api/ressources/)
- [Stocks](http://localhost:8000/api/stocks/)
- [Quantités de Ressources](http://localhost:8000/api/quantites_ressources/)
- [Étapes](http://localhost:8000/api/etapes/)
- [Produits](http://localhost:8000/api/produits/)
- [Recettes](http://localhost:8000/api/recettes/)

---

## Description du projet

Ce projet est une implémentation des concepts étudiés dans le cadre du module de programmation orientée objet et systèmes distribués.

Le projet est divisé en plusieurs parties :

1. **low_level** : Implémentation en C++ pour la gestion d'objets, de villes, de locaux et de sièges sociaux. Cette partie utilise des bibliothèques comme CPR pour effectuer des requêtes HTTP.
2. **crayon** : Application web basée sur Django pour l'affichage et la gestion d'objets et de données via une API REST. Elle intègre une documentation Swagger pour faciliter l'interaction avec l'API.

---

## Contenu du projet

### Partie C++
- **low_level/**
  - `main.cpp`, `Ville.cpp`, `Objet.cpp`, `Local.cpp`, `SiegeSocial.cpp`
  - `Makefile` pour compiler le projet
  - Dépendances : CPR, nlohmann/json

### Partie Django
- **crayon/**
  - `manage.py` : Gestion de l'application
  - `high_level/` : Code source pour les modèles, vues et serializers
  - `urls.py` : Configuration des routes

---

## Prérequis

### Partie C++
- **Compilateur** : `g++` avec support de C++17
- **Bibliothèques** :
  - [CPR](https://github.com/libcpr/cpr)
  - [nlohmann/json](https://github.com/nlohmann/json)

### Partie Django
- **Python 3.12+**
- **Virtualenv** pour gérer les dépendances Python
- **Modules Python** :
  - `Django`, `djangorestframework`, `drf-yasg`

---

## Installation

### Partie C++

1. Clonez le projet :
   ```bash
   git clone https://github.com/Souf2000/tp_coo.git
   cd tp_coo/low_level
   ```

2. Installez les dépendances nécessaires :
   ```bash
   sudo apt update
   sudo apt install g++ cmake libcurl4-openssl-dev
   git clone https://github.com/libcpr/cpr.git
   cd cpr && mkdir build && cd build
   cmake ..
   make
   sudo make install
   ```

3. Compilez le projet :
   ```bash
   cd ~/téléchargements/tp_coo/low_level
   make
   ```

4. Exécutez le programme :
   ```bash
   ./main
   ```

### Partie Django

1. Naviguez dans le dossier de l'application Django :
   ```bash
   cd tp_coo/crayon
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Appliquez les migrations :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

---

## Fonctionnalités

- Gestion des entités : villes, objets, locaux, sièges sociaux, etc.
- API REST pour interagir avec les données.
- Documentation interactive avec Swagger et ReDoc.

---

## Auteur

**Soufiane LAHLALI**  
**Email** : [soufiane.lahali@univ-tlse3.fr](mailto:soufiane.lahali@univ-tlse3.fr)
