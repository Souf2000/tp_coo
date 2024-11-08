# high_level/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('villes/json/', views.ville_list_json, name='ville-list-json'),
]

