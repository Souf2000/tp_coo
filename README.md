# TP COO - Documentation LAHLALI Soufiane

Bienvenue dans le projet **TP COO** réalisé par **Soufiane LAHLALI** dans le cadre des cours à l'Université Toulouse III - Paul Sabatier.

**Auteur** : Soufiane LAHLALI  
**Email** : [soufiane.lahali@univ-tlse3.fr](mailto:soufiane.lahali@univ-tlse3.fr)  
**Licence** : Licence `tp_coo`  
**URL de documentation** : [Documentation locale](http://localhost:8000/docs/)  

**URL des classes** :

- [Villes](http://localhost:8000/api/villes/) ([JSON](http://localhost:8000/api/villes/?format=json))
- [Machines](http://localhost:8000/api/machines/) ([JSON](http://localhost:8000/api/machines/?format=json))
- [Usines](http://localhost:8000/api/usines/) ([JSON](http://localhost:8000/api/usines/?format=json))
- [Ressources](http://localhost:8000/api/ressources/) ([JSON](http://localhost:8000/api/ressources/?format=json))
- [Stocks](http://localhost:8000/api/stocks/) ([JSON](http://localhost:8000/api/stocks/?format=json))
- [Quantités de Ressources](http://localhost:8000/api/quantites_ressources/) ([JSON](http://localhost:8000/api/quantites_ressources/?format=json))
- [Etapes](http://localhost:8000/api/etapes/) ([JSON](http://localhost:8000/api/etapes/?format=json))
- [Produits](http://localhost:8000/api/produits/) ([JSON](http://localhost:8000/api/produits/?format=json))
- [Recettes](http://localhost:8000/api/recettes/) ([JSON](http://localhost:8000/api/recettes/?format=json))

---

## Description du projet

Ce projet est une implémentation des concepts étudiés dans le cadre du module de programmation orientée objet et systèmes distribués.

Le projet est divisé en plusieurs parties :

1. **low_level** : Implémentation en C++ pour la gestion d'objets, de villes, de locaux et de sièges sociaux. Cette partie utilise des bibliothèques comme CPR pour effectuer des requêtes HTTP.
2. **crayon** : Application web basée sur Django pour l'affichage et la gestion d'objets et de données via une API REST. Elle intègre une documentation Swagger pour faciliter l'interaction avec l'API.

---

## Contenu du projet

- **low_level/** : Contient les fichiers pour la partie C++.
  - `main.cpp`, `Ville.cpp`, `Objet.cpp`, `Local.cpp`, `SiegeSocial.cpp`
  - `Makefile` pour compiler le projet
  - Dépendances : CPR, nlohmann/json

- **crayon/** : Application Django.
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
2. Installez les bibliothèques nécessaires (CPR et nlohmann/json).
3. Compilez le projet :
   ```bash
   make
   ```
4. Exécutez le binaire généré :
   ```bash
   ./main
   ```

### Partie Django
1. Accédez au répertoire de l'application Django :
   ```bash
   cd tp_coo/crayon
   ```
2. Activez l'environnement virtuel :
   ```bash
   source ../venv/bin/activate
   ```
3. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```
4. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```
5. Accédez à l'application via votre navigateur : [http://localhost:8000](http://localhost:8000)

---

## Fonctionnalités principales

1. Gestion des entités (villes, machines, usines, etc.) via une interface utilisateur et une API REST.
2. Documentation automatique des endpoints via Swagger et ReDoc.
3. Exemples d'implémentation en C++ avec des interactions HTTP.

---

## Auteur

Soufiane LAHLALI  
[soufiane.lahali@univ-tlse3.fr](mailto:soufiane.lahali@univ-tlse3.fr)

---

*Ce projet est réalisé dans le cadre de la formation en programmation orientée objet à l'Université Toulouse III - Paul Sabatier.*
