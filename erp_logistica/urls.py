# erp_logistica/urls.py

from django.contrib import admin
from django.urls import path, include

# -----------------------------------------------------------------
# CRÍTICO: Importa as classes de visualização de token do JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,    
)
# -----------------------------------------------------------------


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota para Rotas de Autenticação Customizadas (Registro)
    path('api/auth/', include('contas.urls')), 
    
    # -----------------------------------------------------------------
    # CRÍTICO: ADICIONAR ESTAS DUAS ROTAS DE TOKEN (LOGIN)
    # POST /api/token/ -> Login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # POST /api/token/refresh/ -> Refrescar Token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # -----------------------------------------------------------------
]