from django.urls import path
from . import views

urlpatterns = [
    path('villes/', views.ville_list, name='ville-list'),
    path('villes/<int:id>/', views.ville_detail, name='ville-detail'),
    path('ressources/', views.ressource_list, name='ressource-list'),
    path('ressources/<int:id>/', views.ressource_detail, name='ressource-detail'),
    path('machines/', views.machine_list, name='machine-list'),
    path('machines/<int:id>/', views.machine_detail, name='machine-detail'),
    path('usines/', views.usine_list, name='usine-list'),
    path('usines/<int:id>/', views.usine_detail, name='usine-detail'),
    path('stocks/', views.stock_list, name='stock-list'),
    path('stocks/<int:id>/', views.stock_detail, name='stock-detail'),
    path('quantite-ressources/', views.quantite_ressource_list, name='quantite-ressource-list'),
    path('quantite-ressources/<int:id>/', views.quantite_ressource_detail, name='quantite-ressource-detail'),
    path('etapes/', views.etape_list, name='etape-list'),
    path('etapes/<int:id>/', views.etape_detail, name='etape-detail'),
    path('produits/', views.produit_list, name='produit-list'),
    path('produits/<int:id>/', views.produit_detail, name='produit-detail'),
    path('recettes/', views.recette_list, name='recette-list'),
    path('recettes/<int:id>/', views.recette_detail, name='recette-detail'),
]

