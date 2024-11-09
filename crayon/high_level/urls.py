from django.urls import path
from . import views

urlpatterns = [
    path('villes/', views.ville_list, name='ville-list'),
    path('machines/', views.machine_list, name='machine-list'),
    path('usines/', views.usine_list, name='usine-list'),
    path('ressources/', views.ressource_list, name='ressource-list'),
    path('stocks/', views.stock_list, name='stock-list'),
    path('quantite_ressources/', views.quantiteressource_list, name='quantiteressource-list'),
    path('etapes/', views.etape_list, name='etape-list'),
    path('produits/', views.produit_list, name='produit-list'),
    path('recettes/', views.recette_list, name='recette-list'),
]

