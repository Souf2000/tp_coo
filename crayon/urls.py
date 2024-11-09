from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Documentation LAHLALI Soufiane",
        default_version='v1',
        description="Documentation de l'API pour le projet tp_coo, réalisée par LAHLALI Soufiane",
        terms_of_service="http://localhost:8000/terms/",
        contact=openapi.Contact(email="soufiane.lahali@univ-tlse3.fr"),
        license=openapi.License(name="Licence tp_coo"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Cette ligne utilise l'import de 'admin'
    path('api/', include('high_level.urls')),  # Inclure les URLs de votre application ici
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

