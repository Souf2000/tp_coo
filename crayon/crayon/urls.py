from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('high_level.urls')),  # Point d'entrée pour l'API de l'application
]

