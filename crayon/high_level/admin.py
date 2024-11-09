from django.contrib import admin
from .models import Ville, Machine, Usine, Ressource, Stock, QuantiteRessource, Etape, Produit, Recette, RecetteIngredient

# Enregistrement de tous les modèles dans l'interface d'administration
admin.site.register(Ville)
admin.site.register(Machine)
admin.site.register(Usine)
admin.site.register(Ressource)
admin.site.register(Stock)
admin.site.register(QuantiteRessource)  
admin.site.register(Etape)
admin.site.register(Produit)
admin.site.register(Recette)
admin.site.register(RecetteIngredient)

