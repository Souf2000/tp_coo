from django.http import JsonResponse
from .models import Ville, Machine, Usine, Ressource, Stock, QuantiteRessource, Etape, Produit, Recette

def ville_list(request):
    villes = [ville.json() for ville in Ville.objects.all()]
    return JsonResponse(villes, safe=False)

def machine_list(request):
    machines = [machine.json() for machine in Machine.objects.all()]
    return JsonResponse(machines, safe=False)

def usine_list(request):
    usines = [usine.json() for usine in Usine.objects.all()]
    return JsonResponse(usines, safe=False)

def ressource_list(request):
    ressources = [ressource.json() for ressource in Ressource.objects.all()]
    return JsonResponse(ressources, safe=False)

def stock_list(request):
    stocks = [stock.json() for stock in Stock.objects.all()]
    return JsonResponse(stocks, safe=False)

def quantiteressource_list(request):
    quantite_ressources = [qr.json() for qr in QuantiteRessource.objects.all()]
    return JsonResponse(quantite_ressources, safe=False)

def etape_list(request):
    etapes = [etape.json() for etape in Etape.objects.all()]
    return JsonResponse(etapes, safe=False)

def produit_list(request):
    produits = [produit.json() for produit in Produit.objects.all()]
    return JsonResponse(produits, safe=False)

def recette_list(request):
    recettes = [recette.json() for recette in Recette.objects.all()]
    return JsonResponse(recettes, safe=False)

