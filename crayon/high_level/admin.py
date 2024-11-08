# admin.py
from django.contrib import admin
from .models import (
    Ville,
    Machine,
    Usine,
    Ressource,
    Stock,
    Recette,
    # SiegeSocial,  # Commenter ou supprimer cette ligne si SiegeSocial n'existe pas
)

# Enregistre tes modèles ici
admin.site.register(Ville)
admin.site.register(Machine)
admin.site.register(Usine)
admin.site.register(Ressource)
admin.site.register(Stock)
admin.site.register(Recette)
