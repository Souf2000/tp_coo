from django.http import JsonResponse
from .models import Ville

def ville_detail_json(request, pk):
    try:
        ville = Ville.objects.get(pk=pk)
        data = ville.json()  # Utilise la méthode json de la classe Ville pour obtenir les données
    except Ville.DoesNotExist:
        return JsonResponse({"error": "Ville not found"}, status=404)
    
    return JsonResponse(data)


def ville_list_json(request):
    # Obtenez les trois premières villes
    villes = Ville.objects.all()
    
    # Préparez les données en JSON
    data = [ville.json() for ville in villes]
    
    return JsonResponse(data, safe=False)

