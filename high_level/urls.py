# high_level/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VilleViewSet, MachineViewSet, UsineViewSet, RessourceViewSet, StockViewSet, QuantiteRessourceViewSet, EtapeViewSet, ProduitViewSet, RecetteViewSet

router = DefaultRouter()
router.register(r'villes', VilleViewSet)
router.register(r'machines', MachineViewSet)
router.register(r'usines', UsineViewSet)
router.register(r'ressources', RessourceViewSet)
router.register(r'stocks', StockViewSet)
router.register(r'quantitesressource', QuantiteRessourceViewSet)
router.register(r'etapes', EtapeViewSet)
router.register(r'produits', ProduitViewSet)
router.register(r'recettes', RecetteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

