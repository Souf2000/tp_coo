from django.contrib import admin
from .models import Objet, Ville, Usine, Machine, Stock, Ressource, Recette, RecetteIngredient, Etape, Produit

admin.site.register(Objet)
admin.site.register(Ville)
admin.site.register(Usine)
admin.site.register(Machine)
admin.site.register(Stock)
admin.site.register(Ressource)
admin.site.register(Recette)
admin.site.register(RecetteIngredient)
admin.site.register(Etape)
admin.site.register(Produit)

