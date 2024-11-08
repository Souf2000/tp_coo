from django.views.generic import DetailView
from high_level.models import Ville

class VilleDetailView(DetailView):
    model = Ville
    template_name = 'ville_detail.html'  # Assurez-vous que ce template existe
