from django.http import JsonResponse, Http404
from .models import Ville, Machine, Usine, Ressource, Stock, QuantiteRessource, Etape, Produit, Recette

# Vue pour lister toutes les villes
def ville_list(request):
    villes = Ville.objects.all()
    data = [ville.json() for ville in villes]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une ville par ID
def ville_detail(request, id):
    try:
        ville = Ville.objects.get(id=id)
        return JsonResponse(ville.json())
    except Ville.DoesNotExist:
        raise Http404

# Vue pour lister toutes les ressources
def ressource_list(request):
    ressources = Ressource.objects.all()
    data = [ressource.json() for ressource in ressources]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une ressource par ID
def ressource_detail(request, id):
    try:
        ressource = Ressource.objects.get(id=id)
        return JsonResponse(ressource.json())
    except Ressource.DoesNotExist:
        raise Http404

# Vue pour lister toutes les machines
def machine_list(request):
    machines = Machine.objects.all()
    data = [machine.json() for machine in machines]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une machine par ID
def machine_detail(request, id):
    try:
        machine = Machine.objects.get(id=id)
        return JsonResponse(machine.json())
    except Machine.DoesNotExist:
        raise Http404

# Vue pour lister toutes les usines
def usine_list(request):
    usines = Usine.objects.all()
    data = [usine.json() for usine in usines]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une usine par ID
def usine_detail(request, id):
    try:
        usine = Usine.objects.get(id=id)
        return JsonResponse(usine.json())
    except Usine.DoesNotExist:
        raise Http404

# Vue pour lister tous les stocks
def stock_list(request):
    stocks = Stock.objects.all()
    data = [stock.json() for stock in stocks]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'un stock par ID
def stock_detail(request, id):
    try:
        stock = Stock.objects.get(id=id)
        return JsonResponse(stock.json())
    except Stock.DoesNotExist:
        raise Http404

# Vue pour lister toutes les quantités de ressources
def quantite_ressource_list(request):
    quantites = QuantiteRessource.objects.all()
    data = [quantite.json() for quantite in quantites]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une quantité de ressource par ID
def quantite_ressource_detail(request, id):
    try:
        quantite = QuantiteRessource.objects.get(id=id)
        return JsonResponse(quantite.json())
    except QuantiteRessource.DoesNotExist:
        raise Http404

# Vue pour lister toutes les étapes
def etape_list(request):
    etapes = Etape.objects.all()
    data = [etape.json() for etape in etapes]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une étape par ID
def etape_detail(request, id):
    try:
        etape = Etape.objects.get(id=id)
        return JsonResponse(etape.json())
    except Etape.DoesNotExist:
        raise Http404

# Vue pour lister tous les produits
def produit_list(request):
    produits = Produit.objects.all()
    data = [produit.json() for produit in produits]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'un produit par ID
def produit_detail(request, id):
    try:
        produit = Produit.objects.get(id=id)
        return JsonResponse(produit.json())
    except Produit.DoesNotExist:
        raise Http404

# Vue pour lister toutes les recettes
def recette_list(request):
    recettes = Recette.objects.all()
    data = [recette.json() for recette in recettes]
    return JsonResponse(data, safe=False)

# Vue pour afficher les détails d'une recette par ID
def recette_detail(request, id):
    try:
        recette = Recette.objects.get(id=id)
        return JsonResponse(recette.json())
    except Recette.DoesNotExist:
        raise Http404

