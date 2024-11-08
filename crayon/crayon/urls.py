from django.urls import path
from .views import VilleDetailView

urlpatterns = [
    path('villes/<int:pk>/', VilleDetailView.as_view(), name='ville-detail'),
    # ... autres routes
]
