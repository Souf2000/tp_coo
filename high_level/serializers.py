# high_level/serializers.py

from rest_framework import serializers
from .models import Ville, Machine, Usine, Ressource, Stock, QuantiteRessource, Etape, Produit, Recette

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class UsineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usine
        fields = '__all__'

class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ressource
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class QuantiteRessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantiteRessource
        fields = '__all__'

class EtapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etape
        fields = '__all__'

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = '__all__'

