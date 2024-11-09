# high_level/views.py

from rest_framework import viewsets
from .models import Ville, Machine, Usine, Ressource, Stock, QuantiteRessource, Etape, Produit, Recette
from .serializers import VilleSerializer, MachineSerializer, UsineSerializer, RessourceSerializer, StockSerializer, QuantiteRessourceSerializer, EtapeSerializer, ProduitSerializer, RecetteSerializer

class VilleViewSet(viewsets.ModelViewSet):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class UsineViewSet(viewsets.ModelViewSet):
    queryset = Usine.objects.all()
    serializer_class = UsineSerializer

class RessourceViewSet(viewsets.ModelViewSet):
    queryset = Ressource.objects.all()
    serializer_class = RessourceSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class QuantiteRessourceViewSet(viewsets.ModelViewSet):
    queryset = QuantiteRessource.objects.all()
    serializer_class = QuantiteRessourceSerializer

class EtapeViewSet(viewsets.ModelViewSet):
    queryset = Etape.objects.all()
    serializer_class = EtapeSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer

class RecetteViewSet(viewsets.ModelViewSet):
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer

